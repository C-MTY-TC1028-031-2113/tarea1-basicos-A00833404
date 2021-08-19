def main():
    #escribe tu código abajo de esta línea
    print("Programa para bajar de peso.")
    ini = float(input("Introduzca su peso actual: "))
    fin = float(input("Ahora, introduzca el peso al que desee llegar: "))
    mes = int(input("Por último, introduzca el lapso en el que lo desee completar (meses): "))
    cal = (ini - fin)/(mes)
    print("Lo que debes bajar por mes es: " + str(cal))
 



if __name__ == '__main__':
    main()
