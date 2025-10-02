def calculate_tax(item, price)
    item = input("Item Price\n")
    price =  input("Price of item")
    rate = 0.06875

    def calculat_tax(item, price, rate):
        print("The amount of tax to be collected on a " + price " Dollar" + item + " is " + (price*rate))
calculate_tax("Starbucks", 7.99, 0.6825)