##14. Build a dictionary where the keys are product names and the values are their prices.
##Implement options to:
##a. Add a new product
##b. Update price of an existing product
##c. Find products within a given price range


product={}

#Add a new product
def add_product(product):
    name=input("Enter product name: ")
    price=float(input("Enter price: "))
    product[name]=price
    print("product added successfully....")

#Update price of an existing product
def update_product(product):
    update_name=input("Enter name of price to update: ")
    if update_name in product:
        update_price=float(input("Enter new price of product: "))
        product[update_name]=update_price
        print("Product updated successfully....")
    else:
        print("Sorry!! Product Not found....")
#Find products within a given price range

def find_product(product):
    min_range=float(input("Enter the minimum range: "))
    max_range=float(input("Enter the maximum range: "))
    found=False
    for name,value in product.items():
        if value >= min_range and value <= max_range:
            print(f"{name}={value:.2f}")
            found=True
        if not found:
            print("sorry!! No product found within the given range")

#main
while True:
    choice=int(input('''
 ----------------------------------------------
|-------Choose one of the options below------- |
 ----------------------------------------------
|1 : Add a new product                         |
|2 : Update price of an existing product       |
|3 : Find products within a given price range  |
|4 : Exit                                      |
 ----------------------------------------------
'''))
    if choice==1:
        add_product(product)
    elif choice==2:
        update_product(product)
    elif choice==3:
        find_product(product)
    elif choice==4:
        print("Exiting program....")
        break
    else:
        print("Enter valid number")
    

 
    

