import os
#檢查檔案存在否
def chackfile(filename):
    products = []
    with open(filename, "r", encoding="utf8") as r:
        for line in r:
             if "商品,價格" in line:
                  continue
        name, price = line.strip().split(",")
        products.append([name, price])
        print(products)
    return products
#使用者輸入
def userinput(products):
    while True :
        name = input("請輸入商品名稱:")
        if  name == "q" :
            break
        price = int(input("請輸入價格:"))
        products.append([name,price])
    print (products)
    return products
#印出價錢
def printproducts(products):
    for p in products:
        print (p[0],"價錢為:",p[1])
# 寫入檔案
def writeproducts(filename,products):
    with open(filename,"w",encoding= "utf-8") as f :
        f.write('商品,價格\n')
        for p in products :
            f.write(p[0]+","+str(p[1])+"\n")

def main():
    filename= "products.csv"
    if os.path.isfile(filename) :
        print("找到檔案了!!")
        products = chackfile(filename)
    else:
        products = []
        print('找不到檔案')

    products = userinput(products)
    printproducts(products)
    writeproducts('products.csv',products)

main()