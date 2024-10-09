import ipaddress
import sys
import subprocess
import concurrent.futures  


def pingIp(addr):
    result = subprocess.run(
        'ping -c 1 ' + addr,
        shell=True,
        executable="/bin/bash",
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if result.returncode == 0:  
        print(addr)


args = sys.argv

if len(args) < 2:
    print("\nEasySweep requires an argument !! \n")
    print("Correct format : python3 easysweep.py [network_ip]/[mask] \n")
else:
    ip = args[1]
    n1 = ipaddress.ip_network(ip)

    print("------------- EasySweep ------------------")
    print("    SCANNING NETWORK !")
    print("CONNECTED IP's : \n")

    
    with concurrent.futures.ThreadPoolExecutor(max_workers=255) as executor:
        
        executor.map(pingIp, (str(addr) for addr in n1))
