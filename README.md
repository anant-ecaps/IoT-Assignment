# IoT-Assignment3
A cloud-based IoT system for collecting data from virtual sensors using MQTT protocol and ThingSpeak as the cloud-based backend for data storage and visualisation.
____________________________________________________________________________________________________________________________________________________________________________________

System Setup Steps:
1. Sensor Simulation: Developed a stand-alone Python program to mimic sensors producing periodic and random CO2 pressure, humidity, and temperature readings within predetermined ranges.
2. ThingSpeak Setup: Due to its ease of use and fit for IoT applications, selected ThingSpeak as the cloud-based backend using its MQTT functionality for data input and storage.
3. Configuration and Authentication: Configured MQTT channel, client, and device with necessary parameters, such as channel ID, API key, Client ID, username, and password for authentication with ThinkSpeak broker.
4. Data Monitoring and Analysis: Published data in the form of payloads to ThingSpeak channel using Paho MQTT library and MQTT Topic. Analysed the data and kept track of sensor readings ensuring successful data publication.

____________________________________________________________________________________________________________________________________________________________________________________
Console Readings:

<img width="587" alt="Console Output" src="https://github.com/anant-ecaps/IoT-Assignment/assets/61697380/41b5c7dc-2a29-49c7-9662-e887328415b9">

____________________________________________________________________________________________________________________________________________________________________________________

ThingSpeak Dashboard: After collecting hours of sensor data:

<img width="1097" alt="Graph" src="https://github.com/anant-ecaps/IoT-Assignment/assets/61697380/885bceae-51d6-46ca-a69b-30c5eb001e9d">


This system effectively collects data from virtual sensors and distributes it via the MQTT protocol to the cloud-based ThingSpeak backend. The system demonstrates the capability to monitor environmental parameters, and it may be further developed for practical implementation in a range of Internet of Things applications.
