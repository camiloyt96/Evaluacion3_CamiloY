#Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
#La empresa de reparto de paquetes a domicilio "PaquExpress" necesita desarrollar un sistema que permita
#registrar los pedidos antes de enviar su camión repartidor. Para el funcionamiento del sistema se requieren
#las siguientes funcionalidades
#1. Registrar pedido
#2. Listar los todos los pedidos
#3. Imprimir hoja de ruta
#4. Salir del programa
RegistroStarken = {}
paquetesLista = []
def registrar_pedido():
    while True:
        try:
            tamano_plus_paq = ""
            nombreUsuario = input("Ingrese el nombre de Usuario: ")
            direccionUsuario = input("Ingrese direccion de Usuario: ")
            sectorUsuario = input("Ingrese sector del Usuario: ").upper()
            
            while True:
                tamanoPedido = int((input("Ingrese el tamano del paquete.\n1. Pequeno\n2. Mediano\n3. Grande\n4. Salir\n")))
                if tamanoPedido == 1:
                    tamanoPedido = "Pequeno"
                elif tamanoPedido == 2:
                    tamanoPedido = "Mediano"
                elif tamanoPedido == 3:
                    tamanoPedido = "Grande"
                elif tamanoPedido == 4:
                    break
                cantPaquete = (input("Ingrese la cantidad de Paquete"))
                tamano_plus_paq += tamanoPedido + "--" + cantPaquete + ", "
            RegistroStarken = {
                "nombre" : nombreUsuario,
                "direccion" : direccionUsuario,
                "sector" : sectorUsuario,
                "paquetes" : tamano_plus_paq      
            }
            paquetesLista.append(RegistroStarken)
            opcRegistro = input("Desea ingresar otro usuario? Enter para continuar o X para salir al menu.\n ").lower()
            if opcRegistro == "":
                continue
            elif opcRegistro == "x":
                break
            
        except:
            print("Hubo un error de ingreso de datos, vuelva a intentarlo ")    

def listar_pedidos():
    contadorClientes = 1

    for elemento in paquetesLista:
        print(f"Cliente {contadorClientes}")
        print(f"=================================")
        print(f"Cliente: {elemento["nombre"]}")
        print(f"Direccion: {elemento["direccion"]}") 
        print(f"Sector: {elemento["sector"]}")
        print(f"Paquetes: {elemento["paquetes"]}")
        print(f"=================================")
        contadorClientes += 1
def imprimir_pedidos():
    sectorSelect = input("Seleccione sector de entrega. Centro/Norte/Sur: ").upper()

    with open( "pedidos.txt", "w") as archivo_txt:
        for elemento in paquetesLista:
            if sectorSelect in elemento["sector"]:
                archivo_txt.write(f"========================================\n") 
                archivo_txt.write(f"Cliente : {elemento["nombre"]}\n")
                archivo_txt.write(f"Direccion : {elemento["direccion"]}\n")
                archivo_txt.write(f"Sector : {elemento["sector"]}\n")
                archivo_txt.write(f"Paquetes : {elemento["paquetes"]}\n")
                archivo_txt.write(f"Zona Disponibilidad : {sectorSelect}\n\n")
                 



            



