"""Hallo Docker - een klein Flask-programma voor het voorbeeldproject (VS07)."""
import os
import platform
import socket
from datetime import datetime

from flask import Flask, jsonify, render_template

VERSIE = "1.0"

app = Flask(__name__)

# Teller die bijhoudt hoe vaak de pagina is bezocht.
# Let op: deze staat in het geheugen van de container en is weg na een herstart.
bezoeken = 0


def container_info():
    """Verzamelt informatie over de computer (of container) waarop dit draait."""
    return {
        "versie": VERSIE,
        "hostnaam": socket.gethostname(),
        "python_versie": platform.python_version(),
        "besturingssysteem": f"{platform.system()} {platform.release()}",
        "processor": platform.machine(),
        "tijd": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "omgeving": os.environ.get("OMGEVING", "onbekend"),
    }


@app.route("/")
def home():
    global bezoeken
    bezoeken += 1
    return render_template("index.html", info=container_info(), bezoeken=bezoeken)


@app.route("/api/info")
def api_info():
    return jsonify(container_info() | {"bezoeken": bezoeken})


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    # 0.0.0.0 betekent: luister op alle netwerkkaarten.
    # Zonder dit is de app alleen binnen de container zelf bereikbaar.
    app.run(host="0.0.0.0", port=5000)
