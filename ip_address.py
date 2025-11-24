
ip_list=["172.0.0.1","192.168.1.0","8.8.8.1","10.0.0.1"]
import subprocess
import os
for ip in ip_list:
    result=subprocess.run(["ping","-n","1",ip])
    if result.returncode==0:
        print(f"{ip} is reachable")
    else:
        print("f{ip} is unreachable")
