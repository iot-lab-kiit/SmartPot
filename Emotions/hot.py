from ST7735 import TFT
from machine import SPI, Pin
import math  # Import math module for trigonometry

# SPI setup
spi = SPI(1, baudrate=20000000, polarity=0, phase=0,
          sck=Pin(10), mosi=Pin(11), miso=None)
tft = TFT(spi, 16, 17, 18)
tft.initr()
tft.rgb(True)

# Function to clear the screen
def clear_screen():
    tft.fill(TFT.BLACK)

# Function to rotate a point (x, y) by 90 degrees around (cx, cy)
def rotate_point(x, y, cx, cy):
    x_new = cy - y + cx
    y_new = x - cx + cy
    return (x_new, y_new)

# Function to draw a rotated hot emoji (feeling too hot)
def draw_rotated_hot_emoji():
    clear_screen()
    
    # Sun: Red circle to symbolize intense heat
    sun_color = tft.color(255, 0, 0)  # Red color for the sun
    center_x, center_y = 64, 80
    radius = 40
    
    # Rotate center and draw sun
    rotated_center_x, rotated_center_y = rotate_point(center_x, center_y, 64, 80)
    tft.fillcircle((rotated_center_x, rotated_center_y), radius, sun_color)  # Rotated sun

    # Heat waves: Wavy lines around the sun
    wave_color = tft.color(255, 100, 0)  # Orange color for heat waves
    for angle in range(0, 360, 15):  # Rays at smaller intervals for more waves
        for dist in range(5, 15, 5):  # Different distances for wavy effect
            x_start = center_x + (radius + dist) * math.cos(math.radians(angle))
            y_start = center_y + (radius + dist) * math.sin(math.radians(angle))
            x_end = center_x + (radius + dist + 5) * math.cos(math.radians(angle))
            y_end = center_y + (radius + dist + 5) * math.sin(math.radians(angle))
            
            # Convert coordinates to integers
            x_rot_start, y_rot_start = rotate_point(int(x_start), int(y_start), center_x, center_y)
            x_rot_end, y_rot_end = rotate_point(int(x_end), int(y_end), center_x, center_y)
            
            tft.line((x_rot_start, y_rot_start), (x_rot_end, y_rot_end), wave_color)  # Heat wave

    # Sweating face: Sweat drops to show discomfort
    sweat_color = TFT.CYAN
    sweat_positions = [(50, 70), (78, 70), (60, 110)]  # Some sweat positions
    for pos in sweat_positions:
        x, y = pos
        x_rot, y_rot = rotate_point(x, y, center_x, center_y)
        tft.fillcircle((x_rot, y_rot), 3, sweat_color)  # Sweat drops
    
    print("Rotated hot emoji with heat effect displayed!")

# Display the rotated hot emoji
draw_rotated_hot_emoji()

