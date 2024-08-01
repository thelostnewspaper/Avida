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
    personal_preferences_scores = {}
    for scribe, profile in scribe_profiles.items():
        for disabled_person, disabled_profile in disabled_person_profiles.items():
            personal_preferences_score = 0
            if profile['personality'] == disabled_profile['personality']:
                personal_preferences_score = 1
            elif profile['personality'] in disabled_profile['personality_preferences']:
                personal_preferences_score = 0.5
            personal_preferences_scores[(scribe, disabled_person)] = personal_preferences_score
    return personal_preferences_scores

def combine_scores(language_scores, availability_scores, location_scores, disability_type_scores, scribe_skills_scores, personal_preferences_scores):
    combined_scores = {}
    for scribe, disabled_person in language_scores.keys():
        combined_score = (language_scores[(scribe, disabled_person)] + availability_scores[(scribe, disabled_person)] + location_scores[(scribe, disabled_person)] + disability_type_scores[(scribe, disabled_person)] + scribe_skills_scores[(scribe, disabled_person)] + personal_preferences_scores[(scribe, disabled_person)]) / 6
        combined_scores[(scribe, disabled_person)] = combined_score
    return combined_scores

def rank_matches(combined_scores):
    ranked_matches = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
    return ranked_matches

def gale_shapley(matching, preferences, free_scribes, free_disabled):
    while free_scribes:
        scribe = free_scribes.pop(0)
        for disabled in preferences[scribe]:
            if disabled in free_disabled:
                matching[scribe] = disabled
                free_disabled.remove(disabled)
                break
            else:
                current_scribe = matching[disabled]
                if preferences[disabled].index(scribe) < preferences[disabled].index(current_scribe):
                    matching[disabled] = scribe
                    free_scribes.append(current_scribe)
                    break
    return matching