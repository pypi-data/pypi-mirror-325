#!/usr/bin/env python
import subprocess
import json
import time
from datetime import datetime
import schedule
import paho.mqtt.client as mqtt
import click
import rich_click
from rich_click import RichGroup, RichCommand
from rich import print
from rich.table import Table

# -----------------------------
# Configure rich-click settings
# -----------------------------
rich_click.rich_click.USE_RICH_MARKUP = True
rich_click.rich_click.MAX_WIDTH = 45
rich_click.rich_click.SHOW_ARGUMENTS = True
rich_click.rich_click.SHOW_METAVARS_COLUMN = False
rich_click.rich_click.GROUP_ARGUMENTS_OPTIONS = True

# Global configuration variable
config = {}

# -----------------------------
# Core Functions
# -----------------------------
def load_config(file_path):
    """Load configuration from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)

def save_config(file_path, config_data):
    """Save configuration data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(config_data, file, indent=2)

def ping_device(ip, source_ip):
    """Ping a device using the specified source IP."""
    try:
        # Adjust the ping command as needed for your OS
        command = ["ping", "-S", source_ip, "-n", "1", ip]
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if "Destination host unreachable" in result.stdout or "Request timed out" in result.stdout:
            return False
        if "Reply from" in result.stdout:
            return True
        return False
    except Exception as e:
        print(f"[red]Error pinging {ip} with source IP {source_ip}: {e}[/red]")
        return False

def send_to_mqtt(report, mqtt_config):
    """Send the JSON report to the MQTT broker."""
    def on_connect(client, userdata, flags, rc, properties=None):
        print(f"[green]Connected to MQTT with result code {rc}[/green]")

    # Revised on_publish callback: removed reason_code parameter.
    def on_publish(client, userdata, mid, properties=None):
        print(f"[green]Message published with MID: {mid}[/green]")

    client = mqtt.Client(protocol=mqtt.MQTTv5)
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.connect(mqtt_config["broker"], mqtt_config["port"], 60)
    client.loop_start()
    client.publish(mqtt_config["report_topic"], json.dumps(report), qos=1)
    time.sleep(2)  # Allow time for the message to be sent
    client.loop_stop()
    client.disconnect()

def generate_report():
    """Generate a report by pinging devices and sending it via MQTT."""
    report = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": []
    }
    for device in config.get("ied_list", []):
        source_ip = device["source_ip"]
        status = "online" if ping_device(device["ip"], source_ip) else "offline"
        report["results"].append({
            "substation": device["substation"],
            "bay": device["bay"],
            "ied": device["ied"],
            "ip": device["ip"],
            "source_ip": source_ip,
            "status": status
        })
    print("[bold blue]Generated Report:[/bold blue]")
    print(json.dumps(report, indent=2))
    send_to_mqtt(report, config["mqtt"])

def on_message(client, userdata, msg):
    """MQTT callback for receiving manual trigger messages."""
    print(f"[yellow]Trigger received on topic {msg.topic}: {msg.payload.decode()}[/yellow]")
    if msg.topic == config["mqtt"]["trigger_topic"]:
        print("[bold green]Manual trigger activated. Generating report...[/bold green]")
        generate_report()

def schedule_jobs():
    """Schedule automatic report generation at times specified in the configuration."""
    for time_str in config.get("schedule_times", []):
        schedule.every().day.at(time_str).do(generate_report)
    if "schedule_times" in config:
        print(f"[bold green]Scheduled tasks set for: {', '.join(config['schedule_times'])}[/bold green]")
    else:
        print("[yellow]No schedule_times set in configuration.[/yellow]")

# -----------------------------
# CLI Definition using Click & Rich-Click
# -----------------------------
@click.group(cls=RichGroup)
def cli():
    """[bold blue]Pinger CLI[/bold blue] app for device monitoring and MQTT reporting."""
    pass

@cli.command(cls=RichCommand, short_help="Start the Pinger CLI app.")
@click.option(
    "--config",
    "config_path",
    type=str,
    default="config.json",
    help="Path to the configuration file (default: config.json)"
)
def pinger(config_path):
    """Start the Pinger CLI app.

    This command loads the configuration, sets up scheduled tasks for report generation,
    and listens for manual MQTT triggers to generate reports.
    """
    global config
    try:
        config = load_config(config_path)
    except Exception as e:
        print(f"[red]Failed to load configuration file: {e}[/red]")
        return

    schedule_jobs()

    client = mqtt.Client(protocol=mqtt.MQTTv5)
    client.on_message = on_message
    try:
        client.connect(config["mqtt"]["broker"], config["mqtt"]["port"], 60)
    except Exception as e:
        print(f"[red]Failed to connect to MQTT broker: {e}[/red]")
        return
    client.subscribe(config["mqtt"]["trigger_topic"])
    client.loop_start()

    print("[bold green]Pinger CLI app started. Press Ctrl+C to stop.[/bold green]")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("[red]Program stopped manually.[/red]")
    finally:
        client.loop_stop()
        client.disconnect()

# ----- MQTT Configuration Commands -----
@cli.command(cls=RichCommand, short_help="Update MQTT configuration parameters.")
@click.option("--broker", type=str, help="MQTT broker hostname or IP.")
@click.option("--port", type=int, help="MQTT broker port.")
@click.option("--report-topic", type=str, help="MQTT report topic.")
@click.option("--trigger-topic", type=str, help="MQTT trigger topic.")
@click.option(
    "--config",
    "config_path",
    type=str,
    default="config.json",
    help="Path to the configuration file (default: config.json)"
)
def setmqtt(broker, port, report_topic, trigger_topic, config_path):
    """Update the MQTT configuration parameters in the config file."""
    default_mqtt_config = {
        "broker": "broker.mqtt-dashboard.com",
        "port": 1883,
        "report_topic": "muflihuns/ied/connection_report_MRNDA",
        "trigger_topic": "muflihuns/ied/trigger_report_MRNDA"
    }
    try:
        cfg = load_config(config_path)
    except FileNotFoundError:
        print(f"[yellow]Configuration file '{config_path}' not found. A new one will be created with default MQTT settings.[/yellow]")
        cfg = {"mqtt": default_mqtt_config.copy()}
    except Exception as e:
        print(f"[red]Failed to load configuration file: {e}[/red]")
        return

    if "mqtt" not in cfg:
        cfg["mqtt"] = default_mqtt_config.copy()
    else:
        for key, default_value in default_mqtt_config.items():
            if key not in cfg["mqtt"]:
                cfg["mqtt"][key] = default_value

    if broker:
        cfg["mqtt"]["broker"] = broker
    if port:
        cfg["mqtt"]["port"] = port
    if report_topic:
        cfg["mqtt"]["report_topic"] = report_topic
    if trigger_topic:
        cfg["mqtt"]["trigger_topic"] = trigger_topic

    try:
        save_config(config_path, cfg)
        print(f"[bold green]MQTT configuration updated successfully.[/bold green]")
    except Exception as e:
        print(f"[red]Failed to save configuration file: {e}[/red]")

# ----- Scheduling Commands -----
@cli.command(cls=RichCommand, short_help="Update scheduling times.")
@click.option("--time", "times", multiple=True, help="Schedule time in HH:MM format. Can be used multiple times. Default: 10:00, 14:00, 19:00")
@click.option(
    "--config",
    "config_path",
    type=str,
    default="config.json",
    help="Path to the configuration file (default: config.json)"
)
def setschedule(times, config_path):
    """Update scheduling times in the config file."""
    default_schedule = ["10:00", "14:00", "19:00"]
    try:
        cfg = load_config(config_path)
    except FileNotFoundError:
        print(f"[yellow]Configuration file '{config_path}' not found. A new one will be created.[/yellow]")
        cfg = {}
    except Exception as e:
        print(f"[red]Failed to load configuration file: {e}[/red]")
        return

    if times:
        cfg["schedule_times"] = list(times)
    else:
        cfg["schedule_times"] = default_schedule

    try:
        save_config(config_path, cfg)
        print(f"[bold green]Schedule times updated successfully.[/bold green]")
    except Exception as e:
        print(f"[red]Failed to save configuration file: {e}[/red]")

# ----- Combined Configuration Display Command -----
@cli.command(cls=RichCommand, short_help="Display current MQTT configuration and schedule times.")
@click.option(
    "--config",
    "config_path",
    type=str,
    default="config.json",
    help="Path to the configuration file (default: config.json)"
)
def showconfig(config_path):
    """Display the current MQTT configuration and scheduling times from the config file in table format."""
    try:
        cfg = load_config(config_path)
        # Display MQTT Configuration
        mqtt_cfg = cfg.get("mqtt", {})
        if mqtt_cfg:
            table = Table(title="MQTT Configuration")
            table.add_column("Parameter", style="cyan", no_wrap=True)
            table.add_column("Value", style="magenta")
            for key, value in mqtt_cfg.items():
                table.add_row(key, str(value))
            print(table)
        else:
            print("[yellow]No MQTT configuration found.[/yellow]")
        # Display Schedule Times
        schedule_times = cfg.get("schedule_times", [])
        if schedule_times:
            table2 = Table(title="Schedule Times")
            table2.add_column("Time", style="green", no_wrap=True)
            for t in schedule_times:
                table2.add_row(str(t))
            print(table2)
        else:
            print("[yellow]No schedule times set in configuration.[/yellow]")
    except FileNotFoundError:
        print(f"[red]Configuration file '{config_path}' not found.[/red]")
    except Exception as e:
        print(f"[red]Failed to load configuration file: {e}[/red]")

# ----- IP Target (Device) Configuration Commands -----
@cli.command(cls=RichCommand, short_help="Add a new target IP to ping.")
@click.option("--substation", required=True, type=str, help="Name of the substation.")
@click.option("--bay", required=True, type=str, help="Name of the bay.")
@click.option("--ied", required=True, type=str, help="IED identifier.")
@click.option("--ip", required=True, type=str, help="Target IP address to ping.")
@click.option("--source-ip", required=True, type=str, help="Source IP address to use for the ping command.")
@click.option(
    "--config",
    "config_path",
    type=str,
    default="config.json",
    help="Path to the configuration file (default: config.json)"
)
def addtarget(substation, bay, ied, ip, source_ip, config_path):
    """Add a new device target to the configuration."""
    try:
        cfg = load_config(config_path)
    except FileNotFoundError:
        print(f"[yellow]Configuration file '{config_path}' not found. A new one will be created.[/yellow]")
        cfg = {}
    except Exception as e:
        print(f"[red]Failed to load configuration file: {e}[/red]")
        return

    if "ied_list" not in cfg:
        cfg["ied_list"] = []

    new_device = {
        "substation": substation,
        "bay": bay,
        "ied": ied,
        "ip": ip,
        "source_ip": source_ip
    }
    cfg["ied_list"].append(new_device)

    try:
        save_config(config_path, cfg)
        print(f"[bold green]Added new target:[/bold green] {new_device}")
    except Exception as e:
        print(f"[red]Failed to save configuration file: {e}[/red]")

@cli.command(cls=RichCommand, short_help="Display current IP target configuration.")
@click.option(
    "--config",
    "config_path",
    type=str,
    default="config.json",
    help="Path to the configuration file (default: config.json)"
)
def showtargets(config_path):
    """Display the current list of target IPs from the configuration file in table format."""
    try:
        cfg = load_config(config_path)
        targets = cfg.get("ied_list", [])
        if targets:
            table = Table(title="Current IP Targets")
            table.add_column("Substation", style="cyan", no_wrap=True)
            table.add_column("Bay", style="green", no_wrap=True)
            table.add_column("IED", style="magenta", no_wrap=True)
            table.add_column("IP", style="yellow", no_wrap=True)
            table.add_column("Source IP", style="red", no_wrap=True)
            for target in targets:
                table.add_row(
                    target.get("substation", ""),
                    target.get("bay", ""),
                    target.get("ied", ""),
                    target.get("ip", ""),
                    target.get("source_ip", "")
                )
            print(table)
        else:
            print("[yellow]No IP targets found in configuration.[/yellow]")
    except FileNotFoundError:
        print(f"[red]Configuration file '{config_path}' not found.[/red]")
    except Exception as e:
        print(f"[red]Failed to load configuration file: {e}[/red]")

if __name__ == "__main__":
    cli()