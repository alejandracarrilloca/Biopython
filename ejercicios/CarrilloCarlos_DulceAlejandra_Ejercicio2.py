"""
Dulce Alejandra Carrillo Carlos 
BioPython (2026-1)
13 de agosto del 2025 

Instrucción: 
Generar una clase en Python de un gen que cuente con:
    - 3 atributos
    - 3 métodos (contando el constructor)
"""

class Gen:
    def __init__(self):
        self.secuencia = ""
        self.total_gc = 0
        self.rna = ""
        self.inicio = False

    def input_secuencia(self):
        #Pide al usuario ingresar la secuencia
        self.secuencia = input("Introduce la secuencia de DNA: ").upper()

    def porcentaje_GC(self):
        #Calcula el contenido de GC en porcentaje.
        self.total_gc = (self.secuencia.count("G") + self.secuencia.count("C"))/100

    def transcripcion(self):
        #Realiza la transcripción DNA a RNA
        self.rna = self.secuencia.replace("T", "U")

    def codon_inicio(self):
        #Verifica si la secuencia contiene el codón de inicio ATG.
        self.inicio = self.secuencia.find("ATG") >= 0


araC = Gen()
araC.input_secuencia()
araC.porcentaje_GC()
araC.transcripcion()
araC.codon_inicio()

print(f"Contenido de GC: ({araC.total_gc:.2f}%)")
print(f"Transcripción: {araC.rna}")
print("Contiene codón de inicio: Sí" if araC.inicio else "No contiene codón de inicio")
