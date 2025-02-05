"""Utec-py constants."""

AUTH_BASE_URL = "https://oauth.u-tec.com/authorize?"
TOKEN_BASE_URL = "https://oauth.u-tec.com/token?"
API_BASE_URL = "https://api.u-tec.com/action"

ATTR_HANDLE_TYPE = "handleType"
ATTR_DEVICE_ID = "id"
ATTR_NAME = "name"
ATTR_CATEGORY = "category"
ATTR_DEVICE_INFO = "deviceInfo"
ATTR_ATTRIBUTES = "attributes"

class HandleType:
    """Handle types for device capabilities"""
    UTEC_LOCK = "utec-lock"
    UTEC_LOCK_SENSOR = "utec-lock-sensor"
    UTEC_DIMMER = "utec-dimmer"
    UTEC_LIGHT_RGBAW = "utec-light-rgbaw-br"
    UTEC_SWITCH = "utec-switch"

class DeviceCapability:
    """Device capabilities"""
    SWITCH = "Switch"
    LOCK = "Lock"
    BATTERY_LEVEL = "BatteryLevel"
    LOCK_USER = "LockUser"
    DOOR_SENSOR = "DoorSensor"
    BRIGHTNESS = "Brightness"
    COLOR = "Color"
    COLOR_TEMPERATURE = "ColorTemperature"
    SWITCH_LEVEL = "Switch Level"

# Mapping of handle types to their required capabilities
HANDLE_TYPE_CAPABILITIES = {
    HandleType.UTEC_LOCK: {
        DeviceCapability.LOCK,
        DeviceCapability.BATTERY_LEVEL,
        DeviceCapability.LOCK_USER
    },
    HandleType.UTEC_LOCK_SENSOR: {
        DeviceCapability.LOCK,
        DeviceCapability.BATTERY_LEVEL,
        DeviceCapability.DOOR_SENSOR
    },
    HandleType.UTEC_DIMMER: {
        DeviceCapability.SWITCH,
        DeviceCapability.SWITCH_LEVEL
    },
    HandleType.UTEC_LIGHT_RGBAW: {
        DeviceCapability.SWITCH,
        DeviceCapability.BRIGHTNESS,
        DeviceCapability.COLOR,
        DeviceCapability.COLOR_TEMPERATURE
    },
    HandleType.UTEC_SWITCH: {
        DeviceCapability.SWITCH
    }
}