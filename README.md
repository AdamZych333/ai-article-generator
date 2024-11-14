# AI article generator
Aplikacja generująca, z użyciem AI, szablon html artykułu na podstawie tekstu.

## Wymagane

Python `3.10.0`
  ### Biblioteki
  - openai
  - dotenv

## Uruchamianie
1. Na podstawie pliku `.env-example` należy utworzyć plik `.env`. Powinina tam znajdowac się zmienna `OPENAI_API_KEY` z kluczem do API OPENAI.
2. Po uruchomieniu aplikacji wyśle się request i na podstawie odpowiedzi doda się plik `/public/artykul.html`
3. W pliku `/public/szablon.html` jest podstawa finalnego pliku html do którego doczepiany jest artykuł. Aby artykuł poprawnie się załączył do podstawy, konieczne jest postawienie pilków na serwerze lokalnym lub publicznym. Można do tego wykorzystać plugin do VS Code o nazwie `Live Server`.
4. W pliku `/public/podglad.html` jest finalna plik html z dołączonym, przykładowym, wygenerowanym artykułem.
