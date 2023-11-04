# diagnosis/diagnostic_logic.py

from .symptoms import SYMPTOMS

def generate_diagnosis(selected_symptoms, user):
    # Initialize severity and symptom count
    total_severity = 0
    symptom_count = 0

    # Calculate the total severity based on selected symptoms
    for selected_symptom in selected_symptoms:
        symptom_name = selected_symptom
        severity = next((s["severity"] for s in SYMPTOMS if s["name"] == symptom_name), 0)
        total_severity += severity
        symptom_count += 1

    # Define severity thresholds for different diagnosis levels
    mild_threshold = 10
    moderate_threshold = 15

    # Generate diagnosis based on severity and symptom count
    if symptom_count == 0:
        diagnosis_result = "No symptoms selected. Please answer the questionnaire."
    elif total_severity < mild_threshold:
        diagnosis_result = "You may have mild symptoms. Monitor your condition and seek medical advice if needed."
    elif total_severity < moderate_threshold:
        diagnosis_result = "You may have moderate symptoms. Consult a healthcare professional."
    else:
        diagnosis_result = "Your symptoms are severe. Please contact a doctor immediately."

    return diagnosis_result
