"""Authentication service with LDAP and local auth support."""

import logging
from datetime import datetime
from typing import Optional, Tuple
from ldap3 import Server, Connection, ALL, SIMPLE
from ldap3.core.exceptions import LDAPException

from app.config import settings
from app.models.user import User, Role
from app.core.security import verify_password, get_password_hash, create_access_token, create_refresh_token
from app.core.exceptions import AuthenticationError, LDAPConnectionError

logger = logging.getLogger(__name__)


class AuthService:
    """Authentication service handling LDAP and local auth."""

    async def authenticate_user(self, username: str, password: str) -> Tuple[User, str, str]:
        """
        Authenticate user via LDAP or local database.

        Returns:
            Tuple of (user, access_token, refresh_token)
        """
        # Try LDAP authentication first
        ldap_user = await self._authenticate_ldap(username, password)
        if ldap_user:
            user = await self._sync_ldap_user(ldap_user)
            tokens = self._generate_tokens(user)
            return user, tokens[0], tokens[1]

        # Fallback to local authentication
        user = await self._authenticate_local(username, password)
        if user:
            tokens = self._generate_tokens(user)
            return user, tokens[0], tokens[1]

        raise AuthenticationError("Invalid username or password")

    async def _authenticate_ldap(self, username: str, password: str) -> Optional[dict]:
        """Authenticate against LDAP/Active Directory."""
        try:
            # Connect to LDAP server
            server = Server(settings.ldap_server, get_info=ALL)

            # Build user DN for binding
            user_dn = f"uid={username},{settings.ldap_user_search_base}"

            # Try to bind with user credentials
            conn = Connection(
                server,
                user=user_dn,
                password=password,
                authentication=SIMPLE,
                auto_bind=True
            )

            if not conn.bound:
                return None

            # Search for user attributes
            search_filter = settings.ldap_user_search_filter.format(username=username)
            conn.search(
                settings.ldap_user_search_base,
                search_filter,
                attributes=['mail', 'cn', 'givenName', 'sn', 'memberOf']
            )

            if not conn.entries:
                return None

            entry = conn.entries[0]

            # Extract user information
            user_info = {
                'username': username,
                'email': str(entry.mail) if hasattr(entry, 'mail') else f"{username}@municipality.gov.sa",
                'full_name_en': str(entry.cn) if hasattr(entry, 'cn') else username,
                'full_name_ar': username,  # Would need to be stored in LDAP
                'role': self._determine_role_from_ldap(entry),
            }

            conn.unbind()
            logger.info(f"LDAP authentication successful for user: {username}")
            return user_info

        except LDAPException as e:
            logger.warning(f"LDAP authentication failed for {username}: {e}")
            return None
        except Exception as e:
            logger.error(f"LDAP error: {e}")
            return None

    def _determine_role_from_ldap(self, entry) -> Role:
        """Determine user role based on LDAP group membership."""
        # Check group memberships
        if hasattr(entry, 'memberOf'):
            groups = [str(g).lower() for g in entry.memberOf]

            if any('admin' in g for g in groups):
                return Role.ADMIN
            elif any('risk' in g for g in groups):
                return Role.RISK_OFFICER
            elif any('audit' in g for g in groups):
                return Role.AUDITOR

        return Role.VIEWER

    async def _sync_ldap_user(self, ldap_user: dict) -> User:
        """Sync LDAP user to database."""
        user = await User.find_one(User.username == ldap_user['username'])

        if user:
            # Update existing user
            user.email = ldap_user['email']
            user.full_name_en = ldap_user['full_name_en']
            user.full_name_ar = ldap_user['full_name_ar']
            user.role = ldap_user['role']
            user.last_login = datetime.utcnow()
            user.is_ldap_user = True
            await user.save()
        else:
            # Create new user from LDAP
            user = User(
                username=ldap_user['username'],
                email=ldap_user['email'],
                full_name_en=ldap_user['full_name_en'],
                full_name_ar=ldap_user['full_name_ar'],
                role=ldap_user['role'],
                is_ldap_user=True,
                is_active=True,
                last_login=datetime.utcnow(),
            )
            await user.insert()

        return user

    async def _authenticate_local(self, username: str, password: str) -> Optional[User]:
        """Authenticate against local database."""
        user = await User.find_one(User.username == username, User.is_active == True)

        if not user or not user.hashed_password:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        # Update last login
        user.last_login = datetime.utcnow()
        await user.save()

        logger.info(f"Local authentication successful for user: {username}")
        return user

    def _generate_tokens(self, user: User) -> Tuple[str, str]:
        """Generate access and refresh tokens."""
        token_data = {
            "sub": str(user.id),
            "username": user.username,
            "role": user.role.value,
        }

        access_token = create_access_token(token_data)
        refresh_token = create_refresh_token(token_data)

        return access_token, refresh_token

    async def create_local_user(self, username: str, email: str, password: str, **kwargs) -> User:
        """Create a local user account."""
        # Check if user exists
        existing = await User.find_one(User.username == username)
        if existing:
            raise AuthenticationError("Username already exists")

        # Create user
        user = User(
            username=username,
            email=email,
            hashed_password=get_password_hash(password),
            is_ldap_user=False,
            is_active=True,
            **kwargs
        )
        await user.insert()

        logger.info(f"Created local user: {username}")
        return user
