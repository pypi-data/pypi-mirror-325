"""Abstraction class for base devices"""

from ..api import UHomeApi
from ..exceptions import DeviceError
from ..const import (
    HandleType,
    DeviceCapability,
    HANDLE_TYPE_CAPABILITIES
)


class BaseDevice:
    """Base class for all U-Home devices."""

    def __init__(self, discovery_data: dict, api: UHomeApi) -> None:
        """Initialize a device."""
        self._discovery_data = discovery_data
        self._api = api
        self._id = discovery_data["id"]
        self._name = discovery_data["name"]
        self._handle_type = HandleType(discovery_data["handleType"])
        self._supported_capabilities = discovery_data["supportedCapabilities"]
        self._validate_capabilities()
        self._state_data = {}

    @property
    def id(self) -> str:
        """Return the device ID."""
        return self._discovery_data["id"]

    @property
    def supported_capabilities(self) -> set[DeviceCapability]:
        """Get the set of supported capabilities."""
        return self._supported_capabilities

    def has_capability(self, capability: DeviceCapability) -> bool:
        """Check if the device supports a specific capability."""
        return capability in self._supported_capabilities

    def _validate_capabilities(self) -> None:
        """Validate that the device has the required capabilities."""
        required_capabilities = HANDLE_TYPE_CAPABILITIES[self._handle_type]
        if not required_capabilities.issubset(self._supported_capabilities):
            missing = required_capabilities - self._supported_capabilities
            raise DeviceError(
                f"Device {self._id} missing required capabilities: {missing}"
            )