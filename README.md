# 🏡 Gabriel's homeOS
My smart home built on a Raspberry Pi 4 Model B (4GB) running Home Assistant OS, with a connected ConBee II.

## Overview
🛡 Home Security - 📱 Mobile control - 💡 Smart adaptive lighting - 👋 - Motion & occupancy sensing - ⚡ Energy & solar monitoring - 🌡 Smart heating & cooling - 🔊 Multi-room audio - 🎛 Local control
### Foundation
- 🛡 Home is secured using a combination of Aqara contact sensors, Sonos speakers and HomeKit Secure Video (HSV)
- 📱 In general, devices are controlled in the Apple Home app through HomeKit, and managed through Lovelace
- 💡 All lights adapt throughout the day and are color or warm/white Zigbee bulbs by IKEA or Signify
- 👋 Every room contains Hue, Aqara or IKEA motion sensor(s) for occupancy and controlling lights
- ⚡ Energy and solar are being monitored by an Inverter (SEMS) and a Homewizard Energy P1 meter
- 🌡 Heating is controlled by Aqara and Sonoff temperature sensors in combination with Tuya devices and Sonoff relays behind radiators
- 🔊 Multi-room audio is realized using Sonos (& Sonos+IKEA) speakers
- 🎛 Every room (save a few exceptions) contain physical Hue or IKEA Zigbee switches to manually control the lights

### Miscellaneous
- TV (Android) and streaming box (Apple TV) can be controlled through Lovelace or HomeKit
- Air purification is done using a Smartmi purifier controlled through Lovelace (workaround) or HomeKit
- Windows are covered and automated by SwitchBots and IKEA smart shades and controlled through Lovelace or HomeKit
- Game consoles can be turned on/off through Lovelace or HomeKit
- HP Printer & ink state is monitored in Lovelace
- Washer state is monitored through SmartThings in Lovelace and notified in HomeKit

### Management
- Home Assistant is accessible through Nabu Casa Cloud
- The Zigbee network runs on deCONZ/Conbee II through a USB2 extension
- The OS runs on a SATA/USB3 connected Kingston A400 SSD
- Home Assistant's database runs on MariaDB
- Daily backups are created and stored on a Synology NAS
- Home Assistant mobile apps notifies me of new updates for the OS, deCONZ, NAS, Backups and HACS

## Home State & Modifiers
Globally, Home Assistant follows a **State** path during the day, which control how certain things automate:

⛅ `Ochtend` (morning) -> ☀ `Overdag` (daytime) - 🌜 `Avond` (evening) - 🌑 `Nacht` (night)

These **Home States** in turn are adjusted based on which **Home State Modifier** is active during that time. The following modifiers paths are most common:

- `Home` ensures 🚪 security is OFF, 💡 lights are adaptive and 🌡 heating is on
- `Home` -> `Sleeping` -> `Home` ensures 🛡 security is ON, 🕯 lights are dimmed, 🌡 heating is adjusted and ⚙ bedroom automations run
- `Home` -> `Away` -> `Home` ensures 🛡 security is ON, 🚫 lights & devices are off, ❄ heating is lowered
- `Home` -> `Away` -> `On vacation` -> `Home` ensures ⚙ Home State automations will run as if someone's home

## Modes
Additionally, there are a couple of Modes which can be manually turned on depending on the situation:
- **Cinema Mode** ensures the ideal movie watching experience
- **Party Mode** ensures no automations are run that interfere with guests
- **Privacy Mode** ensures downstairs is secured against prying eyes
