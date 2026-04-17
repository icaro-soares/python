primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
nésimo = primeiro_termo + (9 + 1) * razão
for c in range(primeiro_termo, nésimo, razão):
    print(c, end=' ')
