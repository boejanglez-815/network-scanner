import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime

# Load and parse the Nmap XML output
tree = ET.parse("scan_results.xml")
root = tree.getroot()

# Store all scan data here
scan_data = []

# Loop through each scanned device
for host in root.findall("host"):
    ip = host.find("address").attrib.get("addr", "")
    
    hostname_tag = host.find("hostnames/hostname")
    hostname = hostname_tag.attrib.get("name", "") if hostname_tag is not None else ""

    ports = host.find("ports")
    if ports is not None:
        for port in ports.findall("port"):
            port_id = port.attrib.get("portid", "")
            protocol = port.attrib.get("protocol", "")
            
            service = port.find("service")
            service = service.attrib.get("name", "") if service is not None else "unknown"

            state = port.find("state").attrib.get("state", "")

            scan_data.append({
                "ip_address": ip,
                "hostname": hostname,
                "port": int(port_id),
                "protocol": protocol,
                "service": service,
                "status": state,
                "scan_time": datetime.now().strftime("%H:%M:%S")
            })

# Convert to Excel
df = pd.DataFrame(scan_data)
df.to_excel("network_scan_dashboard.xlsx", index=False, sheet_name="Scan Report")
