# 🏡 Gabriel's homeOS
My smart home built on a [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) (4GB) running [Home Assistant](https://www.home-assistant.io/) OS, with a connected [ConBee II](https://www.phoscon.de/en/conbee2).

## Overview
🚨 Home Security - 📱 Mobile control - 💡 Smart adaptive lighting - 👋 - Motion & occupancy sensing - 👁 Smart curtains & blinds - ⚡ Energy & solar monitoring - 🌡 Smart heating & cooling - 🔊 Multi-room audio - 🎛 Local control
### Foundation
- 🚨 Home is secured using a combination of Aqara contact sensors, Sonos speakers and HomeKit Secure Video (HSV)
- 📱 In general, devices are controlled in the Apple Home app through HomeKit, and managed through Lovelace
- 💡 All lights adapt throughout the day and are color or warm/white Zigbee bulbs by IKEA or Signify
- 👋 Every room contains Hue, Aqara or IKEA motion sensor(s) for occupancy and controlling lights
- 👁 Window covers are automated using SwitchBots and IKEA roller blinds
- ⚡ Energy and solar are being monitored by an Inverter (SEMS) and a Homewizard Energy P1 meter
- 🌡 Heating is controlled by Aqara and Sonoff temperature sensors in combination with Tuya devices and Sonoff relays behind radiators
- 🔊 Multi-room audio is realized using Sonos (& Sonos+IKEA) speakers
- 🎛 Every room (save a few exceptions) contain physical Hue or IKEA Zigbee switches to manually control the lights

### Miscellaneous
- TV (Android) and streaming box (Apple TV) can be controlled through Lovelace or HomeKit
- Game consoles can be turned on/off through Lovelace or HomeKit
- Washer state is monitored through SmartThings in Lovelace and notified in HomeKit through a lock entity
- Air purification is done using a Smartmi purifier controlled through Lovelace (workaround) or HomeKit
- HP Printer & ink state is monitored in Lovelace

### Management
- Home Assistant is accessible through [Nabu Casa Cloud](https://www.nabucasa.com/)
- The Zigbee network runs on [deCONZ](https://phoscon.de/en/conbee2/software)/[ConBee II](https://www.phoscon.de/en/conbee2) through a USB2 extension
- The OS runs on a SATA/USB3 connected [Kingston A400 SSD](https://www.kingston.com/en/ssd/a400-solid-state-drive)
- Home Assistant's database runs on [MariaDB](https://mariadb.org/)
- Daily backups are created and stored on a [Synology DS718+](https://www.synology.com/support/download/DS718+?version=7.0#system) NAS
- Home Assistant mobile apps notifies me of new updates for the OS, deCONZ, NAS, Backups and HACS
- Git setup using the community guide [Sharing your configuration on Github](https://community.home-assistant.io/t/sharing-your-configuration-on-github/195144) and [Atlassian Git Cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)

## Home State & Modifiers
Globally, Home Assistant follows a **State** path during a day, which controls how certain automations and scripts run:

🌅 `Ochtend` (morning) -> ☀ `Overdag` (day) - 🌜 `Avond` (evening) - 🌑 `Nacht` (night)

These **Home States** in turn are adjusted based on which **Home State Modifier** is active during that time. The following modifiers paths are most common:

- `Home` ensures 🚪 security is off, 💡 lights are adapted and 🌡 heating is on
- `Home` -> `Sleeping` -> `Home` ensures 🚨 security is on, 🕯 lights are dimmed, 🌡 heating is adjusted and ⚙ bedroom automations run
- `Home` -> `Away` -> `Home` ensures 🚨 security is on, 🚫 lights & devices are off, ❄ heating is lowered
- `Home` -> `Away` -> `On vacation` -> `Home` ensures ⚙ Home State automations will run as if someone's home

## Modes
Additionally, there are a couple of **Modes** which can be manually turned on or off depending on the situation:
- **Cinema Mode** ensures the ideal movie watching experience
- **Party Mode** ensures no automations are run that interfere with guests
- **Privacy Mode** ensures downstairs is secured against prying eyes
