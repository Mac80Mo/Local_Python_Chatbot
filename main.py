#.\chatbot\Scripts\activate
from langchain_ollama import OllamaLLM

# Modell initialisieren
model = OllamaLLM(model="llama3")

# Eingabe an das Modell
result = model.invoke(input="Hello World")

# Ergebnis ausgeben
print(result)
