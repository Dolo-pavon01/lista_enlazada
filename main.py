from lista import Lista

def main():
    lista= Lista()
    for i in range(10):
        lista.insertar(i)
    
    

    print(lista[3],lista[-3])
    #aca ves como funciona  yield
    lista[0]="HOla"
    print("Con yield")
    for i in lista:
        print(i, end="")
    
main()
