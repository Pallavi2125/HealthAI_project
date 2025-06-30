# ================== Medical Knowledge Base ==================

DISEASES = {
    "flu": {
        "symptoms": ["fever", "jwaraṁ", "cough", "dummu", "fatigue", "ālasyam", "headache", "talanooppi", "cold", "jukkam"],
        "remedies": ["Rest", "Drink warm fluids", "Use paracetamol"],
        "tip": "Avoid cold drinks. Stay isolated if coughing.",
        "alert": ""
    },
    "cold": {
        "symptoms": ["cold", "jukkam", "sneezing", "tummadam", "runny nose", "mookajalam", "cough", "mild fever", "thakkuva jwaram"],
        "remedies": ["Steam inhalation", "Vitamin C-rich foods", "Stay hydrated"],
        "tip": "Keep warm and avoid dusty environments.",
        "alert": ""
    },
    "dengue": {
        "symptoms": ["fever", "rash", "headache", "joint pain", "low platelet count", "platelet thaggadam", "body pain", "sarīra vedana"],
        "remedies": ["Papaya leaf juice", "Plenty of fluids", "Avoid aspirin"],
        "tip": "Monitor platelet count daily and avoid dehydration.",
        "alert": "🚨 Seek immediate medical attention if fever worsens or bleeding occurs."
    },
    "malaria": {
        "symptoms": ["fever", "chills", "sweating", "vomiting", "muscle pain", "kaalu noppi", "gontuka vedana"],
        "remedies": ["Antimalarial medication", "Rest", "Stay hydrated", "Use mosquito nets"],
        "tip": "Get a blood test immediately for confirmation.",
        "alert": "🚨 Consult a physician urgently to avoid complications."
    },
    "typhoid": {
        "symptoms": ["high fever", "abdominal pain", "constipation", "fatigue", "loss of appetite", "jeevana ichcha lēkapōvadam"],
        "remedies": ["Antibiotics", "Boiled water", "Soft foods", "Oral rehydration"],
        "tip": "Do not self-medicate. Maintain hygiene.",
        "alert": "🚨 Go to hospital if fever worsens."
    },
    "covid-19": {
        "symptoms": ["fever", "dry cough", "breathing difficulty", "loss of smell", "tiredness", "śvāsakaṣṭaṁ", "gandha grahaṇa abhāvaṁ"],
        "remedies": ["Isolation", "Paracetamol", "Steam inhalation", "Hydration"],
        "tip": "Wear a mask and isolate.",
        "alert": "🚨 Visit a COVID clinic if symptoms increase."
    },
    "asthma": {
        "symptoms": ["shortness of breath", "wheezing", "chest tightness", "coughing", "śvāsa kāṣṭaṁ", "urake gattiga padadam"],
        "remedies": ["Inhaler use", "Avoid allergens", "Practice breathing exercises"],
        "tip": "Carry your inhaler. Avoid smoke and dust.",
        "alert": "🚨 Seek emergency care during severe asthma attack."
    },
    "migraine": {
        "symptoms": ["headache", "nausea", "sensitivity to light", "blurred vision", "talanooppi", "akkaḷi"],
        "remedies": ["Pain relievers", "Lie in a dark room", "Cold compress"],
        "tip": "Avoid stress and screen exposure.",
        "alert": ""
    },
    "pneumonia": {
        "symptoms": ["cough with phlegm", "chest pain", "fever", "shortness of breath", "śvāsakaṣṭaṁ"],
        "remedies": ["Antibiotics", "Warm fluids", "Rest"],
        "tip": "Medical imaging required if persistent.",
        "alert": "🚨 Hospital care may be required in severe cases."
    },
    "diarrhea": {
        "symptoms": ["loose motions", "gastric", "stomach cramps", "loose motion", "vēgamainaviṣṭam"],
        "remedies": ["ORS solution", "Plenty of water", "Banana & rice"],
        "tip": "Avoid spicy food. Use boiled water.",
        "alert": "🚨 See a doctor if symptoms persist over 2 days."
    },
    "jaundice": {
        "symptoms": ["yellow eyes", "skin yellowing", "dark urine", "vomiting", "jaundice", "pasupu kālu", "kallalo pasupu"],
        "remedies": ["Rest", "Coconut water", "Avoid oily food"],
        "tip": "Get liver function test done.",
        "alert": "🚨 Requires blood test and medical supervision."
    }
}

# ================== Disease Prediction Function ==================

def get_disease_predictions(user_symptoms):
    predictions = []
    user_symptoms = [s.strip().lower() for s in user_symptoms if s.strip()]

    if not user_symptoms:
        return []

    for disease, info in DISEASES.items():
        disease_symptoms = [s.lower() for s in info["symptoms"]]
        match_count = sum(1 for symptom in user_symptoms if any(symptom in ds for ds in disease_symptoms))
        total = len(disease_symptoms)
        if match_count > 0:
            score = int((match_count / total) * 100)
            predictions.append({
                "Disease": disease.capitalize(),
                "Confidence": f"{score}%",
                "Remedies": info["remedies"],
                "Tip": info["tip"],
                "Alert": info["alert"]
            })

    predictions.sort(key=lambda x: int(x["Confidence"].strip('%')), reverse=True)
    return predictions