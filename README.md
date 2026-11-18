# Hallo Docker 🐳

Voorbeeldproject voor het keuzedeel *Verdieping software* (VS07) van Sven Teuben.

Een klein Python-webprogramma (Flask) dat in een Docker-container draait. De pagina laat zien op welke "computer" het programma draait: de hostnaam van de container, het besturingssysteem, de Python-versie en hoe vaak de pagina is bezocht.

## Wat heb je nodig?

- Docker Desktop
- Git (alleen om de code op te halen)

Python hoef je **niet** zelf te installeren: dat zit in de container.

## Starten

```bash
docker build -t hallo-docker:1.0 .
docker run -d -p 8080:5000 --name hallo hallo-docker:1.0
```

Open daarna <http://localhost:8080> in je browser.

## Stoppen en opruimen

```bash
docker stop hallo
docker rm hallo
```

## Adressen

| Adres | Wat je ziet |
|---|---|
| `/` | De homepagina met informatie over de container |
| `/api/info` | Dezelfde informatie als JSON |
| `/health` | `{"status": "ok"}` als het programma draait |

## Mappenstructuur

```
hallo-docker/
├── app.py              # Het Python-programma (Flask)
├── requirements.txt    # Welke Python-pakketten nodig zijn
├── templates/
│   └── index.html      # De HTML-pagina
├── static/
│   └── style.css       # De opmaak
├── Dockerfile          # Het bouwplan voor de image
├── .dockerignore       # Bestanden die niet in de image horen
├── .gitignore          # Bestanden die niet in Git horen
└── COMMANDOS.md        # Overzicht van de Docker-basiscommando's
```

## Poort 8080 in plaats van 5000

In de container luistert de app op poort 5000. Op een Mac is poort 5000 al bezet door AirPlay, daarom koppelen we hem aan poort **8080** op de laptop (`-p 8080:5000`).
