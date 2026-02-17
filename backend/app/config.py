"""Application configuration using Pydantic Settings."""

from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    # MongoDB Configuration
    mongodb_url: str = "mongodb://localhost:27017"
    mongodb_db_name: str = "amana_grc"

    # Redis Configuration
    redis_url: str = "redis://localhost:6379/0"

    # JWT Configuration
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 15
    jwt_refresh_token_expire_days: int = 7

    # LDAP Configuration
    ldap_server: str = "ldap://localhost:389"
    ldap_base_dn: str = "dc=example,dc=com"
    ldap_bind_dn: str = ""
    ldap_bind_password: str = ""
    ldap_user_search_base: str = "ou=users,dc=example,dc=com"
    ldap_user_search_filter: str = "(sAMAccountName={username})"

    # vLLM AI Configuration
    vllm_base_url: str = "http://localhost:8000"
    vllm_model_name: str = "Qwen/Qwen3-Coder-MoE"
    vllm_max_tokens: int = 2048
    vllm_temperature: float = 0.1

    # Application Configuration
    app_env: str = "development"
    app_debug: bool = True
    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:5173"]

    # Default Admin User
    default_admin_username: str = "admin"
    default_admin_password: str = "changeme"
    default_admin_email: str = "admin@example.com"


# Global settings instance
settings = Settings()
