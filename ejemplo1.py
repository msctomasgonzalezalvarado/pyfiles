#Esto es un comentario

#Esto es una clase
class Auto:
    marca = "VW" #Atributo dentro de la clase
    modelo = 1000 #Aributo
    placa = "FGJJ255" #Atributo

    def metodo_publico(selft):
        print("Este es un método público");

    def autoavanza(selft):
            print("El auto está avanzando")

#se instancía un objeto
taxi = Auto()

print("Taxi 456 modelo {} con placa {}".format(taxi.modelo, taxi.placa))
taxi.metodo_publico()
taxi.autoavanza()