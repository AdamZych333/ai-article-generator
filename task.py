from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def read_input(file_name):
  with open(file_name, 'r') as file:
      lines = file.readlines()
  return '\n'.join([line.strip() for line in lines])

def generate_output(prompt, text):
  openai_prompt = prompt + text
  print(openai_prompt)
  response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": openai_prompt}])

  return response.choices[0].message.content

task_prompt = """
  Stwórz podstawową strukturę HTML dla artykułu, która będzie czytelna i semantyczna.
  Priorytetyzuj:
  Semantykę - użyj odpowiednich tagów do podziału tekstu np. <section>, <article>, <footer>, <h1>, <h2>, <p>.
  Kompletność - upewnij się, że struktura zawiera całość artykułu i nie ma dodatkowej treści.

  Dodatkowe instrukcje:
  Popraw polskie znaki w tekście.
  Najkrótsze linie z tekstu to tagi <h1> lub <h2> i każdy z nich ma swoją sekcję. Nie dodawaj innych sekcji poza nimi.
  W <footer> powinien być tylko jeden tag <p> zawierający ostatnią linijkę tekstu zaczynającą się od znaku '*'.
  Do każdej sekcji wstaw <img src="placeholder.png"> pasujące do tematu sekcji. Opis w atrybucie alt powinien być szczegółowy i precyzyjny, aby mógł służyć jako prompt do generowania grafiki.

  Oczekiwany wynik:
  Kod HTML, który będzie zawierał tylko zawartość pomiędzy tagu <body>, ale bez niego. Pomiń JavaScript i CSS.

  Artykuł:
"""
task_text = read_input('input.txt')

output = generate_output(task_prompt, task_text)
print(output)