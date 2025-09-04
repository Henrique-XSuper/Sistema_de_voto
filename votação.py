import random

candidatos = {}
print("=== SISTEMA DE VOTAÇÃO ===")
print("Cadastre os candidatos (mínimo 2). Digite 'L' para iniciar a votação.\n")

codigo = 1
while True:
    nome = input(f"Digite o nome do candidato {codigo} ou 'L' para iniciar a votação: ").strip()
    if nome.upper() == 'L':
        if len(candidatos) >= 2:
            break
        else:
            print("Você precisa cadastrar pelo menos 2 candidatos antes de iniciar a votação.")
            continue
    elif nome == "" or nome.isdigit():
        print("Nome inválido. Não pode ser vazio nem apenas números. Tente novamente.")
    else:
        candidatos[codigo] = {"nome": nome, "votos": 0}
        codigo += 1

print("\n=== CANDIDATOS CADASTRADOS ===")
for cod, info in candidatos.items():
    print(f"{cod} - {info['nome']}")

print("\nDigite o número do candidato para votar ou 0 para encerrar a votação.")


while True:
    try:
        voto = int(input("Seu voto: "))
        if voto == 0:
            print("\nVotação encerrada!\n")
            break
        elif voto in candidatos:
            candidatos[voto]["votos"] += 1
            print(f"Voto registrado para {candidatos[voto]['nome']}!")
        else:
            print("Código inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")

print("\n=== RESULTADO FINAL ===")
for info in candidatos.values():
    print(f"{info['nome']}: {info['votos']} votos")

maior_voto = max(candidatos.values(), key=lambda x: x["votos"])["votos"]
empatados = [info for info in candidatos.values() if info["votos"] == maior_voto]

if len(empatados) == 1:
    print(f"\n🏆 Vencedor: {empatados[0]['nome']} com {maior_voto} votos!")
else:
    print("\n⚠️ Empate detectado! Iniciando segundo turno entre os empatados:")
    segundo_turno = {i+1: {"nome": c["nome"], "votos": 0} for i, c in enumerate(empatados)}

    for cod, info in segundo_turno.items():
        print(f"{cod} - {info['nome']}")

    print("\nDigite o número do candidato para votar no segundo turno ou 0 para encerrar.")

   
    while True:
        try:
            voto = int(input("Seu voto (2º turno): "))
            if voto == 0:
                print("\nSegundo turno encerrado!\n")
                break
            elif voto in segundo_turno:
                segundo_turno[voto]["votos"] += 1
                print(f"Voto registrado para {segundo_turno[voto]['nome']}!")
            else:
                print("Código inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    maior_voto_2 = max(segundo_turno.values(), key=lambda x: x["votos"])["votos"]
    empatados_2 = [info for info in segundo_turno.values() if info["votos"] == maior_voto_2]

    if len(empatados_2) == 1:
        print(f"\n🏆 Vencedor do segundo turno: {empatados_2[0]['nome']} com {maior_voto_2} votos!")
    else:
        print("\n⚠️ Novo empate!")

        if len(empatados_2) == 2:
            print("Desempate por cara ou coroa!")
            nome1 = empatados_2[0]['nome']
            nome2 = empatados_2[1]['nome']

            escolha1 = input(f"{nome1}, escolha 'cara' ou 'coroa': ").strip().lower()
            while escolha1 not in ['cara', 'coroa']:
                escolha1 = input("Escolha inválida. Digite 'cara' ou 'coroa': ").strip().lower()

            escolha2 = 'coroa' if escolha1 == 'cara' else 'cara'
            print(f"{nome2} ficou com '{escolha2}'.")

            resultado_moeda = random.choice(['cara', 'coroa'])
            print(f"\n🪙 Resultado do sorteio: {resultado_moeda.upper()}")

            vencedor = nome1 if escolha1 == resultado_moeda else nome2
            print(f"🏆 Vencedor por sorteio: {vencedor}")

        else:
            print("Desempate por número aleatório!")
            sorteios = {}
            for candidato in empatados_2:
                numero = random.randint(1, 100)
                sorteios[candidato['nome']] = numero
                print(f"{candidato['nome']} tirou o número {numero}")

            vencedor_nome = max(sorteios, key=sorteios.get)
