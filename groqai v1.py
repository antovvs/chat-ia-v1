from groq import Groq

# ================= CONFIGURATION =================
client = Groq(api_key="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")  # ← Ta clé

# Liste qui garde l'historique de la conversation
messages = [
    {"role": "system", "content": "Tu es un assistant utile, amical et parlant en français."}
]

print("🤖 Chat Groq démarré ! (tape 'quit' pour arrêter)\n")

while True:
    # Demande à l'utilisateur
    user_input = input("👤 Toi : ")
    
    # Pour quitter
    if user_input.lower() in ["quit", "q", "exit", "bye"]:
        print("👋 Au revoir !")
        break
    
    # Ajoute le message de l'utilisateur à l'historique
    messages.append({"role": "user", "content": user_input})
    
    # Envoie la requête à Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=800
    )
    
    # Récupère la réponse
    assistant_reply = response.choices[0].message.content
    
    # Affiche la réponse
    print(f"🤖 Groq : {assistant_reply}\n")
    
    # Ajoute la réponse de l'IA à l'historique
    messages.append({"role": "assistant", "content": assistant_reply})
