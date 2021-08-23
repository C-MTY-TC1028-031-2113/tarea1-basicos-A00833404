def main():
    #escribe tu código abajo de esta línea
    ant = float(input("Dame el saldo del mes anterior: "))
    ing = float(input("Dame los ingresos: "))
    egr = float(input("Dame los egresos: "))
    ja = int(input("Dame el número de cheques: "))
    che = ja * 13
    fin = ant + ing - egr - che
    res = (fin * 0.075) 
    print("El saldo final de la cuenta es: " + str(fin-res))




if __name__ == '__main__':
    main()
