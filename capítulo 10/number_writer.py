from pathlib import Path
import json


numbers = [2, 3, 5 , 7, 11]

path = Path('numbers.json')
if not path.exists():
    contents = json.dumps(numbers)
    path.write_text(contents)
else:
    path = Path('numbers.json')
    contents = path.read_text()
    numbers = json.loads(contents)
    print(numbers)

