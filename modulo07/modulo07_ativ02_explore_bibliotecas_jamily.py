from datetime import datetime, time
from faker import Faker

fake = Faker("pt_BR")

print("=" * 40)
print("       SISTEMA DE PROVA")
print("=" * 40)

# Dados gerados pelo Faker
nome_avaliador = fake.name()
professor = fake.name()

print(f"\nAvaliador: {nome_avaliador}")
print(f"Professor: {professor}")

# Data e hora
agora = datetime.now()
horario_prova = time(13, 15)

print(f"Data da prova: {agora.strftime('%d/%m/%Y')}")
print(f"Horário da prova: 13:15")
print(f"Horário atual: {agora.strftime('%H:%M')}")

# Verificação do horário
hora_atual = agora.time().replace(second=0, microsecond=0)

if hora_atual < horario_prova:
    print("Status: ADIANTADO")
elif hora_atual > horario_prova:
    print("Status: ATRASADO")
else:
    print("Status: NO HORÁRIO")

# Perguntas
perguntas = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "alternativas": ["A) São Paulo", "B) Brasília", "C) Salvador", "D) Recife"],
        "resposta": "B"
    },
    {
        "pergunta": "Quanto é 5 + 5?",
        "alternativas": ["A) 8", "B) 9", "C) 10", "D) 11"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual planeta é conhecido como Planeta Vermelho?",
        "alternativas": ["A) Terra", "B) Vênus", "C) Marte", "D) Júpiter"],
        "resposta": "C"
    }
]

# Sistema de pontos
pontos = 0

print("\n========== PROVA ==========")

for i, questao in enumerate(perguntas, 1):
    print(f"\nQuestão {i}: {questao['pergunta']}")

    for alternativa in questao["alternativas"]:
        print(alternativa)

    resposta = input("Sua resposta: ").upper()

    if resposta == questao["resposta"]:
        print("✓ Resposta correta!")
        pontos += 1
    else:
        print("✗ Resposta incorreta!")

# Resultado
media = pontos / len(perguntas) * 10

print("\n========== RESULTADO ==========")
print(f"Pontuação: {pontos}/{len(perguntas)}")
print(f"Média: {media:.1f}")

if media >= 6:
    print("Resultado: APROVADO!")
else:
    print("Resultado: REPROVADO!")

print("\nObrigado por realizar a prova!")