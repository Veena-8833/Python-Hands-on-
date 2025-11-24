def ip_reachability():
    ip=input("enter ip address:")
    print("testing ip:",ip)
def calculate_avg(data):
    return sum(data)/len(data)
def get_summary(data):
    summary={
        "min":min(data),
        "max":max(data),
        "average":calculate_avg(data)
    }
    return summary
while True:
    print("1.IP reachability")
    print("2.call summary function ")
    print("3.exit")
    choice=input("enter choice:")
    if choice=="1":
        ip_reachability()
    elif choice=="2":
        values=input("enter comma separated numbers: ")
        data=[float(x) for x in values.split(",")]
        result=get_summary(data)
        print(result)
    elif choice=="3":
        print("exit program")
        break
    else:
        print("invalid choice")
        