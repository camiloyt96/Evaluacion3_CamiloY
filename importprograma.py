import ProgramaStarken as fun


while True:
    try:
        print("Bienvenido al Menu de pedidos de correo\nSeleccione una opcion para continuar: ")
        print("1. Registrar pedido")
        print("2. Listar todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir")

        opc = int(input(""))

        if opc == 1:
            fun.registrar_pedido()
        if opc == 2:
            fun.listar_pedidos()
        if opc == 3:
            fun.imprimir_pedidos()
        if opc == 4:
            print("Usted ha salido del programa de correos, que tenga buena tarde!!.")
            break
    except:
        print("Hubo un error de ingreso, vuelva a intentarlo porfavor. ")