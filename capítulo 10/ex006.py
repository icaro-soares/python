from pathlib import Path


cat = Path('cats.txt')
dog = Path('dogs.txt')
content = cat.read_text(encoding='utf-8')
text = dog.read_text(encoding='utf-8')
print(content)
print(text)
