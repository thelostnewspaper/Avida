import pandas as pd
from hybrid_factorization import HybridFactorization

def calculate_language_scores(scribe_profiles, disabled_person_profiles):
    language_scores = {}
    for scribe, profile in scribe_profiles.items():
        for disabled_person, disabled_profile in disabled_person_profiles.items():
            language_score = 0
            if profile['language'] == disabled_profile['language']:
                language_score = 1
            elif profile['language'] in disabled_profile['language_preferences']:
                language_score = 0.5
            language_scores[(scribe, disabled_person)] = language_score
    return language_scores

def calculate_availability_scores(scribe_profiles, disabled_person_profiles):
    availability_scores = {}
    for scribe, profile in scribe_profiles.items():
        for disabled_person, disabled_profile in disabled_person_profiles.items():
            availability_score = 0
            if profile['availability'] == disabled_profile['availability']:
                availability_score = 1
            elif profile['availability'] in disabled_profile['availability_preferences']:
                availability_score = 0.5
            availability_scores[(scribe, disabled_person)] = availability_score
    return availability_scores

def calculate_location_scores(scribe_profiles, disabled_person_profiles):
    location_scores = {}
    for scribe, profile in scribe_profiles.items():
        for disabled_person, disabled_profile in disabled_person_profiles.items():
            location_score = 0
            if profile['location'] == disabled_profile['location']:
                location_score = 1
            elif profile['location'] in disabled_profile['location_preferences']:
                location_score = 0.5
            location_scores[(scribe, disabled_person)] = location_score
    return location_scores

def calculate_disability_type_scores(scribe_profiles, disabled_person_profiles):
    disability_type_scores = {}
    for scribe, profile in scribe_profiles.items():
        for disabled_person, disabled_profile in disabled_person_profiles.items():
            disability_type_score = 0
            if profile['disability_type'] == disabled_profile['disability_type']:
                disability_type_score = 1
            elif profile['disability_type'] in disabled_profile['disability_type_preferences']:
                disability_type_score = 0.5
            disability_type_scores[(scribe, disabled_person)] = disability_type_score
    return disability_type_scores

def calculate_scribe_skills_scores(scribe_profiles, disabled_person_profiles):
    scribe_skills_scores = {}
    for scribe, profile in scribe_profiles.items():
        for disabled_person, disabled_profile in disabled_person_profiles.items():
            scribe_skills_score = 0
            if profile['skills'] == disabled_profile['skills']:
                scribe_skills_score = 1
            elif profile['skills'] in disabled_profile['skills_preferences']:
                scribe_skills_score = 0.5
            scribe_skills_scores[(scribe, disabled_person)] = scribe_skills_score
    return scribe_skills_scores

def calculate_personal_preferences_scores(scribe_profiles, disabled_person_profiles):
    personal
