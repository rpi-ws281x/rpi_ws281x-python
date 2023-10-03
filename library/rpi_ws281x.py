# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _rpi_ws281x
else:
    import _rpi_ws281x

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


WS2811_TARGET_FREQ = _rpi_ws281x.WS2811_TARGET_FREQ
SK6812_STRIP_RGBW = _rpi_ws281x.SK6812_STRIP_RGBW
SK6812_STRIP_RBGW = _rpi_ws281x.SK6812_STRIP_RBGW
SK6812_STRIP_GRBW = _rpi_ws281x.SK6812_STRIP_GRBW
SK6812_STRIP_GBRW = _rpi_ws281x.SK6812_STRIP_GBRW
SK6812_STRIP_BRGW = _rpi_ws281x.SK6812_STRIP_BRGW
SK6812_STRIP_BGRW = _rpi_ws281x.SK6812_STRIP_BGRW
SK6812_SHIFT_WMASK = _rpi_ws281x.SK6812_SHIFT_WMASK
WS2811_STRIP_RGB = _rpi_ws281x.WS2811_STRIP_RGB
WS2811_STRIP_RBG = _rpi_ws281x.WS2811_STRIP_RBG
WS2811_STRIP_GRB = _rpi_ws281x.WS2811_STRIP_GRB
WS2811_STRIP_GBR = _rpi_ws281x.WS2811_STRIP_GBR
WS2811_STRIP_BRG = _rpi_ws281x.WS2811_STRIP_BRG
WS2811_STRIP_BGR = _rpi_ws281x.WS2811_STRIP_BGR
WS2812_STRIP = _rpi_ws281x.WS2812_STRIP
SK6812_STRIP = _rpi_ws281x.SK6812_STRIP
SK6812W_STRIP = _rpi_ws281x.SK6812W_STRIP
class ws2811_channel_t(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    gpionum = property(_rpi_ws281x.ws2811_channel_t_gpionum_get, _rpi_ws281x.ws2811_channel_t_gpionum_set)
    invert = property(_rpi_ws281x.ws2811_channel_t_invert_get, _rpi_ws281x.ws2811_channel_t_invert_set)
    count = property(_rpi_ws281x.ws2811_channel_t_count_get, _rpi_ws281x.ws2811_channel_t_count_set)
    strip_type = property(_rpi_ws281x.ws2811_channel_t_strip_type_get, _rpi_ws281x.ws2811_channel_t_strip_type_set)
    leds = property(_rpi_ws281x.ws2811_channel_t_leds_get, _rpi_ws281x.ws2811_channel_t_leds_set)
    brightness = property(_rpi_ws281x.ws2811_channel_t_brightness_get, _rpi_ws281x.ws2811_channel_t_brightness_set)
    wshift = property(_rpi_ws281x.ws2811_channel_t_wshift_get, _rpi_ws281x.ws2811_channel_t_wshift_set)
    rshift = property(_rpi_ws281x.ws2811_channel_t_rshift_get, _rpi_ws281x.ws2811_channel_t_rshift_set)
    gshift = property(_rpi_ws281x.ws2811_channel_t_gshift_get, _rpi_ws281x.ws2811_channel_t_gshift_set)
    bshift = property(_rpi_ws281x.ws2811_channel_t_bshift_get, _rpi_ws281x.ws2811_channel_t_bshift_set)
    gamma = property(_rpi_ws281x.ws2811_channel_t_gamma_get, _rpi_ws281x.ws2811_channel_t_gamma_set)

    def __init__(self):
        _rpi_ws281x.ws2811_channel_t_swiginit(self, _rpi_ws281x.new_ws2811_channel_t())
    __swig_destroy__ = _rpi_ws281x.delete_ws2811_channel_t

# Register ws2811_channel_t in _rpi_ws281x:
_rpi_ws281x.ws2811_channel_t_swigregister(ws2811_channel_t)

class ws2811_t(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    render_wait_time = property(_rpi_ws281x.ws2811_t_render_wait_time_get, _rpi_ws281x.ws2811_t_render_wait_time_set)
    device = property(_rpi_ws281x.ws2811_t_device_get, _rpi_ws281x.ws2811_t_device_set)
    rpi_hw = property(_rpi_ws281x.ws2811_t_rpi_hw_get, _rpi_ws281x.ws2811_t_rpi_hw_set)
    freq = property(_rpi_ws281x.ws2811_t_freq_get, _rpi_ws281x.ws2811_t_freq_set)
    dmanum = property(_rpi_ws281x.ws2811_t_dmanum_get, _rpi_ws281x.ws2811_t_dmanum_set)
    channel = property(_rpi_ws281x.ws2811_t_channel_get, _rpi_ws281x.ws2811_t_channel_set)

    def __init__(self):
        _rpi_ws281x.ws2811_t_swiginit(self, _rpi_ws281x.new_ws2811_t())
    __swig_destroy__ = _rpi_ws281x.delete_ws2811_t

# Register ws2811_t in _rpi_ws281x:
_rpi_ws281x.ws2811_t_swigregister(ws2811_t)

WS2811_SUCCESS = _rpi_ws281x.WS2811_SUCCESS
WS2811_ERROR_GENERIC = _rpi_ws281x.WS2811_ERROR_GENERIC
WS2811_ERROR_OUT_OF_MEMORY = _rpi_ws281x.WS2811_ERROR_OUT_OF_MEMORY
WS2811_ERROR_HW_NOT_SUPPORTED = _rpi_ws281x.WS2811_ERROR_HW_NOT_SUPPORTED
WS2811_ERROR_MEM_LOCK = _rpi_ws281x.WS2811_ERROR_MEM_LOCK
WS2811_ERROR_MMAP = _rpi_ws281x.WS2811_ERROR_MMAP
WS2811_ERROR_MAP_REGISTERS = _rpi_ws281x.WS2811_ERROR_MAP_REGISTERS
WS2811_ERROR_GPIO_INIT = _rpi_ws281x.WS2811_ERROR_GPIO_INIT
WS2811_ERROR_PWM_SETUP = _rpi_ws281x.WS2811_ERROR_PWM_SETUP
WS2811_ERROR_MAILBOX_DEVICE = _rpi_ws281x.WS2811_ERROR_MAILBOX_DEVICE
WS2811_ERROR_DMA = _rpi_ws281x.WS2811_ERROR_DMA
WS2811_ERROR_ILLEGAL_GPIO = _rpi_ws281x.WS2811_ERROR_ILLEGAL_GPIO
WS2811_ERROR_PCM_SETUP = _rpi_ws281x.WS2811_ERROR_PCM_SETUP
WS2811_ERROR_SPI_SETUP = _rpi_ws281x.WS2811_ERROR_SPI_SETUP
WS2811_ERROR_SPI_TRANSFER = _rpi_ws281x.WS2811_ERROR_SPI_TRANSFER
WS2811_RETURN_STATE_COUNT = _rpi_ws281x.WS2811_RETURN_STATE_COUNT

def ws2811_init(ws2811):
    return _rpi_ws281x.ws2811_init(ws2811)

def ws2811_fini(ws2811):
    return _rpi_ws281x.ws2811_fini(ws2811)

def ws2811_render(ws2811):
    return _rpi_ws281x.ws2811_render(ws2811)

def ws2811_wait(ws2811):
    return _rpi_ws281x.ws2811_wait(ws2811)

def ws2811_get_return_t_str(state):
    return _rpi_ws281x.ws2811_get_return_t_str(state)

def ws2811_set_custom_gamma_factor(ws2811, gamma_factor):
    return _rpi_ws281x.ws2811_set_custom_gamma_factor(ws2811, gamma_factor)

def ws2811_led_get(channel, lednum):
    return _rpi_ws281x.ws2811_led_get(channel, lednum)

def ws2811_led_set(channel, lednum, color):
    return _rpi_ws281x.ws2811_led_set(channel, lednum, color)

def ws2811_channel_get(ws, channelnum):
    return _rpi_ws281x.ws2811_channel_get(ws, channelnum)

def ws2811_render_nogil(ws2811):
    return _rpi_ws281x.ws2811_render_nogil(ws2811)


