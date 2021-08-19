def main():
    #escribe tu código abajo de esta línea
    print("Programa para calcular promedio.")
    mat1 = float(input("Introduzca su primera calificación: "))
    mat2 = float(input("Ahora la segunda: "))
    mat3 = float(input("Enseguida, la tercera: "))
    mat4 = float(input("Por último, la cuarta: "))
    prom = (mat1 + mat2 + mat3 + mat4)/4
    print("El promedio se sus calificaciones es: " + str(prom))
main()

if __name__ == '__main__':
    main()
