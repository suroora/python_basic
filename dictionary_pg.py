product = {"pen": 10,
           "book": 25,
           "color": 20,
           "pencil": 5,
           "bag": 250,
           "eraser": 3,
           "tiffin box": 100
           }
y=input("enter the product :")
for i in product:
    if i==y:
        print("the price of",i,"is",product[i])



