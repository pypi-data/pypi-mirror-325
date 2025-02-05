"""Abstraction layer for device interaction - switch"""

from ..api import UHomeApi

class UtecSwitch():
    def __init__(self, device_id, api: UHomeApi):
        """Initialise the switch abstraction layer"""
        self._device = device_id
        self.api = api
    
    async def turn_on(self):
        """Turn on the switch"""
        return await self.api.send_command(self._device, "st.switch", "on")

    async def turn_off(self):
        """Turn off the switch"""
        return await self.api.send_command(self._device, "st.switch", "off")

    async def set_level(self, level):
        """Set the level of the switch
        
            Not really sure what function this has for a switch, but if it is supported '0' turns the device off
            and anything above will turn the device on
            
        """
        return await self.api.send_command(self._device, "st.switch", "setLevel", {"level": level})