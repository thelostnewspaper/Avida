def gale_shapley(volunteer_scribes, disabled_persons):
    # Create preference lists for each entity
    volunteer_scribe_prefs = {v: [d for d in disabled_persons] for v in volunteer_scribes}
    disabled_person_prefs = {d: [v for v in volunteer_scribes] for d in disabled_persons}

    # Initialize the matching
    matching = {}

    # Proposal and rejection loop
    while len(matching) < len(volunteer_scribes):
        for v in volunteer_scribes:
            if v not in matching:
                # Get the most preferred disabled person for the current volunteer scribe
                d = volunteer_scribe_prefs[v][0]
                # If the disabled person is not already matched, match them
                if d not in matching.values():
                    matching[v] = d
                # Otherwise, check if the disabled person prefers the current volunteer scribe
                elif disabled_person_prefs[d].index(v) < disabled_person_prefs[d].index(matching[d]):
                    # If they do, update the matching
                    matching[v] = d
                    del matching[matching[d]]
                # If not, reject the proposal
                else:
                    volunteer_scribe_prefs[v].pop(0)

    return matching

# Example usage:
volunteer_scribes = ['John', 'Jane', 'Bob']
disabled_persons = ['Alice', 'Bob', 'Charlie']

matching = gale_shapley(volunteer_scribes, disabled_persons)
print(matching)