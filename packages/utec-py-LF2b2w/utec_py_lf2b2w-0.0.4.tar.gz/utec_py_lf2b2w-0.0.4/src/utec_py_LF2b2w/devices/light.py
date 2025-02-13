"""Abstraction layer for device interaction - Light"""

from ..api import UHomeApi

class UtecLight():
    def __init__(self, device_id, api: UHomeApi):
        """Initialise the light abstraction layer"""
        self._device = device_id
        self.api = api

    async def turn_on(self):
        """Turn on the light."""
        return await self.api.send_command(self._device, "st.switch", "on")

    async def turn_off(self):
        """Turn off the light."""
        return await self.api.send_command(self._device, "st.switch", "off")

    """Currently nothing has been implemented in the API for light devices, however it seems like
        they will use the switch device functions to map to lights.
 
    """
    #async def set_brightness(self, level):
    #    return await self.api.send_command(self._device, "st.switch", "setLevel", {"level", level})

    #async def set_color(self, color):
    #    return await self.api.send_command(self._device, "*Placeholder", "setColor", "*placeholder")

    #async def set_colorTemperature(self, CT):
    #   return await self.api.send_command(self._device, "*Placeholder", "setColourTemperature", "*Placeholder")
