from pathlib import Path
import json


número_favorito = int(input('Qual seu número favorito: '))
path = Path('número_favorito.json')
contents = json.dumps(número_favorito)
path.write_text(contents)
print(contents)