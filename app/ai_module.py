def simple_ai_reply(prompt: str) -> str:
    if not prompt:
        return "No input received. Try: 'Hola, ¿cómo estás?'"

    p = prompt.lower()

    if "hola" in p:
        return "¡Hola! Soy la IA de ejemplo (coello)."

    if "ayuda" in p:
        return "Puedo darte respuestas simples. Pregunta algo :)"

    return f"Eco: {prompt[:100]} ... (respuesta generada por coello)"
