thisList = ['5','3','5','2','7','8','9','1','4','6']
print(thisList," is the given list.")
a = input("Enter 'm' to find minimum number or 'M' to find maximum number :")
if a == 'm':
    print(min(thisList)," is the minimum number.")
elif a == 'M':
    print(max(thisList)," is the maximum number.")
else:
    print("Enter 'm' or 'M' only")
