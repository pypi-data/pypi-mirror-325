""" Api class for Uhome/Utec API"""

from enum import Enum
import aiohttp
import logging

from uuid import uuid4
from typing import Dict, Any, Optional, TypedDict

from attr import dataclass

from .const import API_BASE_URL
from .exceptions import ApiError

logger = logging.getLogger(__name__)

@dataclass
class ApiNamespace(str, Enum):
    DEVICE = "Uhome.Device"
    USER = "Uhome.User"

@dataclass
class ApiOperation(str, Enum):
    DISCOVERY = "Discovery"
    QUERY = "Query"
    COMMAND = "Command"

@dataclass
class ApiHeader(TypedDict):
    namespace: str
    name: str
    messageID: str
    payloadVersion: str

@dataclass
class ApiRequest(TypedDict):
    header: ApiHeader
    payload: dict | None

class UHomeApi:
    """U-Home API client implementation"""

    def __init__(self, websession: aiohttp.ClientSession, token: str):
        """Initialise the API"""
        self.auth = websession
        self._token = token

    async def async_create_request(
        self,
        namespace: ApiNamespace,
        operation: ApiOperation,
        parameters: dict|None
    ) -> ApiRequest:
        """Create a standardised API request"""
        header = {
            "namespace": namespace,
            "name": operation,
            "messageID": str(uuid4()),
            "payloadVersion": "1",
        }
        return {
            "header": header,
            "payload": parameters
        }

    async def async_make_request(self, **kwargs):
        """Make an authenticated API request"""
        headers = {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json",
        }
        async with self.auth.post(API_BASE_URL, **kwargs) as response:
            if response.status == 204:
                return {}
            elif response.status in (200, 201, 202):
                return await response.json()
            else:
                error_text = await response.text()
                logger.error(f"API error: {response.status} - {error_text}")
                raise ApiError(response.status, error_text)

    async def discover_devices(self) -> Dict[str, Any]:
        """Discover available devices"""
        payload = await self.async_create_request(
            ApiNamespace.DEVICE,
            ApiOperation.DISCOVERY,
            None
        )
        return await self.async_make_request(json=payload)

    async def get_device_state(self, device_id: str) -> Dict[str, Any]:
        """Query device status."""
        params = {
            "devices": [{"id": device_id}]
        }
        payload = await self.async_create_request(
            ApiNamespace.DEVICE,
            ApiOperation.QUERY,
            params
        )
        return await self.async_make_request(json=payload)

    async def send_command(
        self,
        device_id: str,
        capability: str,
        command: str,
        arguments: dict | None
    ) -> Dict[str, Any]:
        """Send command to device"""
        command_data = {
            "capability": capability,
            "name": command
        }
        if arguments:
            command_data["arguments"] = arguments

        params = {
            "devices": [{
                "id": device_id,
                "command": command_data
            }]
        }

        payload = await self.async_create_request(
            ApiNamespace.DEVICE,
            ApiOperation.COMMAND,
            params
        )
        return await self.async_make_request(json=payload)

    async def close(self):
        """Close the API client"""
        await self.auth.close()
