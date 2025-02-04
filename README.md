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

Der ChatBot ermöglicht es, in einem fortlaufenden Gespräch Fragen zu stellen und Antworten vom AI-Modell zu erhalten. Der bisherige Gesprächsverlauf wird gespeichert und als Kontext an das Modell übergeben, um konsistente Antworten zu generieren.

## Features

- **Interaktiver Chat:** Nutze den Chatbot in der Kommandozeile.
- **Gesprächsverlauf:** Der bisherige Verlauf wird gespeichert und in zukünftigen Anfragen berücksichtigt.
- **Einfache Einrichtung:** Mit virtueller Umgebung und klaren Setup-Anweisungen.

## Voraussetzungen

- Python 3.6 oder höher
- Eine funktionierende Installation der folgenden Module:
  - `langchain_ollama`
  - `langchain_core`

## Installation

### Virtuelle Umgebung

Um sicherzustellen, dass alle benötigten Abhängigkeiten isoliert installiert werden, wird empfohlen, eine virtuelle Umgebung zu nutzen.

**Aktivieren der virtuellen Umgebung:**

Unter Windows:
```bash
.\chatbot\Scripts\activate
