- [P1IB - P1 Interface Bridge](#p1ib---p1-interface-bridge)
  - [Features](#features)
  - [Hardware](#hardware)
  - [Supported smart power meters](#supported-smart-power-meters)
    - [Note on Aidon meters](#note-on-aidon-meters)
- [Powermeter prerequisite](#powermeter-prerequisite)
- [First time usage](#first-time-usage)
- [Menues](#menues)
  - [Dashboard](#dashboard)
  - [Settings](#settings)
  - [Advanced Settings](#advanced-settings)
  - [Reduced Data Mode](#reduced-data-mode)
- [Firmware update](#firmware-update)
- [Home Assistant](#home-assistant)
  - [Configure MQTT in P1IB](#configure-mqtt-in-p1ib)
  - [Setup the Energy board with p1ib sensors](#setup-the-energy-board-with-p1ib-sensors)
  - [Examples of cards in Home Assistant](#examples-of-cards-in-home-assistant)
    - [Apex charts with energy consumption and electricity spot price from nordpool](#apex-charts-with-energy-consumption-and-electricity-spot-price-from-nordpool)
    - [Example: Current gauges](#example-current-gauges)
  - [Examples of automations in Home Assistant](#examples-of-automations-in-home-assistant)
    - [Example: Disable power switch when fuse amperage is above a given threshold](#example-disable-power-switch-when-fuse-amperage-is-above-a-given-threshold)
- [Homey App](#homey-app)
- [FAQ / Trouble shooting](#faq--trouble-shooting)


# P1IB - P1 Interface Bridge
P1IB (pronounced p-l-i-b) is a software (and hardware) designed to read and parse advanced power meter (AMS) telegrams from the P1
interface port (RJ12) and to send the result to a consumer service, for instance Home Assistant.

![AMS and p1ib](images/p1ib2.jpg?raw=true "AMS and p1ib")
![AMS and p1ib](images/meter.jpg?raw=true "AMS and p1ib")

## Features
- Fully configurable via web UI.
  - WiFi access point
  - DHCP/static ip
  - MQTT settings
  - And lots more...
- Dashboard in web UI with realtime updated graphs for the majority of measurement points from the power meter.
- Supports both protocols that the Swedish meters use at this moment:
  - DLMS/COSEM AXDR/HDLC Mode E (Aidon).
  - DLMS/COSEM ASCII Mode D (The other ones).
- MQTT support.
- Automatic sensor registration for Home Assistant (MQTT Auto Discovery).
- Supports OTA firmware update via web ui (official builds fetched from this github repo).
- Webservice with JSON response of meter data.
- Reduced data mode
- Logging/debug through UDP to a remote computer and/or USB serial.
- P1IB does not require any internet connection (with the exception for over-the-air firmware updates).

## Hardware
The p1ib hardware comes with an RJ12 connector for connecting to the P1 HAN port of the power meter. It also includes an USB port.
The USB port does not need to be connected when plugged in with the RJ12 P1 connection of the power meter. The USB port is only for debugging (and possible changing firmware) purposes.
P1IB is normally powered by the P1 port.

Communication with the p1ib are done through Wi-Fi.

The hardware can normally be bought at [https://remne.tech](https://remne.tech)

![Hardware](images/hw_rev_d.jpg?raw=true "Hardware")
![Case](images/case2.jpg?raw=true)

## Supported smart power meters
Verified to work on the following meters:
- Aidon 6000 & 7000 series (6534 is the most common one, both old and upgraded versions)
- Landis-Gyr E360
- Sagemcom T211/S211
- Sanxing S34U18
- Star STZ351
- Kamstrup OMNIA
- Itron A100/A300
- Kaifa MA304

Will probably work on all Mode D based AMS.

Does not work on:
- ISKRA AM550 (E.on) - E.on cannot activate the P1 port on this meter.
- Kamstrup OMNIPOWER - p1ib can be modified to work with this meter, however, not recommended. OMNIPOWERs P1 port is not compliant with the P1-standard.

### Note on Aidon meters
Aidon meters comes in two flavors, where recently updated meters use Mode-D and older ones Mode-E protocol. If you dont get any data in the dashboard, change power meter mode in the settings menu.

![Mode](images/settings_power_meter_modes.jpg?raw=true "Mode")

Note. In latest firmware the power meter mode is automatically detected.

# Powermeter prerequisite

To be able to get any information out from the P1 HAN interface on your powermeter, the P1 port needs to be activated.

Visit your electricity grid owners homepage for information on how to activate the P1-port on your powermeter.

# First time usage

1. Connect your p1ib with the RJ12 cable into the P1 port of your AMS. A blue LED light will pulse a couple of times to indicate that it is booting. If no blue LED is blinking, then your HAN/P1 port is not activated. See "Powermeter prerequisite" for instructions.
There is no need to connect a USB cable to the p1ib. It is powered via the P1/HAN interface.

2. P1ib enters AP mode (named "p1ib") when no SSID is configured, or connection cannot be established to the configured SSID.

Connect to Wi-Fi access point named "p1ib" without a password with your preferred device (phone or laptop for instance). You might need to disable "Mobile data" on your phone, otherwise it will try to connect via your cellular network provider.

3. When in AP-mode, IP 192.168.1.1 is set on the p1ib. Go to http://192.168.1.1/ or http://p1ib.local/ with the Chrome webbrowser to enter the configuration user interface.

4. Press the menu icon in top left corner, and enter the 'Settings' menu. Here it is possible to scan for your home Wi-Fi accesspoint (SSID), set an SSID password and enable other features.

![Menu](images/menu.png?raw=true "Menu")


5. Once you have entered your preferred settings, press the "Save & Restart"-button.

6. Now you need to change back to your home Wi-Fi on your mobile phone/laptop. If you are using a device capable of mDNS (all computers more or less, probably not mobile devices) go to url http://p1ib.local/. If you are using a mobile device, you probably need to check in your home router for the IP the p1ib was assigned by your dhcp server, ie go to http://some-ip-number/

7. When entering http://p1ib.local/ (or the IP number) in the webbrowser url you will once again see the dashboard. If you selected correct power meter option in the settings page you will see the graphs beeing updated with your current power consumption.

8. At this point it is recommended press the menu icon once again. If the "firmware" menu option have an *red badge* with an '!' on it, it means that there is a new firmware available. It is recommended to always update to the latest recommended firmware in the firmware-page.


Note. Only the Chrome web browser is supported at this moment due to certain javascript dependencies.




# Menues

## Dashboard
The dashboard provides an overview of the current state of the p1ib, and also graphs for some of the measurement points available.

![Dashboard](images/dashboard.png?raw=true "Dashboard")
## Settings

![Settings](images/settings.png?raw=true "Settings")
## Advanced Settings

![Advanced Settings](images/settings_adv.png?raw=true "Advanced Settings")

## Reduced Data Mode

The reduced data mode can be activated if you want to save bandwidth. This is useful for example for remote power monitoring in your summer house or similar where there might be a bandwidth cost from your internet service provider.

Each measurement point can be enabled or disabled, and there is also a hysteresis on each obis code to further limit data bandwidth.

![Reduced Data Mode](images/reduced.png?raw=true "Reduced Data Mode")


# Firmware update

When a new firmware is available, a red badge will be visible in the Firmware menu.
The latest stable firmware is marked with the "recommended" text.
To update the firmware, click on the firmware-download icon for the firmware that you want to update to.

![Firmware badge](images/firmware_avail.png?raw=true "Firmware badge")

![Firmware update](images/firmware_update.gif?raw=true "Firmware update")

# Home Assistant
An MQTT broker is needed to communicate with Home Assistant. The MQTT broker must be installed separately, and is normally not provided by default in an Home Assistant installation.

Please read the Home Assistant MQTT documentation at https://www.home-assistant.io/integrations/mqtt/ if you dont have an MQTT broker installed.

## Configure MQTT in P1IB
Enable the MQTT client in the *settings* menu. Enter your IP/hostname and port number for your mqtt broker. If authentication is used, username and password must be provided. Once activated and connected, the plib will register a sensor in HA for each measurement point.

Make sure that the *MQTT State* shows **connected** in the dashboard.

![MQTT state](images/mqtt_connected.jpg?raw=true "MQTT state")

<br>
The p1ib registers the sensors in Home Assistant at each startup of the p1ib.

![HA Device view](images/ha_devices_view.jpg?raw=true "HA Device view")
![HA Energy Dashboard](images/ha_energy.jpg?raw=true "HA Energy Dashboard")


## Setup the Energy board with p1ib sensors

Home Assistant needs som manual configuration to enable it to collect energy statistics over time, and to make the "energy"-dashboard show any p1ib based information.

1. In Home Assistant press "Settings -> Dashboards -> Energy"
2. Add sensors for consumption and return to grid:

  ![Energy import export](images/ha_energy_import_export_sensors.jpg?raw=true)

1. It will take a couple of hours for Home Assistant to collect data. If it is working as expected, your should finally, after some time, have an dashboard with some nice looking graphs:

![](images/ha_energy_dashboard.jpg?raw=true)

## Examples of cards in Home Assistant

### Apex charts with energy consumption and electricity spot price from nordpool
![Energy graph](images/energy_apex_charts.jpg?raw=true)

1. Install apex charts card [https://github.com/RomRider/apexcharts-card](https://github.com/RomRider/apexcharts-card) and nordpool integration [https://github.com/custom-components/nordpool](https://github.com/custom-components/nordpool)


2. Create a per hour energy (kWh) sensor based on the p1ib energy import sensor.
    - Go to home assistant
    - Click Settings -> Devices & Services -> Helpers
    - Click "+ CREATE HELPER"-button
    - Press "Utility Meter"
    - Name the sensor "energy_consumption_kwh_hour"
    - Select sensor "sensor.p1ib_active_energy_import_q1_q4
    - Meter reset cycle: hourly
    - Press "Submit"

3. Go to your dashboard of choice in home assistant, press the "..." icon and "Edit dashboard".

   ![Edit dashboard](images/ha_edit_dashboard.jpg?raw=true)

4. Press the button "+ ADD CARD". Scroll to the bottom and select under Manual, "Need to add a custom card or just want to manually write the YAML?"



Paste the following code into the editor window:
```
type: custom:apexcharts-card
graph_span: 60h
experimental:
  color_threshold: true
header:
  title: Energy usage and cost estimation (nordpool)
  show: true
apex_config:
  yaxis:
    min: 0
hours_12: false
span:
  start: hour
  offset: '-22h'
now:
  show: true
  label: Now
series:
  - entity: sensor.nordpool_kwh_se3_sek_3_10_025
    type: column
    data_generator: |
      return (entity.attributes.raw_today.map((start, index) => {
        return [new Date(start["start"]).getTime(), entity.attributes.raw_today[index]["value"]];
      })).concat(entity.attributes.raw_tomorrow.map((start, index) => {
        return [new Date(start["start"]).getTime(), entity.attributes.raw_tomorrow[index]["value"]];
      }));
    color_threshold:
      - value: 0
        color: green
      - value: 1
        color: orange
      - value: 2
        color: red
      - value: 3
        color: darkred
      - value: 4
        color: black
  - entity: sensor.energy_consumption_kwh_hour
    type: column
    group_by:
      func: max
      duration: 1h
    color: blue
    show:
      header_color_threshold: true
      extremas: true

```

Change the "sensor.nordpool_kwh_se3_sek_3_10_025" to your nordpool sensor of choice in the code above. The sensor is named based on your geographical location.

5. Press "Save". Your done!

### Example: Current gauges

![Current meters](images/ha_current_gauges.jpg?raw=true)

1. Go to your dashboard of choice in home assistant, press the "..." icon and "Edit dashboard".

2. Press the button "+ ADD CARD". Scroll to the bottom and select under Manual, "Need to add a custom card or just want to manually write the YAML?"

3. Paste the following code into the text editor:

```
type: vertical-stack
cards:
  - type: gauge
    entity: sensor.p1ib_current_l1
    max: 25
    unit: A
    needle: true
    severity:
      green: 0
      yellow: 16
      red: 20
  - type: gauge
    entity: sensor.p1ib_current_l2
    max: 25
    unit: A
    severity:
      green: 0
      yellow: 16
      red: 20
    needle: true
  - type: gauge
    entity: sensor.p1ib_current_l3
    max: 25
    unit: A
    needle: true
    severity:
      green: 0
      yellow: 16
      red: 20
view_layout:
  position: sidebar
```

4. Adjust the "green:", "yellow:" and "red:" values based on your main fuse amperage and limits you want to have in the gauges.

5. Press "Save". Your done!

## Examples of automations in Home Assistant

The examples requires some knowledge about the automation system in Home Assistant.
[https://www.home-assistant.io/docs/automation](https://www.home-assistant.io/docs/automation)

### Example: Disable power switch when fuse amperage is above a given threshold

todo: add example

# Homey App

P1IB supports homey! A homey app is available at [https://homey.app/sv-se/app/nu.ahlner.p1ib/p1ib](https://homey.app/sv-se/app/nu.ahlner.p1ib/p1ib)

The app is developed by Erik Ahlner (whyz). Source code available at https://github.com/whyz/homey-p1ib.

![Homey1](images/homey1.png?raw=true)
![Homey2](images/homey2.png?raw=true)

# FAQ / Trouble shooting
Q: I have changed WiFi settings and set the p1ib to connect to my home WiFi accesspoint - but I cannot find p1ib on my local network.

A: There are several reasons and solutions:
1. You entered incorrect password for your accesspoint - in this case p1ib will return to AP-mode in a couple of seconds. Wait and watch out for the p1ib-ssid in your wifi scanning.
2. Your device does not support mDNS. You need to figure out what IP-address the p1ib have been assigned to. Go to your router/DHCP-servers client list to find out the IP.
3. Get help in the community facebook group named "P1IB / P1 Interface Bridge - support" (https://www.facebook.com/groups/385403882937131).
4. If 1 och 2 does not solve the problem, then the best way to understand the problem is to connect the p1ib to your PC via USB. Install the CH340 drivers if needed (http://www.wch-ic.com/downloads/CH341SER_EXE.html), linux users doesn't need any drivers). Connect to the usb-serial port with your favorite terminal program (putty for instance), baud rate 200000. The P1IB will log current state to the usb connection.
5. Flash new firmware onto the device via USB, which will reset all settings and force p1ib to AP-mode. https://remne.github.io/p1ib/webflash/
6. Send E-mail to hello@remne.tech.

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


Q: I have a different home automation system than HA or Homey I want to use together with my p1ib.

A: MQTT is the prefered protocol in p1ib. Messages will be sent out periodically if connected to an power meter. Easiest way is to
   "sniff" the messages with an local mqtt client (for example mosquitto_sub) to find out all topics available. Subscribe the topic '#' with mosquitto_sub to see all messages and topics.
   There is also a webservice providing the meter data. It can be found att http://p1ib.local/meterData


Q: I cannot see any graphs in the dashboard while in AP mode.

A: The graphs rely on the 'chartjs' library, which is not included in the firmware (due to the library size). Once connected to your Wi-Fi access point (and the internet), the library will be downloaded by your webbrowser and the graphs will work.
