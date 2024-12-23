# Pontuação das Árvores
sabedoria = 0
inteligencia = 0
carisma = 0

print("Bem-vindo à Teoria das Árvores do Conhecimento!")
print("Responda às perguntas abaixo para descobrir de qual árvore você pertence.\n")

# Pergunta 1
print("Pergunta 1) Como você prefere tomar decisões?")
print("1) Confiando na minha intuição e sentimentos.")
print("2) Analisando cuidadosamente os fatos.")
print("3) Buscando conversar e convencer outras pessoas.")
resposta = int(input("Sua resposta: "))

if resposta == 1:
    sabedoria += 2
elif resposta == 2:
    inteligencia += 2
elif resposta == 3:
    carisma += 2
else:
    print("Entrada inválida.")

# Pergunta 2
print("\nPergunta 2) O que mais te motiva?")
print("1) Encontrar equilíbrio emocional e autoconhecimento.")
print("2) Resolver problemas complexos e aprender coisas novas.")
print("3) Liderar, inspirar e influenciar outras pessoas.")
resposta = int(input("Sua resposta: "))

if resposta == 1:
    sabedoria += 3
elif resposta == 2:
    inteligencia += 3
elif resposta == 3:
    carisma += 3
else:
    print("Entrada inválida.")

# Pergunta 3
print("\nPergunta 3) Como você costuma agir em situações de conflito?")
print("1) Procuro compreender as emoções envolvidas antes de agir.")
print("2) Tento entender a lógica do problema para encontrar uma solução.")
print("3) Busco negociar e trazer todos para um consenso.")
resposta = int(input("Sua resposta: "))

if resposta == 1:
    sabedoria += 4
elif resposta == 2:
    inteligencia += 4
elif resposta == 3:
    carisma += 4
else:
    print("Entrada inválida.")

# Pergunta 4
print("\nPergunta 4) Qual ambiente você prefere?")
print("1) Um lugar calmo e introspectivo para reflexão.")
print("2) Um espaço cheio de livros e ferramentas para aprender.")
print("3) Um ambiente social onde posso interagir com muitas pessoas.")
resposta = int(input("Sua resposta: "))

if resposta == 1:
    sabedoria += 2
elif resposta == 2:
    inteligencia += 2
elif resposta == 3:
    carisma += 2
else:
    print("Entrada inválida.")

# Pontuação final
print("\nPontuação Final:")
print(f"Sabedoria: {sabedoria}")
print(f"Inteligência: {inteligencia}")
print(f"Carisma: {carisma}")

# Determinar a árvore predominante
arvores = {
    "Sabedoria": sabedoria,
    "Inteligência": inteligencia,
    "Carisma": carisma
}

arvore_predominante = max(arvores, key=arvores.get)
print(f"\nVocê pertence à Árvore da {arvore_predominante}!")
