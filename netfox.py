import scapy.all as scapy
import socket
import re

print("""
                    _   _      _   ______
                   | \ | |    | | |  ____|
                   |  \| | ___| |_| |__ _____  __
                   |   ` |/ _ \ __|  __/ _ \ \/ /
                   | |\  |  __/ |_| | | (_) >  <
                   |_| \_|\___|\__|_|  \___/_/\_\

       __  ____      __               __   ______
      /  |/  (_)____/ /_  ____ ____  / /  / ____/___  ____  ____ _
     / /|_/ / / ___/ __ \/ __ `/ _ \/ /  / /_  / __ `/ __ \/ __ `/
    / /  / / / /__/ / / / /_/ /  __/ /  / __/ / /_/ / / / / /_/ /
   /_/  /_/_/\___/_/ /_/\__,_/\___/_/  /_/    \__,_/_/ /_/\__, /
                                                         /____/
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│                   Thank you for using NetFox :)                    │
│                                                                    │
│                  Copyright of Michael Fang, 2021                   │
│                                                                    │
│               This is for educational purposes only                │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
""")

ip_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
opened_ports = []

option = input("""Please select an option:

            (1) Scan Devices          (2) Scan Ports

>>>""")

if option == '1':
    while True:
        ip_entered = input("Please enter the IP you want to scan:")
        if ip_range_pattern.search(ip_entered):
            print("Start scanning...")
            scapy.arping(ip_entered)
            print("Scan completed!")
            break
        else:
            print("Please enter a valid IP range!")
if option == '2':
    while True:
        port_ip_entered = input("Please enter the IP you want to scan:")
        if ip_pattern.search(port_ip_entered):
            break
        else:
            print("Please enter a valid IP!")
    while True:
        port_range = input("Please enter the port range (ex: 1-99):")
        port_range_correct = port_range_pattern.search(port_range)
        if port_range_correct:
            port_min = int(port_range_correct.group(1))
            port_max = int(port_range_correct.group(2))
            break
        else:
            print("Please enter a valid port range!")
    for port in range(port_min, port_max + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as so:
                so.settimeout(0.5)
                so.connect((port_ip_entered, port))
                opened_ports.append(port)
        except:
            pass
    for port in opened_ports:
        print(f"""
        Port {port} is open""")
