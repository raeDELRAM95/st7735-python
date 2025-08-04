import time

from PIL import Image, ImageDraw, ImageFont

import st7735

MESSAGE = "USC NCR Lab Project - Incubator"

# Create ST7735 LCD display class.
disp = st7735.ST7735(
    port=0,
    cs=st7735.BG_SPI_CS_BACK,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT. BG_SPI_CS_FRONT (eg: CE1) for Enviro Plus
    dc="GPIO24",                 # "GPIO9" / "PIN21". "PIN21" for a Pi 5 with Enviro Plus
#    backlight="GPIO22",          # "PIN18" for back BG slot, "PIN19" for front BG slot. "PIN32" for a Pi 5 with Enviro Plus
    rst="GPIO25",
    rotation=0,
    invert=False,
    spi_speed_hz=16000000
)

# Initialize display.
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height


img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)

x1, y1, x2, y2 = font.getbbox(MESSAGE)
size_x = x2 - x1
size_y = y2 - y1

text_x = 160
text_y = (80 - size_y) // 2

t_start = time.time()

while True:
    x = (time.time() - t_start) * 100
    x %= (size_x + 160)
    draw.rectangle((0, 0, 160, 80), (0, 0, 0))
    draw.text((int(text_x - x), text_y), MESSAGE, font=font, fill=(255, 255, 255))
    disp.display(img)
