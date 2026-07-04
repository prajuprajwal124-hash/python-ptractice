#calculater
print("basic calcualter")
R=int(input("enter num1:"))
T=int(input("enter num2:"))
y=input("choose any operator:")
if y == "add":
    print(" ",R+T)
elif y=="sub":
    print("",R-T)
elif y=="mul":
    print("",R*T)
elif y=="div":
    if T != 0:
       print("",R/T)
    else:
        print("divided by zero")
else:
    print("invalid operation ")

