import openai
import os
import random
import json
from datetime import datetime

# Nouvelle méthode pour configurer l'API
client = openai.OpenAI(api_key=os.getenv("KAAMELOTT_API"))

# Charger les plats
with open("plats.txt", "r", encoding="utf-8") as f:
    plats = [line.strip() for line in f if line.strip()]

plat_choisi = random.choice(plats)

prompt = f"Propose une manière originale et savoureuse de revisiter ce plat : {plat_choisi}. Donne une idée concrète, en 2-3 phrases maximum."

# Appel via la nouvelle interface
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Tu es un chef cuisinier créatif et professionnel."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7
)

suggestion = response.choices[0].message.content.strip()

# Sauvegarde de la suggestion
with open("suggestion.json", "w", encoding="utf-8") as f:
    json.dump({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "plat": plat_choisi,
        "suggestion": suggestion
    }, f, ensure_ascii=False, indent=2)

print(f"Suggestion générée pour : {plat_choisi}")
