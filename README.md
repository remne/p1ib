# P1IB - P1 Interface Bridge
P1IB (pronounced p-l-i-b) is a software (and hardware) designed to read and parse advanced power meter (AMS) telegrams from the P1 
interface port (RJ12) and to send the result to a consumer service, for instance Home Assistant.

## Features
- Web UI configuration.
- Dashboard in web ui with realtime updated graphs for the majority of measurement points from the power meter.
- Supports both protocols that the Swedish meters use at this moment:
  - DLMS/COSEM AXDR/HDLC Mode E (Aidon).
  - DLMS/COSEM ASCII Mode D (The other ones :).
- MQTT support.
- Automatic sensor registration for Home Assistant (MQTT Auto Discovery).
- Supports OTA firmware update via web ui (official builds fetched from this github repo).
- Webservice with JSON response of meter data.
- Logging/debug through UDP to a remote computer and/or USB serial.

## Hardware 
The p1ib hardware comes with an RJ12 connector for connecting to the P1 HAN port of the power meter. It also includes an USB port.
The USB port does not need to be connected when plugged in with the RJ12 P1 connection of the power meter. The USB port is only for debugging (and possible changing firmware) purposes.

Communication with the p1ib are done through Wi-Fi.

![AMS and p1ib](images/meter.jpg?raw=true "AMS and p1ib")
![Hardware](images/hw_rev_d.jpg?raw=true "Hardware")

## Supported smart power meters
Verified to work on the following meters:
- Aidon 6534 (Tekniska Verken)
- Landis-Gyr E360
- Sagemcom S211

Will probably work on all Mode D based AMS.

Does not work on:
- ISKRA AM550 (E.on) - E.on cannot activate the P1 port on this meter.


Meters that have (for me) unknown protocol standard but have the P1/HAN RJ12 hardware interface, thus p1ib is not tested nor verified on.
- Ningbo Sanxing S34U18 (Vattenfall, https://we.vattenfalleldistribution.se/globalassets/matarbyte/vattenfall-eldistribution-oversikt-elmatare-vers.-1.0.pdf )
- Itron A100/A300 (Borås elnät, https://boraselnat.se/elnat/elmatarbyte-2020-2021/sa-har-fungerar-din-nya-elmatare/)

## First time usage

1. Connect your p1ib with the RJ12 cable into the P1 port of your AMS. A blue LED light will pulse a couple of times to indicate that it is booting. If no blue LED is blinking, then your HAN/P1 port is not activated. See "Powermeter prerequisite" for instructions. 
There is no need to connect a USB cable to the p1ib. It is powered via the P1/HAN interface.

2. P1ib enters AP mode (named "p1ib") when no SSID is configured, or connection cannot be established to the configured SSID.

Connect to Wi-Fi access point named "p1ib" without a password with your preferred device (phone or laptop for instance). You might need to disable "Mobile data" on your phone, otherwise it will try to connect via your cellular network provider.

3. When in AP-mode, IP 192.168.1.1 is set on the p1ib. Go to http://192.168.1.1/ or http://p1ib.local/ with the Chrome webbrowser to enter the configuration user interface.

4. Press the menu icon in top left corner, and enter the 'Settings' menu. Here it is possible to scan for your home Wi-Fi accesspoint (SSID), set an SSID password and enable other features.

5. Once you have entered your preferred settings, press the "Save & Restart"-button. 

6. Now you need to change back to your home Wi-Fi on your mobile phone/laptop. If you are using a device capable of mDNS (all computers more or less, probably not mobile devices) go to url http://p1ib.local/. If you are using a mobile device, you probably need to check in your home router for the IP the p1ib was assigned by your dhcp server, ie go to http://some-ip-number/

7. When entering http://p1ib.local/ (or the IP number) in the webbrowser url you will once again see the dashboard. If you selected correct power meter option in the settings page you will see the graphs beeing updated with your current power consumption.

8. At this point it is recommended press the menu icon once again. If the "firmware" menu option have an *red badge* on it with an '!' on it, it means that there is a new firmware available. It is recommended to always update to the latest recommended firmware in the firmware-page.


Note. Only chrome web browser is supported at this moment due to certain javascript dependencies.


![Dashboard](images/dashboard.png?raw=true "Dashboard")

![Menu](images/menu.png?raw=true "Menu")

## Powermeter prerequisite

To be able to get any information out from the P1 HAN interface on your powermeter, the P1 port needs to be activated.

For Eon, to to url https://www.eon.se/kundservice#humany-kundservice-privat=/g25505-hur-aktiverar-jag-min-elmaetares-han-port

For Tekniska Verken, go to url https://www.tekniskaverken.se/privat/elnat/matning-av-din-elanvandning/din-elmatare/#HAN

For Ellevio, see "Lokalt kundgränssnitt". at url https://www.ellevio.se/kundservice-kontakta-oss/elmatarbyte/matarbyte-mig/

## Firmware update

When a new firmware is available, a red badge will be visible in the Firmware menu.
The latest stable firmware is marked with the "recommended" text. 
To update the firmware, click on the firmware-download icon for the firmware that you want to update to.

![Firmware badge](images/firmware_avail.png?raw=true "Firmware badge")

![Firmware update](images/firmware_update.gif?raw=true "Firmware update")

## Home Assistant
An MQTT broker is needed to communicate with Home Assistant. Enable the MQTT client in the *settings* menu. Once activated and connected, the plib will register a sensor in HA for each measurement point.

Make sure that the *MQTT State* shows **connected** in the dashboard.

The p1ib registers the sensors once in Home Assistant at each startup of the p1ib.

![HA Device view](images/ha_devices_view.jpg?raw=true "HA Device view")


## Examples of automations in Home Assistant:

todo: add examples

## Plastic case
You can find a 3d model (stl) under the "case-model"-directory, which can be 3dprinted.

![Case](images/case1.jpg?raw=true)
![Case](images/case2.jpg?raw=true)
![Case](images/case_3dprinting.jpg?raw=true)
![Case](images/ledthingy.jpg?raw=true)

## FAQ / Trouble shooting
Q: The LED light pulses with red color, what does it mean?

A: It means p1ib is in AP mode, and needs to be configured. Connect to the Wi-Fi access point named "p1ib" and browse to http://192.168.1.1. You might need to disable "Mobile data" on your phone to be able to access it.


Q: What does the intermitten blue pulse LED light mean?

A: That a power meter messages was correctly parsed and verified (crc check was ok).


Q: What does intermitten red pulses mean? 

A: That p1ib received an incomplete message from your powermeter and/or crc check did not pass.


Q: I cannot access p1ib by http://p1ib.local/ after I have selected an access point in the settings menu and entered a password

A1: If p1ib is still available in the devices list of access points, then p1ib could not connect to your AP SSID. Connect to it and double check that you entered the correct password. You can press the 'eye' icon to make the password visible in clear text.

A2: Your client might not support mDNS protocol, which must be activated to be able to resolve p1ib.local to an IP address. If this is the case, use the IP address given by your router instead.


Q: I have Home Assistant and I want all data as sensors.

A: Its easy! Just enable "MQTT" option, enter IP and port and possible username / password to your mqtt broker. 
   P1ib automatically register a sensor for each measurement point from your AMS into HA.


Q: I have an Homey or other home automation system I want to use together with my p1ib.

A: MQTT is the prefered protocol in p1ib. Messages will be sent out periodically if connected to an power meter. Easiest way is to 
   "sniff" the messages with an local mqtt client (for example mosquitto_sub) to find out all topics available. Subscribe the topic '#' with mosquitto_sub to see all messages and topics.
   There is also a webservice providing the meter data. It can be found att http://p1ib.local/meterData


Q: I cannot see any graphs in the dashboard while in AP mode.

A: The graphs rely on the 'chartjs' library, which is not included in the firmware (due to the library size). Once connected to your Wi-Fi access point (and the internet), the library will be downloaded by your webbrowser and the graphs will work.
