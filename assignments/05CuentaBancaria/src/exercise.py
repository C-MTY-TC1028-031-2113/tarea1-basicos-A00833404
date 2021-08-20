def main():
    #escribe tu código abajo de esta línea
    ant = float(input("Ingrese el saldo del mes anterior: "))
    ing = float(input("Ingresos: "))
    egr = float(input("Egresos: "))
    ja = int(input("Número de cheques expedidos: "))
    che = ja * 13
    fin = ant + ing - egr - che
    res = (fin * 0.075) 
    print("Saldo del final del mes: " + str(fin-res))




if __name__ == '__main__':
    main()
