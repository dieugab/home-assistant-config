# 🏡 Gabriel's homeOS
My smart home built on a [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) (4GB) running [Home Assistant](https://www.home-assistant.io/) OS, with a connected [ConBee II](https://www.phoscon.de/en/conbee2).

## Overview
🚨 Home Security | 📱 Mobile control | 💡 Smart adaptive lighting | 👋 Motion & occupancy sensing | 👁 Smart curtains & blinds | ⚡ Energy & solar monitoring | 🌡 Smart heating & cooling | 🔊 Multi-room audio | 🎛 Local control

![Hero-combined](https://user-images.githubusercontent.com/61377476/138591773-0800bf9a-436e-49e3-895f-d651278713fd.png)

### Foundation
- 🚨 Home is secured using a combination of Aqara contact sensors, Sonos speakers and HomeKit Secure Video
- 📱 Most everything is controlled in the Apple Home app through HomeKit, and managed through Home Assistant Lovelace
- 💡 All lights adapt throughout the day and are color or warm/white Zigbee bulbs by IKEA or Signify
- 👋 Every room contains Hue, Aqara or IKEA motion sensor(s) for occupancy and controlling lights
- 👁 Window covers are automated using SwitchBots and IKEA roller blinds
- ⚡ Energy and solar are monitored by a Homewizard Energy P1 meter and Solar Inverter (SEMS) 
- 🌡 Heating is controlled by Aqara and Sonoff temperature sensors in combination with Tuya devices and Sonoff relays behind electric radiators
- 🔊 Multi-room audio is realized using Sonos (& Sonos+IKEA) speakers
- 🎛 Every room (save a few exceptions) contain physical Hue or IKEA Zigbee switches to manually control the lights

### Miscellaneous
- TV (Android) and streaming box (Apple TV) can be controlled through Lovelace or HomeKit
- Game consoles can be turned on/off through Lovelace or HomeKit
- Washer state is monitored through SmartThings in Lovelace and notified in HomeKit through a lock entity
- Air purification is done using a Smartmi purifier controlled through Lovelace (via helpers) or HomeKit (direct)
- HP Printer & ink state is monitored in Lovelace

### Technical
- Home Assistant is accessible away from home through [Nabu Casa Cloud](https://www.nabucasa.com/) and a HomeKit Hub
- The Zigbee network runs on [deCONZ](https://phoscon.de/en/conbee2/software)/[ConBee II](https://www.phoscon.de/en/conbee2) through a USB2 extension
- The OS runs on a SATA/USB3 connected [Kingston A400 SSD](https://www.kingston.com/en/ssd/a400-solid-state-drive)
- Lovelace uses my custom [homeOS theme](https://github.com/gvssr/home-assistant-config/tree/main/themes/homeOS_theme), based on work by [JuanMTech](https://github.com/JuanMTech)
- Home Assistant's database runs on [MariaDB](https://mariadb.org/)
- Daily backups are created and stored through SMB on a [Synology DS718+](https://www.synology.com/support/download/DS718+?version=7.0#system)
- Home Assistant mobile app notifies me about new updates for Core, deCONZ, NAS DSM, Backups and Custom Integrations
- Git setup using the community guide [Sharing your configuration on Github](https://community.home-assistant.io/t/sharing-your-configuration-on-github/195144) and [Atlassian Git Cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)

## Home State & Modifiers
Globally, my Home Assistant config follows a **State** path during the day, which controls how certain automations and scripts run: ⛅️ `Morning` ⇢ ☀️ `Day` ⇢ 🌜 `Evening` ⇢ 🌑 `Night`

Each **Home State** is controlled by a switch and corresponding Input Select, which run scripts in the background. Roughly, the actions are as following:

- ⛅️ `Morning` turns off outside lights, and opens all the blinds except the bedroom
- ☀️ `Day` ensures the `Home` Modifier is set, opens all curtains and runs certain bedroom automations
- 🌜 `Evening` turns on outside and living room lights, and closes all curtains
- 🌑 `Night` ensures the `Sleeping` Modifier is set and turns off lights & devices

These **Home States** in turn are adjusted based on which **Home State Modifier** is active during that time. The following modifiers are available:

- 🏠 `Home` ⇢ 💤 `Sleeping` turns security on, dims lights, adjusts heating and runs certain bedroom automations
- 🏠 `Home` ⇢ 📍 `Away` turns security on, turns off lights & devices and lowers heating
- 📍 `Away` ⇢ ⛱️ `On vacation` ensures Home State automations will run as if someone's home
- 💤 `Sleeping` | 📍 `Away` | ⛱️ `On vacation` ⇢ 🏠 `Home` turns security off, adapts lights and turns on heating

## Modes
Additionally, there are a couple of **Modes** which can be manually turned on depending on the situation. Turning them off runs the corresponding script actions of the currect **Home State** to ensure a smooth transition back to the status quo.
- 🍿 ``Cinema Mode`` ensures the ideal movie watching experience, by turning on the tv, closing the curtains and turning off or dimming certain lights
- 🎉 ``Party Mode`` ensures no automations are run that interfere with guests, like curtains opening, alarms triggering or lights dimming
- 👀 ``Privacy Mode`` ensures the living room is secured against prying eyes from outside, by closing the curtains, dimming lights, disabling camera's and playing music

