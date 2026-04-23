import json
import random
from datetime import datetime

def carregar_perguntas(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        perguntas = json.load(f)
        return perguntas

def mostrar_historico():
    try:
        with open('historico.json', 'r', encoding='utf-8') as f:
            historico = json.load(f)
        print("\n===== HISTÓRICO DE RESULTADOS =====")
        for registro in historico:
            print(f"Data: {registro['data']}, Acertos: {registro['acertos']} de {registro['total']}")
        print("====================================\n")
    except FileNotFoundError:
        print("\nAinda não há histórico salvo!\n")

def salvar_historico(acertos, total):
    registro = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "acertos": acertos,
        "total": total
    } 
    try:
        with open('historico.json', 'r', encoding='utf-8') as f:
            historico = json.load(f)
    except FileNotFoundError:
        historico = []
    historico.append(registro)
    with open('historico.json', 'w', encoding='utf-8') as f:
        json.dump(historico, f, indent=4, ensure_ascii=False)
        print("📁 Resultado salvo no histórico!")

def jogar_quiz():
    perguntas = carregar_perguntas('Perguntas_Python.json')
    random.shuffle(perguntas)
    acertos = 0
    for pergunta in perguntas:
        print(pergunta['pergunta'])
        for alternativa in pergunta['alternativas']:
            print(alternativa)
        resposta = input("\nSua resposta: ").upper().strip()
        if resposta == pergunta['resposta']:
             print("✅ Correto!\n")
             acertos += 1
        else:
            print(f"❌ Errado! A resposta correta era: {pergunta['resposta']}\n")
    print(f"Resultado final: {acertos} de {len(perguntas)} acertos")
    salvar_historico(acertos, len(perguntas))
    print(f"Resultado final: {acertos} de {len(perguntas)} acertos")

# Loop principal do quiz
while True:
    print("\nMenu do Quiz: Perguntas_Python")
    print("  [Q] - Iniciar o quiz")
    print("  [H] - Ver o histórico")
    print("  [S] - Sair\n")
    escolha = input("Escolha uma opção: ").strip().upper()
    if escolha == 'Q':
        jogar_quiz()
    elif escolha == 'H':
        mostrar_historico()
    elif escolha == 'S':
        print("Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")

