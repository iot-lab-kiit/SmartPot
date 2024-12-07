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

# Function to draw smaller "ZZZ" letters
def draw_small_zzz(center_x, center_y, color):
    zzz_points = [
        [(55, 95), (65, 95), (60, 105), (70, 105)],   # First Z
        [(75, 95), (85, 95), (80, 105), (90, 105)],   # Second Z
        [(95, 95), (105, 95), (100, 105), (110, 105)]  # Third Z
    ]
    
    # Draw each Z with smaller size
    for z in zzz_points:
        for i in range(0, len(z), 2):
            x1, y1 = rotate_point(z[i][0], z[i][1], center_x, center_y)
            x2, y2 = rotate_point(z[i+1][0], z[i+1][1], center_x, center_y)
            tft.line((x1, y1), (x2, y2), color)

# Function to draw a rotated sleepy emoji
def draw_rotated_sleepy_emoji():
    clear_screen()

    # Face: Light yellow circle
    face_color = tft.color(255, 255, 128)  # Light yellow color for sleepy face
    center_x, center_y = 64, 80
    radius = 50
    
    # Rotate the face center and draw it
    rotated_center_x, rotated_center_y = rotate_point(center_x, center_y, 64, 80)
    tft.fillcircle((rotated_center_x, rotated_center_y), radius, face_color)

    # Eyes: Droopy eyes to show sleepiness (rotate each eye)
    eye_color = TFT.WHITE
    eye_left_x, eye_left_y = 50, 70
    eye_right_x, eye_right_y = 78, 70
    eye_left_rotated = rotate_point(eye_left_x, eye_left_y, center_x, center_y)
    eye_right_rotated = rotate_point(eye_right_x, eye_right_y, center_x, center_y)
    tft.fillcircle(eye_left_rotated, 8, eye_color)  # Left eye
    tft.fillcircle(eye_right_rotated, 8, eye_color)  # Right eye
    
    # Adding "sleepy" effect: Half-closed eyes (rotate each eye too)
    tft.fillcircle((eye_left_rotated[0], eye_left_rotated[1] + 2), 4, TFT.BLACK)  # Left half-closed eye
    tft.fillcircle((eye_right_rotated[0], eye_right_rotated[1] + 2), 4, TFT.BLACK)  # Right half-closed eye

    # Draw the smaller "ZZZ" symbol (replace mouth with ZZZ)
    zzz_color = TFT.CYAN  # Set ZZZ color to cyan
    draw_small_zzz(center_x, center_y, zzz_color)

    print("Rotated sleepy emoji displayed with smaller ZZZ replacing the mouth!")

# Display the rotated sleepy emoji
draw_rotated_sleepy_emoji()

