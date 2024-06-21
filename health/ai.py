from transformers import pipeline

nlp_model = pipeline('question-answering')

def interpret_query(query):
    context = "Your health context here"  # Customize as needed
    return nlp_model(question=query, context=context)

def suggest_health_plan(user_profile):
    health_plans = []

    if user_profile.age > 50:
        health_plans.extend([
            "Plan A: Regular health checkups",
            "Plan B: Balanced diet with more calcium and vitamin D",
            "Plan C: Moderate exercise like walking or swimming",
            "Plan D: Regular bone density screenings",
            "Plan E: Cardiovascular health monitoring"
        ])
    elif user_profile.age > 30:
        health_plans.extend([
            "Plan A: Regular exercise, including cardio and strength training",
            "Plan B: Balanced diet rich in proteins and healthy fats",
            "Plan C: Stress management techniques like yoga or meditation",
            "Plan D: Regular sleep schedule and quality sleep",
            "Plan E: Routine health screenings (cholesterol, blood pressure)"
        ])
    else:
        health_plans.extend([
            "Plan A: High-intensity interval training (HIIT) or regular exercise",
            "Plan B: Balanced diet with a focus on lean proteins and whole grains",
            "Plan C: Adequate hydration and healthy snacking",
            "Plan D: Mental wellness practices like mindfulness or hobbies",
            "Plan E: Regular dental and eye checkups"
        ])

    if user_profile.gender.lower() == "female":
        health_plans.append("Plan F: Regular gynecological checkups and breast exams")
    elif user_profile.gender.lower() == "male":
        health_plans.append("Plan F: Regular prostate screenings after age 40")

    if user_profile.weight / ((user_profile.height / 100) ** 2) > 25:
        health_plans.append("Plan G: Weight management plan with a nutritionist")

    return health_plans
