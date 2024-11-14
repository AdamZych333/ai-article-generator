from openai import OpenAI
from dotenv import load_dotenv
import re

load_dotenv()
client = OpenAI()

def read_input(file_name):
  with open(file_name, 'r') as file:
      lines = file.readlines()
  return '\n'.join([line.strip() for line in lines])

def generate_output(prompt, text):
  openai_prompt = prompt + text
  response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": openai_prompt}])

  return response.choices[0].message.content

def write_output(output):
    pattern = r"```html\n(.*?)\n```"
    matches = re.findall(pattern, output, re.DOTALL)
    html = matches[0]

    with open('public/artykul.html', 'w') as file:
        file.write(html)

task_prompt = """
Zadanie:
Najpierw znajdź i popraw błędnie zapisane polskie znaki w tekście artykułu. Na podstawie tego tekstu stwórz strukturę HTML dla artykułu, która będzie czytelna i semantyczna.

Priorytetyzuj:
Semantykę - użyj odpowiednich tagów do podziału tekstu np. <section>, <article>, <footer>, <h1>, <h2>, <p>.
Kompletność - struktura MUSI zawierać całość artykułu i nie powinna mieć dodatkowej treści.

Dodatkowe instrukcje:
Najkrótsze linie z tekstu to tagi <h1> lub <h2> i każdy z nich ma swoją sekcję. Nie dodawaj innych sekcji poza nimi. Jedna sekcja może mieć kilka tagów <p>.
Do każdej sekcji wstaw <img src="placeholder.png"> pasujące do tematu sekcji. Opis w atrybucie alt powinien być szczegółowy i precyzyjny, aby mógł służyć jako prompt do generowania grafiki.

Oczekiwany wynik:
Kod HTML, który będzie zawierał tylko zawartość pomiędzy tagu <body>, ale bez niego. Pomiń JavaScript i CSS.

Artykuł:
"""
task_text = read_input('input.txt')

task_output = generate_output(task_prompt, task_text)

write_output(task_output)