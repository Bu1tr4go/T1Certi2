def TipoTriangulo(a, b, c):
    res = ""
    if a == b and b == c:
        res = "EQUILATERO"
    elif a == b or a == c or b == c:
        res = "ISOSCELES"
    else:
        res = "ESCALENO"
    return res

if __name__ == "__main__":
    a = float(input("Ingresa el lado A del triángulo: "))
    b = float(input("Ingresa el lado B del triángulo: "))
    c = float(input("Ingresa el lado C del triángulo: "))
    tipo = TipoTriangulo(a, b, c)
    print("EL TRIÁNGULO ES " + tipo)
    input("Presiona enter para acabar...")


    