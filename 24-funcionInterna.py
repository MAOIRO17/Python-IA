def externa():
    def interna():
        print("¡Hola desde la función interna!")
    print(interna())
externa()