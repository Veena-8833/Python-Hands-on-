
latency_list=[23,56,77,89,35]
def calculate_avg(data):
    return sum(data)/len(data)
def get_summary(data):
    summary={
        "min":min(data),
        "max":max(data),
        "average":calculate_avg(data)
    }
    return summary
result=get_summary(latency_list)
print(result)
while True:
    print("1.IP reachability")
    print("2.call summary function ")
    print("3.exit")
    choice=input("enter choice:")
    if choice=="1":
        ip_reachability(input("ip:"))
    elif choice=="2":
        values=list(map(int,input("latence values:").split(",")))
        print(get_summary(values))
    elif choice=="3":
        print("exit program")
        break
    else:
        print("invalid choice")