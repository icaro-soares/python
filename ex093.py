ficha = {}
tot = []
ficha['nome'] = str(input('Nome jogador: '))
jogos = int(input(f'Quantos jogos {ficha['nome']} jogou? '))
for c in range(0, jogos):
    gol = int(input(f'Quantidade do gols no jogo {c}: '))
    tot.append(gol)
print('-='*30)
print(ficha, jogos)
