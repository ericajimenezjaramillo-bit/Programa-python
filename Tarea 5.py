#Nombre del estudiante: Erica Jimenez Jaramillo
#Grupo:213022_1034
#Programa: Ingenieria de sistemas
#Codigo fuente: Autoria propia

#Auditoria de inventario
#R1:MATRIZ DE INVENTARIO
inventario = [
    ["A001", "ARROZ", 20, 50],
    ["A002", "AZUCAR", 60, 40],
    ["A003", "ACEITE", 10, 30],
    ["A004", "SAL", 25, 25],
    ["A005", "CAFE", 5, 20]
]
#R2 Y R3: FUNCION PARA CALCULAR PEDIDO
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

#R4: GENERAR LISTA DE PEDIDOS
lista_pedidos = []
for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)
    if cantidad_pedir > 0:
        lista_pedidos.append([nombre, cantidad_pedir])
    else:
        lista_pedidos.append([nombre, 0])

#R5: MOSTRAR RESULTADOS
print("Auditoria de inventario\n")
print("Lista de pedidos:\n")
for item in lista_pedidos:
    print(f"Articulo: {item[0]} | Cantidad a pedir: {item[1]}")