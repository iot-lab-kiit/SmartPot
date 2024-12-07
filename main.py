import time
from machine import Pin, ADC, SPI
from ST7735 import TFT
from sysfont import sysfont

# Import emotion files
import happy  # happy.py
import thirsty  # thirsty.py
import sleepy  # sleepy.py
import hot  # hot.py
import freeze  # freeze.py
import savory  # savory.py

# Initialize the sensor pins
lm35_pin = ADC(Pin(26))  # LM35 connected to GP26
ldr_pin = ADC(Pin(27))   # LDR connected to GP27
soil_pin = ADC(Pin(28))  # Soil sensor connected to GP28

# Initialize the SPI interface for the display
spi = SPI(1, baudrate=20000000, polarity=0, phase=0,
          sck=Pin(10), mosi=Pin(11), miso=None)

# Initialize TFT display
tft = TFT(spi, 16, 17, 18)  # Adjust the GPIO pins for CS, Reset, and A0
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)

# Function to read analog sensor values
def read_sensor(pin):
    return pin.read_u16()  # Read the 16-bit value from the ADC

# Function to display text on the TFT display
def display_text(x, y, text, color):
    tft.text((x, y), text, color, sysfont)

# Define threshold values for the plant’s condition
temperature_threshold_high = 35  # Set lower threshold for hot condition (in °C)
temperature_threshold_low = 10   # Min optimal temperature for plants (in °C)
light_threshold_low = 20         # Minimum light intensity (0-100 scale)
soil_moisture_threshold_low = 40 # Min soil moisture to avoid thirst
soil_moisture_threshold_high = 60 # Max soil moisture for healthy watering

# Define function to normalize sensor readings to a 0-100 scale
def normalize_reading(value, min_val, max_val):
    return ((value - min_val) / (max_val - min_val)) * 100

# Define function to calculate combined plant condition and display emotion
def calculate_plant_condition(temperature, light_intensity, soil_moisture):
    # Normalize sensor values to 0-100 range
    temp_normalized = normalize_reading(temperature, 0, 50)  # Assuming temp range 0-50°C
    light_normalized = normalize_reading(light_intensity, 0, 100)  # Light: 0-100% scale
    soil_normalized = normalize_reading(soil_moisture, 0, 100)  # Soil moisture: 0-100% scale
    
    # Combine sensor readings with appropriate weights (higher weight to temperature and light)
    combined_score = 0.4 * temp_normalized + 0.4 * light_normalized + 0.2 * soil_normalized

    # Determine emotion based on combined score and conditions
    if combined_score < 30:
        # Stressed conditions: High temperature, low light, low soil moisture
        if temp_normalized < 20 and light_normalized < 10:
            freeze.draw_rotated_freeze_emoji()  # Extremely cold or no light
        elif soil_normalized < 40:
            thirsty.draw_rotated_thirsty_emoji()  # Low soil moisture
        else:
            freeze.draw_rotated_freeze_emoji()  # Low light and temperature
    elif 30 <= combined_score < 60:
        # Mild stress: Slightly unhappy, needs attention
        if soil_normalized > 80:
            savory.draw_rotated_savory_emoji()  # Overwatered
        elif temp_normalized < 20:
            freeze.draw_rotated_freeze_emoji()  # Too cold, plant is freezing
        else:
            sleepy.draw_rotated_sleepy_emoji()  # Slightly under-lit or under-watered
    elif combined_score >= 60:
        # Healthy, happy plant
        happy.draw_rotated_happy_emoji()  # Healthy and happy plant

# Main loop to display values on the TFT and show the plant's emotion
while True:
    # Read sensor values
    lm35_value = read_sensor(lm35_pin)
    ldr_value = read_sensor(ldr_pin)
    soil_value = read_sensor(soil_pin)

    # Convert the analog readings to a usable range
    temperature = (lm35_value / 65535) * 3.3 * 100  # LM35 temperature (in °C)
    light_intensity = 100 - ((ldr_value / 65535) * 100)  # Invert the light intensity
    soil_moisture = 100 - ((soil_value / 65535) * 100)  # Invert the soil moisture (if the sensor shows reverse behavior)

    # Print sensor readings to Thonny terminal
    print(f"Temperature: {temperature:.2f} °C")
    print(f"Light Intensity: {light_intensity:.2f} %")
    print(f"Soil Moisture: {soil_moisture:.2f} %")
    print(f"Raw Soil Sensor Value: {soil_value}")  # Print the raw soil sensor value

    # Clear the screen before updating the emotion
    tft.fill(TFT.BLACK)

    # Display the plant's emotional state based on its combined environment
    calculate_plant_condition(temperature, light_intensity, soil_moisture)

    # Wait for the next sensor reading
    time.sleep(2)  # Adjust the delay between updates if needed
