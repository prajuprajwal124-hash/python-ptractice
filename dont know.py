#calculater
print("basic calcualter")
R=int(input("enter num1:"))
T=int(input("enter num2:"))
y=input("choose any operator (+,-,*,/):")
if y == "+":
    print(" ",R+T)
elif y=="-":
    print("",R-T)
elif y=="*":
    print("",R*T)
elif y=="/":
    if T != 0:
       print("",R/T)
    else:
        print("divided by zero")
else:
    print("invalid operation ")

