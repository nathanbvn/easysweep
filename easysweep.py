import ipaddress
import sys 
import subprocess
import threading


def pingIp(addr):
    result = subprocess.run(
        'ping -c 1 '+addr, 
        shell=True, 
        executable="/bin/bash", 
        stdout=subprocess.DEVNULL,  
        stderr=subprocess.DEVNULL   
    )
    if "returncode=0" in str(result): 
        ipCo = str(result).split("-c 1 ")[1].split("'")[0]
        print(ipCo)

args = sys.argv

if len(args) < 2 :
    print("\nEasySweep requires an argument !! \n")
    print("Correct format : python3 easysweep.py [network_ip]/[mask] \n")
else :
    ip = args[1]
    n1 = ipaddress.ip_network(ip)
    
    print("------------- EasySweep ------------------")
    print("    SCANNING NETWORK !")
    print("CONNECTED IP's : \n")

    threads = []
    
    for addr in list(n1):
        thread = threading.Thread(target=pingIp, args=(str(addr),))
        threads.append(thread)
        thread.start()

    
    for thread in threads:
        thread.join()


