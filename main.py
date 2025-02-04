# =============================================================================
# Aktivierung und Deaktivierung der virtuellen Umgebung:
# -----------------------------------------------------------------------------
# Um die virtuelle Umgebung zu aktivieren, öffne das Terminal und führe aus:
#     .\chatbot\Scripts\activate
#
# Um die virtuelle Umgebung zu verlassen, gib im Terminal ein:
#     deactivate
# =============================================================================

# -----------------------------------------------------------------------------
# Importieren der benötigten Module:
# -----------------------------------------------------------------------------
# - OllamaLLM: Stellt die Schnittstelle zum Sprachmodell (hier "llama3") bereit.
# - ChatPromptTemplate: Erlaubt das Erstellen von Vorlagen (Templates) für Chat-Eingaben.
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# -----------------------------------------------------------------------------
# Definition des Prompt-Templates:
# -----------------------------------------------------------------------------
# Das Template bestimmt, wie die Eingaben (z. B. der bisherige Gesprächsverlauf 
# und die aktuelle Frage) in den Prompt eingebunden werden.
template = """
Answer the question below.

Here ist the conversation history: {context}

Question: {question}

Answer:
"""

# -----------------------------------------------------------------------------
# Initialisierung des Sprachmodells:
# -----------------------------------------------------------------------------
# Erstellen einer Instanz des Sprachmodells "llama3" mithilfe der OllamaLLM-Klasse.
model = OllamaLLM(model="llama3")

# -----------------------------------------------------------------------------
# Erstellen des ChatPromptTemplates:
# -----------------------------------------------------------------------------
# Das Template wird in ein ChatPromptTemplate-Objekt umgewandelt, das später 
# zur Formulierung des endgültigen Prompts genutzt wird.
prompt = ChatPromptTemplate.from_template(template)

# -----------------------------------------------------------------------------
# Kombinieren von Prompt und Modell:
# -----------------------------------------------------------------------------
# Durch den "Pipe-Operator" (|) werden prompt und model zu einer sogenannten "Chain"
# verbunden, die den erstellten Prompt an das Modell übergibt.
chain = prompt | model

# -----------------------------------------------------------------------------
# Definition der Funktion zur Handhabung des Gesprächsverlaufs:
# -----------------------------------------------------------------------------
def handle_conversation():
    # Initialisieren des Kontexts (Gesprächsverlaufs), zunächst leer.
    context = ""
    # Ausgabe einer Begrüßungsnachricht an den Benutzer.
    print("Welcome to the AI ChatBot! Type 'exit' to quit.")
    
    # Endlosschleife, die das fortlaufende Gespräch steuert.
    while True:
        # Abfrage der Benutzereingabe.
        user_input = input("You: ")
        
        # Überprüfen, ob der Benutzer das Gespräch beenden möchte.
        if user_input.lower() == "exit":
            break

        # -----------------------------------------------------------------------------
        # Übergabe der Eingabe an das Modell:
        # -----------------------------------------------------------------------------
        # Die Chain erhält als Input ein Dictionary mit:
        # - 'context': Den bisherigen Gesprächsverlauf.
        # - 'question': Die aktuelle Frage bzw. Eingabe des Benutzers.
        # Das Modell liefert als Antwort einen Text, der in 'result' gespeichert wird.
        result = chain.invoke({"context": context, "question": user_input})
        
        # -----------------------------------------------------------------------------
        # Ausgabe der Antwort:
        # -----------------------------------------------------------------------------
        # Die vom Modell generierte Antwort wird an den Benutzer ausgegeben.
        print("Bot: ", result)
        
        # -----------------------------------------------------------------------------
        # Aktualisieren des Gesprächsverlaufs:
        # -----------------------------------------------------------------------------
        # Die Benutzereingabe und die Modellantwort werden zum bisherigen Kontext hinzugefügt.
        context += f"\nUser: {user_input}\nAI: {result}"

# -----------------------------------------------------------------------------
# Programmstart:
# -----------------------------------------------------------------------------
# Wenn das Skript direkt ausgeführt wird (nicht importiert), wird die Chat-Funktion gestartet.
if __name__ == "__main__":
    handle_conversation()
