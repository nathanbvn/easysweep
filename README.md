# easysweep
Ping Sweeper | Scan active IP's in your network

EasySweep

EasySweep is a simple Python-based networking and scanning tool that identifies and lists the active IP addresses connected to a network. It takes a network IP range as input, performs ping sweeps, and prints the IP addresses that are online within that range. This tool is useful for basic network diagnostics and network discovery.
Features

    Network Scanning: Scans all IP addresses in a given network range.
    Multi-threaded: Executes ping requests concurrently using threads to speed up scanning.
    Cross-Platform: Compatible with systems that support Python and the ping command.

Requirements

    Python 3.x
    Linux-based or Unix-like systems (uses /bin/bash for running ping commands)

* Installation * 

    Clone the repository:
  
```
git clone https://github.com/nathanbvn/easysweep.git
```

Navigate into the project directory:
```

    cd easysweep
```

Usage

You can run EasySweep directly using Python 3. It requires a network IP address and subnet mask in CIDR notation.
Command:

```

python3 easysweep.py [network_ip]/[mask]
```

Example:
```
python3 easysweep.py 192.168.1.0/24
```

Output:

The tool will scan the network and display a list of connected (active) IP addresses in the given range:
```

------------- EasySweep ------------------
    SCANNING NETWORK !
CONNECTED IP's :

192.168.1.1
192.168.1.3
192.168.1.5

```
How it Works

    Network Input: You provide a network in CIDR notation (e.g., 192.168.1.0/24). The tool uses Python’s ipaddress module to generate the list of IPs in the network.

    Ping Sweep: For each IP address in the network, a ping request is sent using a separate thread. If the host responds, it is considered connected, and the IP is printed.

    Multi-threading: The tool utilizes Python’s threading module to perform ping requests in parallel, allowing faster network scans.

