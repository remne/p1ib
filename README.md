# P1IB - P1 Interface Bridge
P1IB (pronounced p-l-i-b) is a software (and hardware) designed to read and parse advanced power meter (AMS) telegrams from the P1 
interface port (RJ12) and to send the result to a consumer service, for instance Home Assistant.

## Supported smart power meters
Currently the following meters are (probably) supported:
- Aidon (Tekniska Verken)
- Landis Gyr (E.on, E360)
- Sagemcom (S211, Ellevio and E.on)

Verified to work on the following meters:
- Aidon

## Features
- Web UI configuration.
- Dashboard in web ui with realtime updated graphs for the majority of measurement points from the power meter.
- Supports both protocols that the Swedish meters use at this moment:
  - COSEM/DLMS AXDR/HDLC Mode E (Aidon).
  - COSEM/DLMS ASCII Mode D (The other ones :).
- MQTT support.
- Automatic sensor registration for Home Assistant (MQTT Auto Discovery).
- Supports OTA firmware update via web ui (official builds fetched from this github repo).
- Webservice with JSON response of meter data.
- Logging/debug through UDP to a remote computer and/or USB serial.


## Hardware 
The p1ib hardware comes with an RJ12 connector for connecting to the P1 HAN port of the power meter. It also includes an USB port.
The USB port does not need to be connected when plugged in with the RJ12 P1 connection of the power meter. The USB port is only for debugging (and possible changing firmware) purposes.

Communication with the p1ib are done through Wi-Fi.

![Hardware](images/hw.jpg?raw=true "Hardware")

### Plastic case
You can find a 3d model (stl) under the "case-model"-directory, which can be 3dprinted.

![Case](images/case_rend.png?raw=true)
![Case](images/case1.jpg?raw=true)
![Case](images/case2.jpg?raw=true)
![Case](images/case_3dprinting.jpg?raw=true)
![Case](images/ledthingy.jpg?raw=true)


## First time usage
P1ib enters AP mode (named "p1ib") when no SSID is configured, or connection cannot be established to the configured SSID.

1. Connect to it without a password with your preferred device (phone or laptop for instance).

2. When in AP-mode, IP 192.168.1.1 is set on the p1ib. Go to http://192.168.1.1/ or http://p1ib.local/ with the Chrome webbrowser to enter the configuration user interface.

3. Press the menu icon, and enter the 'Settings' menu. Here it is possible to scan for your Wi-Fi accesspoint (SSID), set a SSID password, and enable other features.

4. Once you have entered your preferred settings, press the "Save & Restart"-button. Now you need to change url to http://p1ib.local/ . 
Remember that you also need to change AP on your device to the one selected in the p1ib settings.

5. When entered http://p1ib.local/ in the webbrowser url, and you will once again see the dashboard. If you selected correct power meter option in the settings page you will see the graphs beeing updated with your current power consumption.

6. At this point it is recommended press the menu icon once again. If the "firmware" menu option have an red badge on it with an '!' on it, it means that there is a new firmware update available. 
It is recommended to always update to the latest recommended firmware in the firmware-page.


Note. Only chrome web browser is supported at this moment due to certain javascript dependencies.


![Dashboard](images/dashboard.png?raw=true "Dashboard")

![Menu](images/menu.png?raw=true "Menu")


## Powermeter prerequisite

To be able to get any information out from the P1 HAN interface on your powermeter, the P1 port needs to be activated.

For Eon, to to url https://www.eon.se/kundservice#humany-kundservice-privat=/g25505-hur-aktiverar-jag-min-elmaetares-han-port

For Tekniska Verken, go to url https://www.tekniskaverken.se/privat/elnat/matning-av-din-elanvandning/din-elmatare/#HAN


## Firmware update

When a new firmware is available, a red badge will be visible in the Firmware menu.
The latest stable firmware is marked with the "recommended" text. 
To update the firmware, click on the firmware-download icon for the firmware that you want to update to.

![Firmware badge](images/firmware_avail.png?raw=true "Firmware badge")

![Firmware update](images/firmware_update.gif?raw=true "Firmware update")


## Examples of automations in Home Assistant:

todo: add examples

## FAQ / Trouble shooting
Q: The LED light pulses with red color, what does it mean?

A: It means p1ib is in AP mode, and needs to be configured. Connect to the Wi-Fi access point named "p1ib" and browse to http://192.168.1.1. You might need to disable "Mobile data" on your phone to be able to access it.


Q: What does the blue pulse LED light mean?

A: That a power meter messages was correctly parsed and verified (crc check was ok).


Q: What does intermitten red pulses mean? 

A: That p1ib received an incomplete message and/or crc check did not pass.


Q: I cannot access p1ib by http://p1ib.local/ after I have selected an access point in the settings menu and entered a password

A1: If p1ib is still available in the devices list of access points, then p1ib could not connect to your AP SSID. Connect to it and double check that you entered the correct password. You can press the 'eye' icon to make the password visible in clear text.

A2: Your client might not support mDNS protocol, which must be activated to be able to resolve p1ib.local to an IP address. If this is the case, use the IP address given by your router instead.


Q: I have Home Assistant and I want all data as sensors.

A: Its easy! Just enable "MQTT" option, enter IP and port and possible username / password to your mqtt broker. 
   P1ib automatically register a sensor for each measurement point from your AMS into HA. In short, there will be sensor entities in HA automatically when the mqtt feature is enabled.


Q: I have an Homey or other home automation system I want to use together with my p1ib.

A: MQTT is the prefered protocol in p1ib. Messages will be sent out periodically if connected to an power meter. Easiest way is to 
   "sniff" the messages with an local mqtt client (for example mosquitto_sub) to find out all topics available. Subscribe the topic '#' with mosquitto_sub to see all messages and topics.


Q: I cannot see any graphs in the dashboard while in AP mode.

A: The graphs rely on the 'chartjs' library, which is not included in the firmware (due to the library size). Once connected to your Wi-Fi access point (and the internet), the library will be downloaded by your webbrowser and the graphs will work.
