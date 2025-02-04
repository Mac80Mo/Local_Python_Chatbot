# AI ChatBot mit OllamaLLM

Dieses Repository enthält einen einfachen AI-Chatbot, der in Python entwickelt wurde. Der Chatbot verwendet das Sprachmodell **llama3** über die [OllamaLLM](https://github.com/ollama/ollama-python) Schnittstelle und nutzt [LangChain](https://github.com/hwchase17/langchain) zur Verwaltung von Prompt-Templates und Modellinteraktionen.

## Inhaltsverzeichnis

- [Über das Projekt](#über-das-projekt)
- [Features](#features)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
  - [Virtuelle Umgebung](#virtuelle-umgebung)
  - [Abhängigkeiten installieren](#abhängigkeiten-installieren)
- [Verwendung](#verwendung)
- [Code-Übersicht](#code-übersicht)
- [Anpassung](#anpassung)
- [Lizenz](#lizenz)

## Über das Projekt

Dieses Projekt ist mein erster Kontakt mit **OllamaLLM** und stellt einen **lokalen Chatbot** auf Grundlage des Sprachmodells **llama3** dar. Der ChatBot ermöglicht es, in einem fortlaufenden Gespräch Fragen zu stellen und Antworten vom AI-Modell zu erhalten. Der bisherige Gesprächsverlauf wird gespeichert und als Kontext an das Modell übergeben, um konsistente Antworten zu generieren.

## Features

- **Interaktiver Chat:** Nutze den Chatbot in der Kommandozeile.
- **Gesprächsverlauf:** Der bisherige Verlauf wird gespeichert und in zukünftigen Anfragen berücksichtigt.
- **Einfache Einrichtung:** Mit virtueller Umgebung und klaren Setup-Anweisungen.
- **Lokal ausführbar:** Kein externer API-Zugriff notwendig – alle Berechnungen laufen lokal auf deinem Gerät.

## Voraussetzungen

- Python 3.6 oder höher
- Eine funktionierende Installation der folgenden Module:
  - `langchain_ollama`
  - `langchain_core`
  - `ollama`

## Installation

### Virtuelle Umgebung

Um sicherzustellen, dass alle benötigten Abhängigkeiten isoliert installiert werden, wird empfohlen, eine virtuelle Umgebung zu nutzen.

**Erstellen und Aktivieren der virtuellen Umgebung:**

Unter Windows:
```bash
python -m venv chatbot          # Erstellen
.\chatbot\Scripts\activate      # Aktivieren
```

Unter Linux/macOS:
```bash
python3 -m venv chatbot
source chatbot/bin/activate
```

### Abhängigkeiten installieren

```bash
pip install langchain_ollama langchain_core ollama
```

## Verwendung

Nach der erfolgreichen Installation kann der Chatbot über die Kommandozeile gestartet werden:

```bash
python main.py
```

Anschließend kannst du in einem interaktiven Dialog mit dem AI-Modell **llama3** chatten.

## Code-Übersicht

- **`main.py`** – Hauptskript zum Starten des Chatbots
- **`requirements.txt`** – Enthält die benötigten Abhängigkeiten
- **`README.md`** – Diese Dokumentation

## Anpassung

Falls du den Chatbot weiter anpassen möchtest, kannst du:
- Die Prompt-Vorlagen in `chatbot.py` verändern
- Den Speichermechanismus für den Gesprächsverlauf erweitern oder anpassen
- Weitere Features hinzufügen, wie z. B. eine GUI oder eine API-Schnittstelle

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz veröffentlicht. Weitere Details findest du in der Datei `LICENSE`.

---

Falls du Fragen oder Anregungen hast, freue ich mich über Feedback!

