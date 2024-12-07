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

1. **LM35 Temperature Sensor**  
   *Product Link*: [LM35 Temperature Sensor](product_link_here)

2. **LDR Light Sensor**  
   *Product Link*: [LDR Light Sensor](product_link_here)

3. **Capacitive Soil Moisture Sensor**  
   *Product Link*: [Capacitive Soil Moisture Sensor](product_link_here)

4. **1.8-inch Display**  
   *Product Link*: [1.8-inch Display](product_link_here)

> **Note**: You can purchase these components from any retailer at a cheaper price. The links provided are for reference.

---

### **Circuit Diagram**

A clear and simple circuit diagram of the **PlantPal** setup, showing how each sensor and component is connected.

 <img src="Circuit%20Diagram/WhatsApp%20Image%202024-12-03%20at%2020.22.39_c2fcb2b1.jpg" width="300" />

---

### **Pin Table**

A reference pin table indicating the correct GPIO pins for each sensor and component on the **Raspberry Pi Pico**.

<img src="Circuit%20Diagram/WhatsApp%20Image%202024-12-03%20at%2020.49.55_a2af6984.jpg" width="300" />

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
