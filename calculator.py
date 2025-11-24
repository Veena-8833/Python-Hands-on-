
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
operator=input("enter operator:")
if operator=="+":
    result=num1+num2
    print(result)
elif operator=="-":
    result=num1-num2
    print(result)
elif operator=="*":
    result=num1*num2
    print(result)
elif operator=="/":
    if num2==0:
        print("Eror message")
    else:
        result=num1/num2
        print(result)
else:
    print("invalid operator")
        
    