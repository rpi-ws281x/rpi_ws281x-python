import pytest

@pytest.fixture()
def strip(_rpi_ws281x):
    from rpi_ws281x import PixelStrip
    strip = PixelStrip(10, 20)
    strip.begin()
    strip.off()
    yield strip

def test_setup(_rpi_ws281x):
    from rpi_ws281x import PixelStrip
    strip = PixelStrip(10, 20)
    strip.begin()

def test_setup_compat(_rpi_ws281x):
    from rpi_ws281x import PixelStrip
    strip = PixelStrip(10, 20, strip_type=[1.0]*256)
    strip.begin()
    _rpi_ws281x.ws2811_channel_t_strip_type_set.assert_called_with(strip._channel,
                                                                   _rpi_ws281x.WS2811_STRIP_GRB)
    _rpi_ws281x.ws2811_channel_t_gamma_set.assert_called_with(strip._channel,[1.0]*256)

def test_setup_init_fail(_rpi_ws281x):
    from rpi_ws281x import PixelStrip
    _rpi_ws281x.ws2811_init.return_value = 1
    strip = PixelStrip(10, 20)
    with pytest.raises(RuntimeError):
        strip.begin()

def test_cleanup(_rpi_ws281x, strip):
    assert _rpi_ws281x.ws2811_fini.call_count == 0
    assert _rpi_ws281x.delete_ws2811_t.call_count == 0
    strip._cleanup()
    assert _rpi_ws281x.ws2811_fini.call_count == 1
    assert _rpi_ws281x.delete_ws2811_t.call_count == 1
    assert strip._leds is None
    assert strip._channel is None

def test_show(_rpi_ws281x, strip):
    assert _rpi_ws281x.ws2811_render.call_count == 1
    strip.show()
    assert _rpi_ws281x.ws2811_render.call_count == 2
    sub = strip.createPixelSubStrip(5, last=10)
    sub.show()
    assert _rpi_ws281x.ws2811_render.call_count == 3

    _rpi_ws281x.ws2811_render.return_value = 1
    with pytest.raises(RuntimeError):
        sub.show()

def test_brightness(_rpi_ws281x, strip):
    assert _rpi_ws281x.ws2811_channel_t_brightness_get.call_count == 0
    strip.getBrightness()
    assert _rpi_ws281x.ws2811_channel_t_brightness_get.call_count == 1
    calls = _rpi_ws281x.ws2811_channel_t_brightness_set.call_count
    strip.setBrightness(20)
    assert _rpi_ws281x.ws2811_channel_t_brightness_set.call_count == calls + 1

def test_gamma(_rpi_ws281x, strip):
    calls = _rpi_ws281x.ws2811_channel_t_gamma_set.call_count
    strip.setGamma(1.0)
    assert _rpi_ws281x.ws2811_channel_t_gamma_set.call_count == calls
    strip.setGamma([1.0, 1.0])
    assert _rpi_ws281x.ws2811_channel_t_gamma_set.call_count == calls
    strip.setGamma([1.0] * 256)
    assert _rpi_ws281x.ws2811_channel_t_gamma_set.call_count == calls + 1


def test_num_pixels(strip):
    assert len(strip[:]) == 10
    assert len(strip) == 10
    assert strip.numPixels() == 10

def test_set_pixel(strip):
    from rpi_ws281x import RGBW
    strip[0] = RGBW(255, 0, 0)
    assert strip[0] == strip.getPixelColor(0)
    assert strip[0] == RGBW(255, 0, 0)
    assert strip.getPixelColorRGB(0) == RGBW(255, 0, 0)
    assert strip.getPixelColorRGBW(0) == RGBW(255, 0, 0)
    assert strip.getPixelColorRGBW(0).r == 255

def test_set_multiple(strip):
    from rpi_ws281x import RGBW
    strip[:] = RGBW(255, 0, 0)
    assert strip[:] == [RGBW(255, 0, 0)] * 10

def test_set_pixel_slice(strip):
    from rpi_ws281x import RGBW
    colours = [RGBW(i*10, 0, 0) for i in range(0, 10)]
    strip[0:10] = colours
    for i in range(0, 10):
        assert strip[i] == RGBW(i*10, 0, 0)

def test_set_odd(strip):
    from rpi_ws281x import RGBW
    strip[::2] = RGBW(255, 0, 0)
    assert strip[:] == [RGBW(255, 0, 0), RGBW(0, 0, 0)] * 5


def test_create_substrip(strip):
    from rpi_ws281x import InvalidStrip
    with pytest.raises(InvalidStrip):
        sub = strip.createPixelSubStrip(100)
    with pytest.raises(InvalidStrip):
        sub = strip.createPixelSubStrip(5)
    with pytest.raises(InvalidStrip):
        sub = strip.createPixelSubStrip(5, 11)
    with pytest.raises(InvalidStrip):
        sub = strip.createPixelSubStrip(5, -2)
    with pytest.raises(InvalidStrip):
        sub = strip.createPixelSubStrip(5, num=6)
    with pytest.raises(InvalidStrip):
        sub = strip.createPixelSubStrip(-1, num=5)
    with pytest.raises(InvalidStrip):
        sub = strip.createPixelSubStrip(5, num=-2)
    sub = strip.createPixelSubStrip(5, last=10)
    assert len(sub[:]) == 5
    assert len(sub) == 5
    assert sub.numPixels() == 5
    sub = strip.createPixelSubStrip(5, num=5)
    assert len(sub[:]) == 5
    assert len(sub) == 5
    assert sub.numPixels() == 5

def test_adjust_pos(strip):
    sub = strip.createPixelSubStrip(5, 10)
    assert sub._adjust_pos(3) == 8
    assert sub._adjust_pos(-2) == 8
    assert sub._adjust_pos(slice(None, None)) == slice(5, 10)  # [:]
    assert sub._adjust_pos(slice(0, None)) == slice(5, 10)     # [0:]
    assert sub._adjust_pos(slice(None, 5)) == slice(5, 10)     # [:5]

    assert sub._adjust_pos(slice(-1, None)) == slice(9, 10)    # [-1:] (start, step default to None)
    assert sub._adjust_pos(slice(-2, None)) == slice(8, 10)    # [-2:]
    assert sub._adjust_pos(slice(None, -1)) == slice(5, 9)     # [:-1]
    assert sub._adjust_pos(slice(None, -2)) == slice(5, 8)     # [:-2]
    assert sub._adjust_pos(slice(-1, 0)) == slice(9, 5)        # [-1:0]

    assert sub._adjust_pos(slice(2, 4)) == slice(7, 9)         # [2:4]
    assert sub._adjust_pos(slice(None, None, -2)) == slice(5, 10, -2)  # [::-2]

def test_substrip_set(strip):
    from rpi_ws281x import RGBW
    sub = strip.createPixelSubStrip(5, 10)

    sub[0] = RGBW(1, 1, 1)
    assert strip[5] == RGBW(1, 1, 1)

    sub.setPixelColor(2, RGBW(2, 2, 2))
    assert strip[7] == RGBW(2, 2, 2)

    sub.setPixelColorRGB(3, 3, 4, 5)
    assert strip[8] == RGBW(3, 4, 5)

    strip.off()
    sub[1:4] = RGBW(1, 2, 3)
    assert strip[6:9] == sub[1:4]
    assert strip[6:9] == [RGBW(1, 2, 3)] * 3
    assert strip.getPixels() == [RGBW(0, 0, 0)] * 6 + [RGBW(1, 2, 3)] * 3 + [RGBW(0, 0, 0)]

    strip.off()
    colours = [RGBW(i, i, i) for i in range(1, 4)]
    sub[1:4] = colours
    print(f"strip is {strip[:]}")

    assert strip[6:9] == sub[1:4]
    assert strip[6:9] == colours

    strip.off()
    sub = strip.createPixelSubStrip(2, 10)

    sub[-1:0:-2] = [RGBW(i, i, i) for i in range(1, 9)]
    assert strip[:] == ([RGBW(0, 0, 0)]
                        + [RGBW(0, 0, 0)]
                        + [RGBW(0, 0, 0)]
                        + [RGBW(4, 4, 4)]
                        + [RGBW(0, 0, 0)]
                        + [RGBW(3, 3, 3)]
                        + [RGBW(0, 0, 0)]
                        + [RGBW(2, 2, 2)]
                        + [RGBW(0, 0, 0)]
                        + [RGBW(1, 1, 1)])

    strip.off()
    sub[-1:2:-2] = [RGBW(i, i, i) for i in range(1, 9)]
    assert strip[:] == ([RGBW(0, 0, 0)]
                        + [RGBW(0, 0, 0)]
                        + [RGBW(0, 0, 0)]
                        + [RGBW(0, 0, 0)]
                        + [RGBW(0, 0, 0)]
                        + [RGBW(3, 3, 3)]
                        + [RGBW(0, 0, 0)]
                        + [RGBW(2, 2, 2)]
                        + [RGBW(0, 0, 0)]
                        + [RGBW(1, 1, 1)])

def test_RGBW():
    from rpi_ws281x import RGBW
    c = RGBW(0x50)
    assert c == 0x50
    assert c.r == 0x00 and c.g == 0x00 and c.b == 0x50 and c.w == 0x0
    c = RGBW(0x50, g=0x60)
    assert c.r == 0x50 and c.g == 0x60 and c.b == 0x00 and c.w == 0x00
    c = RGBW(0x50, b=0x60)
    assert c.r == 0x50 and c.g == 0x00 and c.b == 0x60 and c.w == 0x00
    c = RGBW(0x50, 0x60, 0x70)
    assert c.r == 0x50 and c.g == 0x60 and c.b == 0x70 and c.w == 0x00
    c = RGBW(0x50, 0x60, 0x70, 0x80)
    assert c.r == 0x50 and c.g == 0x60 and c.b == 0x70 and c.w == 0x80
    assert c == (0x80 << 24) + (0x50 << 16) + (0x60 << 8) + 0x70
