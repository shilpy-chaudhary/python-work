def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        print("num1 is max.")
        return num1

    elif num2>=num1 and num2>=num3:
        print("num2 is max.")
        return num2

    else:
        print("num3 is max.")   
        return num3 


result=max_num(2,5,7)

print(result)
