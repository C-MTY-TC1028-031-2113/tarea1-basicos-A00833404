def main():
    #escribe tu código abajo de esta línea
    ini = float(input("Dame el peso inicial: "))
    fin = float(input("Dame el peso final: "))
    mes = int(input("Dame la cantidad de meses: "))
    cal = (ini - fin)/(mes)
    print("Lo que debes bajar por mes es: " + str(cal))
 



if __name__ == '__main__':
    main()
