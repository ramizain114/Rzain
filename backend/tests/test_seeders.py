"""Seeder tests."""

import pytest

from app.models.standard import Standard
from app.models.control import Control
from app.seeders import nca_ecc, nca_cscc, ndmo, sdaia


@pytest.mark.asyncio
async def test_nca_ecc_seeder_structure(db):
    """Test NCA-ECC seeder data structure."""
    assert nca_ecc.STANDARD_META['code'] == 'NCA-ECC'
    assert len(nca_ecc.CONTROLS) > 0
    
    # Check first control has all required fields
    first_control = nca_ecc.CONTROLS[0]
    required_fields = [
        'control_id', 'domain_en', 'domain_ar',
        'title_en', 'title_ar',
        'description_en', 'description_ar',
        'priority'
    ]
    
    for field in required_fields:
        assert field in first_control, f"Missing field: {field}"


@pytest.mark.asyncio
async def test_all_seeders_have_metadata(db):
    """Test that all seeders have proper metadata."""
    seeders = [nca_ecc, nca_cscc, ndmo, sdaia]
    
    for seeder in seeders:
        assert hasattr(seeder, 'STANDARD_META')
        assert hasattr(seeder, 'CONTROLS')
        
        meta = seeder.STANDARD_META
        assert 'code' in meta
        assert 'name_en' in meta
        assert 'name_ar' in meta
        assert 'version' in meta
        assert 'category' in meta
