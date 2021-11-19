import random
r=random.randint(1,100)
count = 0
maxN=100
minN=1
while True:
    num=int(input("請輸入"+str(minN)+"~"+str(maxN)+"間的數字:"))
    count = count + 1
    if num>maxN or num < minN:
        print("輸入有誤,請重新輸入")
        continue
    elif num < r:
        print("猜錯了")
        minN = num+1
    elif num > r :
        print("猜錯了")
        maxN = num-1
    elif num == r:
        print("猜對了")        
        break
    print("這次你猜的第",count,"次")
print("這次你猜的第",count,"次")
    
        
    
        
