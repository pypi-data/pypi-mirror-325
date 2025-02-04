import asyncio
import aiohttp
import pytest
from redgtech_api import RedgtechAPI

@pytest.mark.asyncio
async def test_get_data():
    api = RedgtechAPI("pypi-AgEIcHlwaS5vcmcCJDVjYmNjY2NhLWI1MjctNGU2OS1hM2NlLTU5NDM0Mjg0YzNhYwACKlszLCJmYjQ2ZWMxNC04ZmUyLTRhMDQtOTJjYS0wZDdjOWZkYWExZjgiXQAABiCYSH-_FZq8qEKHUpXXbShUR1bGSqrhmRxzKBzbJ4fPZg")
    data = await api.get_data()
    assert "boards" in data
    await api.close()

@pytest.mark.asyncio
async def test_set_switch_state():
    api = RedgtechAPI("pypi-AgEIcHlwaS5vcmcCJDVjYmNjY2NhLWI1MjctNGU2OS1hM2NlLTU5NDM0Mjg0YzNhYwACKlszLCJmYjQ2ZWMxNC04ZmUyLTRhMDQtOTJjYS0wZDdjOWZkYWExZjgiXQAABiCYSH-_FZq8qEKHUpXXbShUR1bGSqrhmRxzKBzbJ4fPZg")
    success = await api.set_switch_state("endpoint_id", True)
    assert success
    await api.close()

@pytest.mark.asyncio
async def test_set_light_brightness():
    api = RedgtechAPI("pypi-AgEIcHlwaS5vcmcCJDVjYmNjY2NhLWI1MjctNGU2OS1hM2NlLTU5NDM0Mjg0YzNhYwACKlszLCJmYjQ2ZWMxNC04ZmUyLTRhMDQtOTJjYS0wZDdjOWZkYWExZjgiXQAABiCYSH-_FZq8qEKHUpXXbShUR1bGSqrhmRxzKBzbJ4fPZg")
    success = await api.set_light_brightness("endpoint_id", 128)
    assert success
    await api.close()