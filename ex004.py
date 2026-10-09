data = input("Write something: ")

print("its primitive type is: ",  type(data))
print("Is it alphabetic?", data.isalpha())
print("Is it a number?", data.isnumeric())
print("Is is in upper letters?", data.isupper())
print("Is it in lower letters?", data.islower())
print("Is it capitalised?", data.istitle())