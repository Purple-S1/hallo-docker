# Docker-basiscommando's

Overzicht van de tien basiscommando's die ik geleerd heb (leerdoel 1), met een voorbeeld en uitleg in eigen woorden.

| # | Commando | Voorbeeld | Wat doet het? |
|---|---|---|---|
| 1 | `docker pull` | `docker pull nginx` | Haalt een image op van Docker Hub en zet hem op je computer. |
| 2 | `docker images` | `docker images` | Laat alle images zien die op je computer staan. |
| 3 | `docker run` | `docker run -d -p 8081:80 --name webserver nginx` | Maakt van een image een nieuwe container en start hem. `-d` = op de achtergrond, `-p` = poort koppelen, `--name` = naam geven. |
| 4 | `docker ps` | `docker ps -a` | Laat de draaiende containers zien. Met `-a` zie je ook de gestopte containers. |
| 5 | `docker logs` | `docker logs webserver` | Laat zien wat het programma in de container heeft geschreven. Handig bij fouten. |
| 6 | `docker exec` | `docker exec -it webserver bash` | Voert een commando uit ín een draaiende container. Met `-it bash` krijg je een terminal in de container. |
| 7 | `docker stop` | `docker stop webserver` | Stopt een container. De container bestaat nog wel. |
| 8 | `docker start` | `docker start webserver` | Start een gestopte container opnieuw. |
| 9 | `docker rm` | `docker rm webserver` | Verwijdert een (gestopte) container. |
| 10 | `docker rmi` | `docker rmi nginx` | Verwijdert een image. Dat kan pas als er geen container meer van bestaat. |

## Extra commando's voor een eigen image

| Commando | Voorbeeld | Wat doet het? |
|---|---|---|
| `docker build` | `docker build -t hallo-docker:1.0 .` | Bouwt een image volgens de Dockerfile in de huidige map (`.`). `-t` geeft de image een naam en versie (tag). |
| `docker version` | `docker version` | Laat zien welke versie van Docker er draait. |

## Image of container?

- Een **image** is het bouwplan of de "bevroren" versie van een programma. Hij verandert niet.
- Een **container** is een draaiend exemplaar van een image. Van één image kun je meerdere containers starten.

Vergelijking: een image is een recept, een container is de taart die je ermee bakt.
