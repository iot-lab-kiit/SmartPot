# 🌿 **PlantPal: Smart Plant Pot**

**PlantPal** is an innovative, smart plant pot that brings your plant to life by displaying emotions based on its needs. Using data from moisture, temperature, and light sensors, **PlantPal** provides feedback on your plant's health, making it feel more like a pet. By showing emotions like **"Thirsty"** or **"Happy,"** it fosters an interactive and caring relationship between you and your plant.

This project is designed to be simple and straightforward, creating a professional yet accessible way to enhance plant care using technology.

---

### **Features**

**PlantPal** displays six different emotions based on sensor data:

1. **Thirsty**  
   *Emotion*: 💧 (Thirsty Emoji)  
   *Description*: The plant needs water.  
   <img src="pictures%20of%20emotions/thirsty.jpg" width="120" />

2. **Hot**  
   *Emotion*: 🌞 (Red Sun Emoji)  
   *Description*: The plant is too hot and needs cooling.  
   <img src="pictures%20of%20emotions/hot.jpg" width="120" />

3. **Cold**  
   *Emotion*: ❄️ (Freeze Emoji)  
   *Description*: The plant is too cold and needs warmth.  
   <img src="pictures%20of%20emotions/cold.jpg" width="120" />

4. **Happy**  
   *Emotion*: 😊 (Happy Emoji)  
   *Description*: The plant is healthy and well-cared-for.  
   <img src="pictures%20of%20emotions/happy.jpg" width="120" />

5. **Savory**  
   *Emotion*: 😋 (Savory Emoji)  
   *Description*: The plant is enjoying optimal conditions.  
   <img src="pictures%20of%20emotions/savory.jpg" width="120" />

6. **Sleepy**  
   *Emotion*: 💤 (Sleep Emoji)  
   *Description*: The plant is resting or in low-energy mode.  
   <img src="pictures%20of%20emotions/sleepy.jpg" width="120" />


---

### **How It Works**

1. **Set Up the Sensors**  
   - Connect the **LM35 temperature sensor**, **LDR light sensor**, and **capacitive soil moisture sensor** to your **PlantPal** pot.

2. **Install the Necessary Software**  
   - Install the required **MicroPython** libraries for sensor readings.

3. **Connect the Display**  
   - Hook up the **1.8-inch display** to show the emotions of the plant.

4. **Copy the Code to Raspberry Pi Pico**  
   - Open **Thonny** and flash your **Raspberry Pi Pico** with **MicroPython**.
   - Copy the code files from your project folder to the Pico individually (e.g., copy two code files from the `lib` folder to the Pico).
   - **Note**: Avoid copying the entire folder to the Pico; instead, copy only the necessary files.

5. **Power Up and Monitor**  
   - Once powered on, the **PlantPal** will start monitoring the plant’s conditions and display its emotions accordingly.

---

### **Components**

Here is a list of the essential components used in the **PlantPal** project:

1. **Raspberry Pico W**  
   *Product Link*: [Raspberry Pico W](https://amazon.in/Raspberry-Support-RP2040-Dual-core-Processor/dp/B0DL4GLK79/ref=sr_1_3?sr=8-3)

2. **LM35 Temperature Sensor**  
   *Product Link*: [LM35 Temperature Sensor](https://www.amazon.in/LM35DZ-LM35-Temperature-Sensor-Voltage/dp/B0B2WZDSDY?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=AJ6SIZC8YQDZX)

3. **LDR Light Sensor**  
   *Product Link*: [LDR Light Sensor](https://www.amazon.in/HemCorp-sensitive-Resistor-intensity-RASPBERRY/dp/B09NP5M331/ref=sr_1_10?s=industrial&sr=1-10)

4. **Capacitive Soil Moisture Sensor**  
   *Product Link*: [Capacitive Soil Moisture Sensor](https://www.amazon.in/RoboElectrixx-Capacitive-Moisture-Voltage-Anti-Corrosion/dp/B0CC8JHP19/ref=sr_1_2?s=industrial&sr=1-2)

5. **1.8-inch Display**  
   *Product Link*: [1.8-inch Display](https://www.amazon.in/Display-Module-Support-Hardware-128x160/dp/B0CG3K93DL/ref=sr_1_2?sr=8-2)

6. **Bread Board**  
   *Product Link*: [Bread Board](https://www.amazon.in/Generic-Elementz-Solderless-Piecesb-Circuit/dp/B00MC1CCZQ/ref=sr_1_5?sr=8-5)

6. **Jumper Wires**  
   *Product Link*: [Jumper Wires](https://www.amazon.in/Aptechdeals-Jumper-Wires-Female-Breadboard/dp/B074JB6SX8/ref=sr_1_3?sr=8-3)

> **Note**: You can purchase these components from any retailer at a cheaper price. The links provided are for reference.Also i'm using pico w here but you can simply use pico if you don't intend to add any wifi capabilities from your side since this version dosen't use the wifi capabiities.

---

### **Circuit Diagram**

A clear and simple circuit diagram of the **PlantPal** setup, showing how each sensor and component is connected.

 <img src="Circuit%20Diagram/circuit%20diagram.jpg" width="300" />

---

### **Pin Table**

A reference pin table indicating the correct GPIO pins for each sensor and component on the **Raspberry Pi Pico**.

<img src="Circuit%20Diagram/pin%20layout.jpg" width="300" />

---

### **Breadboard Model**

A breadboard-based model of the **PlantPal** project to help you visualize the setup and connections.

<img src="Circuit%20Diagram/represnetation%20of%20circuit%20in%20bread%20board.jpg" width="300" />

---

### **Requirements**

- **Sensors**: LM35 (Temperature Sensor), LDR (Light Sensor), Capacitive Soil Moisture Sensor.
- **Display**: 1.8-inch display for showing plant emotions.
- **Platform**: Raspberry Pi Pico W (or similar).
- **Software**: **MicroPython** flashed onto Raspberry Pi Pico, **Thonny** for coding.

---

### **License**

This project is in its **Version 1.0** stage. Future versions will include additional features and improvements. License information will be added as the project evolves.
