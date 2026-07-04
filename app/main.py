from ai import ask_ai
from health import check_ollama

print("====================================")
print("      AI LOG EXPLAINER v1")
print("====================================")

if not check_ollama():
    print("❌ Ollama server is not running.")
    print("Start it using:")
    print("    ollama serve")
    exit()

while True:
    print()
    log = input("Paste log (or type 'exit'): ")

    if log.lower() == "exit":
        print("Goodbye!")
        break

    print("\nAnalyzing...\n")

    response = ask_ai(log)

    print("========== AI RESPONSE ==========")
    print(response)
    print("=================================")