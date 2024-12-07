from ST7735 import TFT
from machine import SPI, Pin

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

# Function to draw a rotated droplet-like emoji with eyes
def draw_rotated_droplet_emoji():
    clear_screen()
    
    # Droplet Shape: Using multiple filled circles to simulate a droplet
    droplet_color = tft.color(0, 255, 255)  # Light blue color (water-like)
    center_x, center_y = 64, 80
    base_radius = 50
    top_radius = 35

    # Rotate the center of the droplet
    rotated_center_x, rotated_center_y = rotate_point(center_x, center_y, 64, 80)

    # Draw the upper part of the droplet (smaller circle)
    rotated_top_x, rotated_top_y = rotate_point(center_x, center_y - 10, 64, 80)
    tft.fillcircle((rotated_top_x, rotated_top_y), top_radius, droplet_color)

    # Draw the bottom part of the droplet (larger circle)
    rotated_bottom_x, rotated_bottom_y = rotate_point(center_x, center_y + 20, 64, 80)
    tft.fillcircle((rotated_bottom_x, rotated_bottom_y), base_radius, droplet_color)

    # Eyes: Two small black circles inside the droplet (rotate each eye)
    eye_color = TFT.BLACK
    eye_left_x, eye_left_y = 50, 70
    eye_right_x, eye_right_y = 78, 70

    # Rotate the eye positions
    eye_left_rotated = rotate_point(eye_left_x, eye_left_y, center_x, center_y)
    eye_right_rotated = rotate_point(eye_right_x, eye_right_y, center_x, center_y)

    tft.fillcircle(eye_left_rotated, 5, eye_color)  # Left eye
    tft.fillcircle(eye_right_rotated, 5, eye_color)  # Right eye

    print("Rotated droplet emoji with eyes displayed!")

# Display the rotated droplet emoji
draw_rotated_droplet_emoji()

