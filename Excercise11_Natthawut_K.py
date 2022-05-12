number = int(input("ใส่จำนวนชั้นปีระมิต :"))
for x in range(number):
    print(" " *(number-x), "*"  *(x+1)+ "*" * x)