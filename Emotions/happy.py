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

# Function to draw rotated happy emoji with expressive mouth
def draw_rotated_happy_emoji():
    clear_screen()
    
    # Face: Yellow circle
    face_color = tft.color(255, 255, 0)  # Yellow color
    center_x, center_y = 64, 80
    radius = 50

    # Rotate center and draw face
    rotated_center_x, rotated_center_y = rotate_point(center_x, center_y, 64, 80)
    tft.fillcircle((rotated_center_x, rotated_center_y), radius, face_color)  # Draw rotated face
    
    # Blush on cheeks (rotate blush as same as eyes)
    blush_color = tft.color(255, 182, 193)  # Light pink blush
    blush_left_x, blush_left_y = rotated_center_x - 30, rotated_center_y + 20  # More apart
    blush_right_x, blush_right_y = rotated_center_x + 30, rotated_center_y + 20  # More apart

    # Rotate the blush positions
    blush_left_rotated = rotate_point(blush_left_x, blush_left_y, center_x, center_y)
    blush_right_rotated = rotate_point(blush_right_x, blush_right_y, center_x, center_y)

    # Draw rotated blush
    tft.fillcircle(blush_left_rotated, 12, blush_color)  # Slightly bigger blush
    tft.fillcircle(blush_right_rotated, 12, blush_color)  # Slightly bigger blush

    # Eyes: Larger black circles with highlight
    eye_color = TFT.BLACK
    highlight_color = tft.color(255, 255, 255)  # White highlight
    eye_left_x, eye_left_y = 50, 70
    eye_right_x, eye_right_y = 78, 70

    # Rotate and draw eyes
    eye_left_rotated = rotate_point(eye_left_x, eye_left_y, center_x, center_y)
    eye_right_rotated = rotate_point(eye_right_x, eye_right_y, center_x, center_y)
    tft.fillcircle(eye_left_rotated, 8, eye_color)  # Larger eyes
    tft.fillcircle(eye_right_rotated, 8, eye_color)  # Larger eyes

    # Highlights on eyes (small white circles)
    highlight_left_x = eye_left_rotated[0] + 2
    highlight_left_y = eye_left_rotated[1] - 2
    highlight_right_x = eye_right_rotated[0] + 2
    highlight_right_y = eye_right_rotated[1] - 2
    tft.fillcircle((highlight_left_x, highlight_left_y), 2, highlight_color)
    tft.fillcircle((highlight_right_x, highlight_right_y), 2, highlight_color)

    # Mouth: Slightly open to show more expressive happiness (rotated)
    mouth_color = TFT.BLACK
    # Mouth coordinates before rotation
    mouth_coords = [
        (rotated_center_x - 19, rotated_center_y + 20),
        (rotated_center_x - 9, rotated_center_y + 30),
        (rotated_center_x - 9, rotated_center_y + 30),
        (rotated_center_x + 11, rotated_center_y + 30),
        (rotated_center_x + 11, rotated_center_y + 30),
        (rotated_center_x + 21, rotated_center_y + 20)
    ]
    
    # Apply rotation to each mouth coordinate
    rotated_mouth_coords = [rotate_point(x, y, center_x, center_y) for x, y in mouth_coords]
    
    # Draw rotated mouth using the new coordinates (open mouth)
    tft.line(rotated_mouth_coords[0], rotated_mouth_coords[1], mouth_color)  # Left side of mouth
    tft.line(rotated_mouth_coords[2], rotated_mouth_coords[3], mouth_color)  # Bottom part of mouth
    tft.line(rotated_mouth_coords[4], rotated_mouth_coords[5], mouth_color)  # Right side of mouth

    print("Rotated happy emoji with expressive mouth displayed!")

# Display the rotated happy emoji
draw_rotated_happy_emoji()

