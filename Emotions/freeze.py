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

# Function to draw a rotated freeze emoji
def draw_rotated_freeze_emoji():
    clear_screen()
    
    # Face: Light blue circle
    face_color = tft.color(173, 216, 230)  # Light blue color
    center_x, center_y = 64, 80
    radius = 50
    
    # Rotate center and draw face
    rotated_center_x, rotated_center_y = rotate_point(center_x, center_y, 64, 80)
    tft.fillcircle((rotated_center_x, rotated_center_y), radius, face_color)  # Rotated face

    # Eyes: Two small blue circles (rotate each eye)
    eye_color = TFT.BLUE
    eye_left_x, eye_left_y = 50, 70
    eye_right_x, eye_right_y = 78, 70
    eye_left_rotated = rotate_point(eye_left_x, eye_left_y, center_x, center_y)
    eye_right_rotated = rotate_point(eye_right_x, eye_right_y, center_x, center_y)
    tft.fillcircle(eye_left_rotated, 5, eye_color)  # Left eye
    tft.fillcircle(eye_right_rotated, 5, eye_color)  # Right eye

    # Mouth: Zig-zag line to show "chattering teeth"
    mouth_color = TFT.WHITE
    mouth_y = 100
    for x in range(45, 85, 10):  # Zig-zag from x=45 to x=85
        x_rot, y_rot = rotate_point(x, mouth_y, center_x, center_y)
        x_rot2, y_rot2 = rotate_point(x + 5, mouth_y + 5, center_x, center_y)
        tft.line((x_rot, y_rot), (x_rot2, y_rot2), mouth_color)  # Up stroke
        x_rot3, y_rot3 = rotate_point(x + 5, mouth_y + 5, center_x, center_y)
        x_rot4, y_rot4 = rotate_point(x + 10, mouth_y, center_x, center_y)
        tft.line((x_rot3, y_rot3), (x_rot4, y_rot4), mouth_color)  # Down stroke

    # Snowflakes: Small white stars around the face
    snowflake_color = TFT.WHITE
    snowflake_positions = [(20, 20), (100, 30), (30, 140), (110, 120)]
    for pos in snowflake_positions:
        x, y = pos
        x_rot, y_rot = rotate_point(x, y, center_x, center_y)
        tft.line((x_rot - 3, y_rot), (x_rot + 3, y_rot), snowflake_color)  # Horizontal line
        tft.line((x_rot, y_rot - 3), (x_rot, y_rot + 3), snowflake_color)  # Vertical line
        tft.line((x_rot - 2, y_rot - 2), (x_rot + 2, y_rot + 2), snowflake_color)  # Diagonal line \
        tft.line((x_rot - 2, y_rot + 2), (x_rot + 2, y_rot - 2), snowflake_color)  # Diagonal line /

    print("Rotated freeze emoji displayed!")

# Display the rotated freeze emoji
draw_rotated_freeze_emoji()

