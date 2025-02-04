# Pinger - Ping device via CLI

![PyPI](https://img.shields.io/pypi/v/geetak) ![License](https://img.shields.io/github/license/muflihnurfaizi/geetak) ![Python](https://img.shields.io/badge/python-3.8%2B-blue)

**Pinger** is a command-line application for monitoring network devices by pinging target IP addresses and reporting their status via MQTT. It allows you to configure MQTT settings, schedule automatic pings, and manage target devices—all from the terminal with a polished interface provided by Click and Rich.

---

## ✨ Features

- **Device Monitoring:** Ping a list of devices and report if they are online or offline.
- **MQTT Reporting:** Publish JSON-formatted reports to an MQTT broker.
- **Scheduling:** Set and update scheduled times for automatic pings (default: `10:00, 14:00, 19:00`).
- **Dynamic Configuration:** Update and view MQTT settings, schedule times, and device targets through dedicated CLI commands.
- **Rich CLI Interface:** User-friendly, formatted outputs (tables, progress bars, etc.) using [Rich](https://rich.readthedocs.io/) and [rich-click](https://github.com/RealOrangeOne/rich-click).

---

## 🚀 Installation

Pinger CLI is available on PyPI. To install it, simply run:

```bash
pip install pinger-cli
```

Once installed, the pinger command will be available in your terminal.

---

## 🛠️ Usage

### Starting the Pinger CLI

To start the application (which loads your configuration, sets up scheduled tasks, and listens for MQTT triggers), run:

```bash
pinger --config config.json
```

If no configuration file exists, you can create one or update settings using the configuration commands described below.

### Commands

#### MQTT Configuration
- Update MQTT Settings:

```bash
pinger setmqtt --broker new_broker_address --port 1883 --report-topic new_report_topic --trigger-topic new_trigger_topic
```

- Display Combined Configuration (MQTT & Schedule Times):

```bash
pinger showconfig --config config.json
```

This command displays both the current MQTT configuration and the scheduled times in a table format.

#### Scheduling
- Update Scheduling Times:

```bash
pinger setschedule --time 09:30 --time 12:00 --time 18:45
```

If you omit the --time options, the default schedule (10:00, 14:00, 19:00) will be set.

#### Device (IP Target) Management
- Add a New IP Target:
```bash
pinger addtarget --substation "Substation A" --bay "Bay 1" --ied "IED1" --ip "192.168.1.10" --source-ip "192.168.1.1"
```

- Display Current IP Targets:
```bash
pinger showtargets --config config.json
```


#### Triggering a Report

The application listens for MQTT messages on the trigger topic specified in your MQTT configuration. When a message (e.g., trigger) is received, the app immediately generates a report and publishes it via MQTT.

## 📖 Configuration File Format

Your configuration file (default: config.json) is a JSON file that may look like this:

```bash
{
  "mqtt": {
    "broker": "broker.mqtt-dashboard.com",
    "port": 1883,
    "report_topic": "muflihuns/ied/connection_report_MRNDA",
    "trigger_topic": "muflihuns/ied/trigger_report_MRNDA"
  },
  "schedule_times": ["10:00", "14:00", "19:00"],
  "ied_list": [
    {
      "substation": "GIS Marunda",
      "bay": "Bay Transformer 1",
      "ied": "OC150",
      "ip": "10.140.16.131",
      "source_ip": "10.140.16.120"
    },
    {
      "substation": "GIS Marunda",
      "bay": "Bay Transformer 1",
      "ied": "LCD",
      "ip": "10.140.16.132",
      "source_ip": "10.140.16.120"
    }
  ]
}
```

mqtt: Contains MQTT broker settings.
- schedule_times: An array of times (in HH:MM format) for when the app should automatically generate reports.
- ied_list: A list of devices with their target IP addresses, source IP addresses, and identifiers.

## 🪛 Troubleshooting
- Configuration File: Ensure that your configuration file exists and is properly formatted.
- MQTT Connection: Verify that the MQTT broker settings are correct and that the broker is reachable.
- Ping Command: If you encounter issues with pinging devices, ensure your operating system supports the parameters used in the command (you may need to adjust the command for your OS).

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## 🛡️ License

This project is licensed under the [MIT](LICENSE) License.

## ⭐ Support
If you find Pinger useful, don’t forget to give a star ⭐ on this repository!
