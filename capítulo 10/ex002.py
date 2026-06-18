from pathlib import Path

nome = input('Digite seu nome: ').title().strip()
path = Path('guests.txt')
path.write_text(nome)
