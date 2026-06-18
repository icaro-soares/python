from pathlib import Path


while True:
    guest = input('Digite o nome: ').title().strip()
    path = Path('guest_book.txt')
    path.write_text(guest)
    continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
