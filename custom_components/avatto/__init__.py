from homeassistant.core import HomeAssistant
from .const import DOMAIN, _LOGGER
from homeassistant.const import EVENT_HOMEASSISTANT_STOP
from homeassistant.config_entries import ConfigEntry


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Avatto component."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "cover")
    )
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    return await hass.config_entries.async_forward_entry_unload(entry, "cover")
