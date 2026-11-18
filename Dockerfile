# 1. Basis-image: een kleine Linux met Python 3.12 erop
FROM python:3.12-slim

# 2. Map in de container waar het programma komt te staan
WORKDIR /app

# 3. Eerst alleen de lijst met benodigdheden kopiëren en installeren.
#    Docker onthoudt deze stap (cache), zodat hij niet opnieuw hoeft als alleen de code verandert.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Daarna de rest van de code kopiëren
COPY . .

# 5. Een omgevingsvariabele die het programma kan uitlezen
ENV OMGEVING=docker

# 6. Veiligheid: draai het programma niet als 'root' maar als een gewone gebruiker
RUN useradd --create-home appgebruiker
USER appgebruiker

# 7. Vastleggen dat de app op poort 5000 luistert
EXPOSE 5000

# 8. Het commando dat uitgevoerd wordt als de container start
CMD ["python", "app.py"]
