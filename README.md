# Network ScannerV3

This is a "simple' network scanner I built using nmap, Python, and Excel.(This took me THREE times to perfect.)

It scans devices on a local network and exports the results into a clean Excel file. The Excel file includes a pie chart that breaks down open and filtered ports.

**~ Tools Used**

nmap ~ for scanning IP addresses, ports, and services  
Python ~ for parsing XML and generating Excel output  
pandas ~ for handling and formatting data  
Excel ~ for creating the visual dashboard  

**~ What It Does**

Scans the local network (example: 192.168.1.0/24)  
Pulls the IP, hostname, port, protocol, service, and status  
Outputs a formatted Excel file with a dashboard-style summary  

**~ How To Run It**

1. Run the network scan:
```bash
nmap -p- -T4 -oX scan_results.xml 192.168.1.0/24

2.

python3 nmap_to_excel.py
