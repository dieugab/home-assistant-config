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
- 📺 Android TV and Apple TV can be controlled through Lovelace or HomeKit
- 🎮 Game consoles can be controlled through Lovelace or HomeKit
- 🧺 Washer state is monitored using SmartThings in Lovelace and notified in HomeKit through a lock entity
- 💨 Air purification is done using a Smartmi purifier controlled through Lovelace (via helpers) or HomeKit (directly)
- 🖨️ HP Printer & ink state is monitored in Lovelace

## Technical
### Software
- [Home Assistant OS](https://www.home-assistant.io/installation/) is accessible away from home through [Nabu Casa Cloud](https://www.nabucasa.com/)
- The Zigbee network runs on the [deCONZ](https://phoscon.de/en/conbee2/software) add-on
- Home Assistant's database runs on [MariaDB](https://mariadb.org/)
- Lovelace uses my custom [homeOS theme](https://github.com/gvssr/home-assistant-config/tree/main/themes/homeOS_theme), based on work by [JuanMTech](https://github.com/JuanMTech)
- Daily backups are created and stored remotely through SMB using the [Samba Backup](https://github.com/thomasmauerer/hassio-addons/tree/master/samba-backup) add-on
- [Home Assistant iOS](https://github.com/home-assistant/iOS) app notifies me about new updates for Core, deCONZ, DSM and Custom Integrations
- Files and SSH are accessible using the [Samba share](https://github.com/home-assistant/addons/tree/master/samba), [SSH & Web Terminal](https://github.com/hassio-addons/addon-ssh) and [File Editor](https://github.com/home-assistant/addons/tree/master/configurator) add-ons
- This Git was setup using a [community guide](https://community.home-assistant.io/t/sharing-your-configuration-on-github/195144) and [Atlassian Git Cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)

### Hardware
| [Raspberry Pi 4B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)  | [ConBee II](https://phoscon.de/en/conbee2) | [Synology DS718+](https://www.synology.com/nl-nl/support/download/DS718+) | [Philips Hue Bridge v2](https://www.philips-hue.com/nl-nl/p/hue-bridge/8718696511800) | [Hue HDMI Sync Box](https://www.philips-hue.com/nl-nl/p/hue-play-hdmi-sync-box/8718699704803) | [SwitchBot Hub Mini](https://www.switch-bot.com/products/switchbot-hub-mini) | [Apple TV 4K](https://www.apple.com/apple-tv-4k/) |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| ![Raspberry Pi](https://github.com/gvssr/home-assistant-config/blob/main/.github/IMG/icons8-raspberry-pi-80.png#gh-light-mode-only)![Raspberry Pi](https://github.com/gvssr/home-assistant-config/blob/main/.github/IMG/icons8-raspberry-pi-80_dark-mode.png#gh-dark-mode-only) | ![USB](IMG/icons8-usb-memory-stick-80.png#gh-light-mode-only)![USB](IMG/icons8-usb-memory-stick-80_dark-mode.png#gh-dark-mode-only) | ![NAS](IMG/icons8-nas-80.png#gh-light-mode-only)![NAS](IMG/icons8-nas-80_dark-mode.png#gh-dark-mode-only) | ![Hub](IMG/icons8-hub-80.png#gh-light-mode-only)![Hub](IMG/icons8-hub-80_dark-mode.png#gh-dark-mode-only) | ![HDMI](IMG/icons8-hdmi-cable-80.png#gh-light-mode-only)![HDMI](IMG/icons8-hdmi-cable-80_dark-mode.png#gh-dark-mode-only) | ![Switch](IMG/icons8-switch-80.png#gh-light-mode-only)![Switch](IMG/icons8-switch-80_dark-mode.png#gh-dark-mode-only) | ![Apple TV](IMG/icons8-apple-tv-80.png#gh-light-mode-only)![Apple TV](IMG/icons8-apple-tv-80_dark-mode.png#gh-dark-mode-only) |
| Runs Home Assistant OS and it's add-ons like SSH and SMB from a [Kingston A400 SSD](https://www.kingston.com/en/ssd/a400-solid-state-drive)  | USB-gateway connected through a USB2.0 Extension cable to connect all my Zigbee nodes. | Stores SMB backups and contains a Homebridge instance for devices Home Assistant doesn't support.  | In use to control the entertainment area in conjuction with the HDMI Sync Box and OTAU Hue devices. | In use for the Ambilight behind the tv and the rest of the entertainment area in conjuction with the Hue Bridge.  | In use to connect to SwitchBot Curtains, runs through HomeBridge to Home Assistant.  | In use as HomeKit Home Hubs to run location automations and control the Home app when away. |

Icons by [Icons8](https://icons8.com)

## Implementation
In general, whenever I built something in Home Assistant it uses the following structure: an **Automation** to control a **Switch**, which triggers a **Script(s)**. Major exceptions to this rule are:
- deCONZ devices, which are controlled directly with Automations by listening for events, 
- Motion sensors, which are controlled by an Automation per sensor
- Notifications, which listen for state changes and calls the Notify service

### Home States
Globally, my Home Assistant config follows a **State** path during the day, which controls how certain Automations, and thus Switches and Scripts run: ⛅️ `Morning` ⇢ ☀️ `Day` ⇢ 🌜 `Evening` ⇢ 🌑 `Night`

Each **Home State** is controlled by a Switch and corresponding Input Select, which run Scripts in the background. All of these either run automatically through Automations, or can be called through a Home app or a physical controller. Roughly, the corresponding actions are as following:

- ⛅️ `Morning` turns off outside lights, and opens all the blinds except the bedroom
- ☀️ `Day` ensures the `Home` Occupancy is set, opens all curtains and runs certain bedroom automations
- 🌜 `Evening` turns on outside and living room lights, and closes all curtains
- 🌑 `Night` ensures the `Sleeping` Occupancy is set and turns off lights & devices

### Home State Occupancy
While **Home States** are mostly based on _time and/or sun-position_, I've also created **Home State Occupancy** as an additional variable based on location data. Similarly, these are controlled by Switches and an Input Select, which runs Scripts. Some of these, like `Away` and `On vacation` run automatically through Automations. Others, like `Sleeping` need to specifically be called, either through a Home app or physical controller. The following occupancy state transitions are possible:

- 🏠 `Home` ⇢ 💤 `Sleeping` turns security on, dims lights, adjusts heating and runs certain bedroom automations
- 🏠 `Home` ⇢ 📍 `Away` turns security on, turns off lights & devices and lowers heating
- 📍 `Away` ⇢ ⛱️ `On vacation` ensures Home State automations will run as if someone's home
- 💤 `Sleeping` | 📍 `Away` | ⛱️ `On vacation` ⇢ 🏠 `Home` turns security off, adapts lights and turns on heating

### Modes
Additionally, there are a couple of **Modes** which can be manually turned on depending on the situation. Turning them off runs the corresponding script actions of the currect **Home State** to ensure a smooth transition back to the status quo.
- 🍿 ``Cinema Mode`` ensures the ideal movie watching experience, by turning on the tv, closing the curtains and turning off or dimming certain lights
- 🎉 ``Party Mode`` ensures no automations are run that interfere with guests, like curtains opening, alarms triggering or lights dimming
- 👀 ``Privacy Mode`` ensures the living room is secured against prying eyes from outside, by closing the curtains, dimming lights, disabling camera's and playing music
