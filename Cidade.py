class Cidade:
    def __init__(self, nome, distanciaObjetivo):
        self.visitado = False
        self.distanciaObjetivo = distanciaObjetivo
        self.nome = nome
        self.adjacentes = []

    def addCidadeAdjacente(self, cidade):
        self.adjacentes.append(cidade)

# c = Cidade("Teste")
# print(c.nome)
#%%
