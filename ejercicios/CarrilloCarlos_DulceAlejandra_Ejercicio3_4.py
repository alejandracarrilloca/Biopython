"""
Dulce Alejandra Carrillo Carlos 
BioPython (2026-1)
22 de agosto del 2025 

Instrucción: 
-   3: Usando el concepto de Herencia, realicen una subclase de la clase gen, 
    llamada tRNA, y otra clase llamada RNA no codificante.  Luego deriva de tRNA otra 
    subclase llamada proteina.

-   4: Genera una función longitud para la clase tRNA y una función longitud 
    para la clase proteína.  La primera regresa el numero de nucleótidos, la segunda, 
    el número de nucleótidos y de aminoácidos.
"""

class Gen:
    def __init__(self):
        self.secuencia = ""
        self.total_gc = 0
        self.rna = ""
        self.inicio = False

    def input_secuencia(self):
        self.secuencia = input("Introduce la secuencia de DNA:  ").upper()

    def porcentaje_GC(self):
        if len(self.secuencia) > 0:
            self.total_gc = ((self.secuencia.count("G") + self.secuencia.count("C")) / len(self.secuencia)) * 100

    def transcripcion(self):
        trans_nucleotidos = {"A": "U", "T": "A", "G": "C", "C": "G"}
        self.rna = "".join(trans_nucleotidos.get(base, "") for base in self.secuencia)

    def codon_inicio(self):
        self.inicio = "ATG" in self.secuencia


# Subclase tRNA
class tRNA(Gen):
    def longitud(self):
        return len(self.rna) 


# Subclase RNA no codificante
class NC_Rna(Gen):
    pass


# Subclase Proteína derivada de tRNA
class Proteina(tRNA):
    def __init__(self):
        super().__init__()
        self.aminoacidos = []

    def traduccion(self):
        codigo_genetico = {
            "F": ["UUU", "UUC"],
            "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
            "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
            "Y": ["UAU", "UAC"],
            "*": ["UAA", "UAG", "UGA"],  # Codon de paro
            "C": ["UGU", "UGC"],
            "W": ["UGG"],
            "P": ["CCU", "CCC", "CCA", "CCG"],
            "H": ["CAU", "CAC"],
            "Q": ["CAA", "CAG"],
            "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
            "I": ["AUU", "AUC", "AUA"],
            "M": ["AUG"],
            "T": ["ACU", "ACC", "ACA", "ACG"],
            "N": ["AAU", "AAC"],
            "K": ["AAA", "AAG"],
            "V": ["GUU", "GUC", "GUA", "GUG"],
            "A": ["GCU", "GCC", "GCA", "GCG"],
            "D": ["GAU", "GAC"],
            "E": ["GAA", "GAG"],
            "G": ["GGU", "GGC", "GGA", "GGG"]
        }

        self.aminoacidos = []
        for i in range(0, len(self.rna) - 2, 3):
            codon = self.rna[i:i+3]
            for aa, codones in codigo_genetico.items():
                if codon in codones:
                    if aa == "*":  # codón de paro
                        return
                    self.aminoacidos.append(aa)
                    break

    def longitud(self):
        return len(self.rna), len(self.aminoacidos)


araC = Gen()
araC.input_secuencia()
araC.porcentaje_GC()
araC.transcripcion()
araC.codon_inicio()

print(f"Contenido de GC: {araC.total_gc:.2f}%")
print(f"Transcripción: {araC.rna}")
print("Contiene codón de inicio: Sí" if araC.inicio else "No contiene codón de inicio")

# tRNA
trna = tRNA()
trna.secuencia = araC.secuencia
trna.transcripcion()
print(f"Longitud de tRNA: {trna.longitud()} nucleótidos")

# Proteína
prot = Proteina()
prot.secuencia = araC.secuencia
prot.transcripcion()
prot.traduccion()
print(f"Longitud de Proteína: {prot.longitud()[0]} nucleótidos, {prot.longitud()[1]} aminoácidos")
print(f"Aminoácidos: {''.join(prot.aminoacidos)}")
