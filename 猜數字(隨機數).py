import random
start=int(input("請輸入隨機數字的開始值:"))
end=int(input("請輸入隨機數字的結束值:"))

r=random.randint(start,end)
count = 0
while True:
    count = count + 1
    pwd=(input("請輸入數字:"))
    if pwd == r:
        print("答對了")
        print("這次你猜的第",count,"次")
        break
    elif pwd > r:
        print("猜錯了!比答案大")
    elif pwd < r:
        print("猜錯了!比答案小")
    print("這次你猜的第",count,"次")
    
        
        
    
