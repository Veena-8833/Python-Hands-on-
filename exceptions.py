
ip_list=["172.0.0.1","192.168.1.0","8.8.8.1","10.0.0.1"]
import subprocess

for ip in ip_list:
    print(f"checking {ip}..")
    try:
        result=subprocess.run(["ping","-n","1",ip],
                              timeout=0.005)
        if result.returncode==0:
            print(f"{ip} is reachable")
        else:
            print("f{ip} is unreachable")
    except subprocess.TimeoutExpired:
        print(f"{ip} ping timed out\n")