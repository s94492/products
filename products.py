import os
product = []
#檢查檔案存在否
if os.path.isfile('products.csv') :
    print ("找到檔案了!!")
    with open("products.csv", "r", encoding="utf8") as r:
        for line in r:
            if "商品,價格" in line:
                continue
            name, price = line.strip().split(",")
            product.append([name, price])
    print(product)
else:
    print("查無檔案")

#使用者輸入
while True :
    name = input("請輸入商品名稱:")
    if  name == "q" :
        break
    price = int(input("請輸入價格:"))
    product.append([name,price])
print (product)

#印出價錢
for p in product:
    print (p[0],"價錢為:",p[1])

# 寫入檔案
with open("products.csv","w",encoding= "utf-8") as f :
    f.write('商品,價格\n')
    for p in product :
        f.write(p[0]+","+str(p[1])+"\n")

