"""Database seeder runner for Saudi regulatory standards."""

import asyncio
import argparse
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.config import settings
from app.models import DOCUMENT_MODELS
from app.models.standard import Standard
from app.models.control import Control, ImplementationStatus

# Import seeder data
from app.seeders import nca_ecc, nca_cscc, ndmo, sdaia

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SEEDERS = {
    'nca-ecc': nca_ecc,
    'nca-cscc': nca_cscc,
    'ndmo': ndmo,
    'sdaia': sdaia,
}


async def seed_standard(seeder_module):
    """Seed a standard and its controls."""
    standard_meta = seeder_module.STANDARD_META
    controls_data = seeder_module.CONTROLS
    
    logger.info(f"Seeding standard: {standard_meta['code']}")
    
    # Check if standard already exists
    existing = await Standard.find_one(Standard.code == standard_meta['code'])
    
    if existing:
        logger.info(f"Standard {standard_meta['code']} already exists, updating...")
        for key, value in standard_meta.items():
            setattr(existing, key, value)
        standard = existing
        await standard.save()
    else:
        # Create new standard
        standard = Standard(**standard_meta)
        await standard.insert()
        logger.info(f"Created standard: {standard.code}")
    
    # Seed controls
    controls_created = 0
    controls_updated = 0
    
    for control_data in controls_data:
        # Check if control already exists
        existing_control = await Control.find_one(
            Control.control_id == control_data['control_id']
        )
        
        if existing_control:
            # Update existing control
            for key, value in control_data.items():
                if key != 'control_id':
                    setattr(existing_control, key, value)
            existing_control.standard = standard
            await existing_control.save()
            controls_updated += 1
        else:
            # Create new control
            control = Control(
                standard=standard,
                implementation_status=ImplementationStatus.NOT_IMPLEMENTED,
                **control_data
            )
            await control.insert()
            controls_created += 1
    
    logger.info(
        f"Standard {standard.code}: "
        f"{controls_created} controls created, "
        f"{controls_updated} controls updated"
    )
    
    return {
        'standard': standard.code,
        'controls_created': controls_created,
        'controls_updated': controls_updated,
    }


async def seed_all():
    """Seed all standards."""
    results = []
    
    for name, seeder in SEEDERS.items():
        result = await seed_standard(seeder)
        results.append(result)
    
    return results


async def reset_all():
    """Delete all standards and controls."""
    logger.warning("Resetting all standards and controls...")
    
    await Control.delete_all()
    await Standard.delete_all()
    
    logger.info("All standards and controls deleted")


async def main():
    """Main seeder entry point."""
    parser = argparse.ArgumentParser(description='Seed Saudi regulatory standards')
    parser.add_argument(
        '--standard',
        choices=['nca-ecc', 'nca-cscc', 'ndmo', 'sdaia'],
        help='Specific standard to seed'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Seed all standards'
    )
    parser.add_argument(
        '--reset',
        action='store_true',
        help='Reset all data before seeding'
    )
    
    args = parser.parse_args()
    
    # Connect to database
    client = AsyncIOMotorClient(settings.mongodb_url)
    db = client[settings.mongodb_db_name]
    
    await init_beanie(database=db, document_models=DOCUMENT_MODELS)
    logger.info("Connected to MongoDB")
    
    try:
        # Reset if requested
        if args.reset:
            await reset_all()
        
        # Seed standards
        if args.all:
            logger.info("Seeding all standards...")
            results = await seed_all()
            
            logger.info("\n=== Seeding Summary ===")
            total_created = sum(r['controls_created'] for r in results)
            total_updated = sum(r['controls_updated'] for r in results)
            
            for result in results:
                logger.info(
                    f"  {result['standard']}: "
                    f"+{result['controls_created']} "
                    f"~{result['controls_updated']} controls"
                )
            
            logger.info(
                f"\nTotal: {total_created} created, {total_updated} updated"
            )
            
        elif args.standard:
            logger.info(f"Seeding standard: {args.standard}")
            seeder = SEEDERS[args.standard]
            result = await seed_standard(seeder)
            
            logger.info("\n=== Seeding Summary ===")
            logger.info(
                f"{result['standard']}: "
                f"{result['controls_created']} created, "
                f"{result['controls_updated']} updated"
            )
        else:
            parser.print_help()
            
    finally:
        client.close()
        logger.info("Disconnected from MongoDB")


if __name__ == "__main__":
    asyncio.run(main())
