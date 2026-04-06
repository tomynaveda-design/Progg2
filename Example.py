
class Profesor:
    def __init__(self, nombre, materia, curso):
        self.nombre = nombre
        self.materia = materia
        self.curso = curso


    def saludar(self):
        return f"Hola Developers, {self.nombre}"
    
profe_uno = Profesor("Pepe","Programación", "Prog2")

print(profe_uno.saludar())


profe_dos = Profesor("Ana", "base de datos", "Prog3")

print(profe_dos.saludar())













