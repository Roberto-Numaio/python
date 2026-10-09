priceProduct = int(input("What is the price of the product: "))
discount = '5%'

print ("This product costs {}$, with {} discount the new price is {}".format(priceProduct, discount, (priceProduct - ( (priceProduct*5) /100) )))
      