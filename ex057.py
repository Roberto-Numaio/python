genero = input("Qual e seu genero [M/F]: ")

while genero not in "MmFf":
    genero = input("Genero invalido. Por favor, digite novamente [M/F]: ")
print("Genero {} registrado com sucesso!".format(genero))