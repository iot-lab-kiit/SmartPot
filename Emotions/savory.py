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

# Function to draw the savory emoji without blush
def draw_rotated_savory_emoji():
    clear_screen()

    # Face: Light yellow color to indicate joy from savoring
    face_color = tft.color(255, 255, 150)  # Light yellow color for contentment
    center_x, center_y = 64, 80
    radius = 50

    # Rotate center and draw face
    rotated_center_x, rotated_center_y = rotate_point(center_x, center_y, 64, 80)
    tft.fillcircle((rotated_center_x, rotated_center_y), radius, face_color)  # Rotated face

    # Eyes: Relaxed and expressive half-squinted eyes
    eye_color = TFT.BLACK
    eye_left_x, eye_left_y = 50, 70
    eye_right_x, eye_right_y = 78, 70

    # Rotate and draw eyes
    eye_left_rotated = rotate_point(eye_left_x, eye_left_y, center_x, center_y)
    eye_right_rotated = rotate_point(eye_right_x, eye_right_y, center_x, center_y)
    tft.fillcircle(eye_left_rotated, 6, eye_color)  # Slightly bigger eyes
    tft.fillcircle(eye_right_rotated, 6, eye_color)  # Slightly bigger eyes

    # Highlights on eyes (small white circles for extra expressiveness)
    highlight_color = tft.color(255, 255, 255)
    highlight_left_x = eye_left_rotated[0] + 2
    highlight_left_y = eye_left_rotated[1] - 2
    highlight_right_x = eye_right_rotated[0] + 2
    highlight_right_y = eye_right_rotated[1] - 2
    tft.fillcircle((highlight_left_x, highlight_left_y), 2, highlight_color)
    tft.fillcircle((highlight_right_x, highlight_right_y), 2, highlight_color)

    # Mouth: Slightly open, expressing joy from savoring (rotated)
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
    
    # Draw rotated mouth using the new coordinates (slightly open, joyful)
    tft.line(rotated_mouth_coords[0], rotated_mouth_coords[1], mouth_color)  # Left side of mouth
    tft.line(rotated_mouth_coords[2], rotated_mouth_coords[3], mouth_color)  # Bottom part of mouth
    tft.line(rotated_mouth_coords[4], rotated_mouth_coords[5], mouth_color)  # Right side of mouth

    # Aroma/Flavor Lines: Showcasing the savoriness coming from the food
    aroma_color = tft.color(255, 215, 0)  # Light yellow for aroma
    aroma_positions = [(30, 50), (100, 50), (60, 40), (60, 40)]
    aroma_end_positions = [(20, 40), (110, 40), (90, 20), (30, 20)]
    for (x, y), (x_end, y_end) in zip(aroma_positions, aroma_end_positions):
        x_rot, y_rot = rotate_point(x, y, center_x, center_y)
        x_end_rot, y_end_rot = rotate_point(x_end, y_end, center_x, center_y)
        tft.line((x_rot, y_rot), (x_end_rot, y_end_rot), aroma_color)  # Aroma line

    print("Rotated savory emoji without blush displayed!")

# Display the rotated savory emoji
draw_rotated_savory_emoji()

