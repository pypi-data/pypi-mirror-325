"""Abstraction layer for device interaction - Lock"""

from ..api import UHomeApi

class UtecLock():
    def __init__(self, device_id, api: UHomeApi):
        """Initialise the lock abstraction layer"""
        self._device = device_id
        self.api = api

    async def lock(self):
        """Lock the device"""
        return await self.api.send_command(self._device, "st.lock", "Lock")
    
    async def unlock(self):
        """Unlock the device"""
        return await self.api.send_command(self._device, "st.lock", "Unlock")