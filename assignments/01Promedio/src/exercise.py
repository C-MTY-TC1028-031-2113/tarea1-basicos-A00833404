def main():
    #escribe tu código abajo de esta línea
    mat1 = float(input("Calificación de la materia: "))
    mat2 = float(input("Calificación de la materia: "))
    mat3 = float(input("Calificación de la materia: "))
    mat4 = float(input("Calificación de la materia: "))
    prom = float((mat1 + mat2 + mat3 + mat4)/4)
    print("El promedio es: " + str(prom))
main()

if __name__ == '__main__':
    main()