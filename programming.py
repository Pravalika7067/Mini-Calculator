
#mini calculator 
print("=====Simple Calculator=====")
num1=float(input("Enter First number"))
num2=float(input("enter second number"))
print("choose operation")
print("1.Add")
print("2.subtract")
print("3.Multiply")
print("4.Divide")
choice=input("Enter choice (1/2/3/4):")
if choice =="1":
    result=num1+num2
    print("Result:",result)
elif choice=="2":
    result=num1-num2
    print("Result:",result)
elif choice=="3":
    result=num1*num2
    print("Result:",result)
elif choice=="4":
    if num2!=0:
        result=num1/num2
        print("Result:",result)
    else:
        print("cannot divide by zero")

else:
    print("Invalid choice")