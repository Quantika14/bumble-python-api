# Bumble API Wrapper in Python

**Author**: Jorge Coronado & QuantiKa14

This project provides a Python wrapper for interacting with Bumble’s API. It was adapted from an original Node.js version created by [hpats](https://github.com/hpats/bumapi/blob/master/app.js) and inspired by the research published by ISE in their [Bumble API reverse engineering article](https://blog.securityevaluators.com/reverse-engineering-bumbles-api-a2a0d39b3a87).

## Overview

This Python wrapper enables login, access to encounters, matches, and specific interaction capabilities for Bumble’s API. While the Bumble API is not publicly documented, these methods were developed through reverse engineering techniques and are intended for educational purposes only.

## Setup

**Dependencies**:
- Python 3.x
- `requests`
  
To install `requests`, use:
```bash
pip install requests
```

1. login(t, p)
Description: Logs into Bumble using a phone number and password.
Parameters:
t: Phone number.
p: Password.
Returns: A success message if login is successful.
2. startup()
Description: Initializes the Bumble app environment and retrieves essential app configurations.
Returns: Calls the login() function on success.
3. getEncounters()
Description: Retrieves a list of encounter suggestions.
Returns: Encounter list data in JSON format.
4. voteYesForEncounter(id)
Description: Votes “Yes” for a specific encounter by ID.
Parameters:
id: Encounter ID to vote for.
Returns: A success message indicating a positive vote.
5. voteNoForEncounter(id)
Description: Votes “No” for a specific encounter by ID.
Parameters:
id: Encounter ID to vote against.
Returns: A success message indicating a negative vote.
6. getMatchesList()
Description: Retrieves the list of matches for the user.
Returns: JSON data containing the matches list.
7. getMatchesDetails(id)
Description: Retrieves detailed information for a specific match.
Parameters:
id: ID of the match to retrieve details for.
Returns: JSON object with match details.
Example Usage
python
Copiar código
from bumble_api import BumbleAPI

# Initialize the BumbleAPI class
api = BumbleAPI(phone_number="1234567890", password="password123")

# Log in
login_status = api.login()
print(login_status)  # Expected output: "Login Successful"

# Retrieve encounters
encounters = api.get_encounters()
print(encounters)

# Vote yes for a specific encounter
yes_vote_status = api.vote_yes_for_encounter("encounter_id_123")
print(yes_vote_status)  # Expected output: "voted Yes"

# Retrieve matches list
matches = api.get_matches_list()
print(matches)

# Get details for a specific match
match_details = api.get_matches_details("match_id_123")
print(match_details)

# License
This project is licensed under the MIT License.

# Example
```
from bumble_api import BumbleAPI

# Initialize the BumbleAPI class
api = BumbleAPI(phone_number="1234567890", password="password123")

# Log in
login_status = api.login()
print(login_status)  # Expected output: "Login Successful"

# Retrieve encounters
encounters = api.get_encounters()
print(encounters)

# Vote yes for a specific encounter
yes_vote_status = api.vote_yes_for_encounter("encounter_id_123")
print(yes_vote_status)  # Expected output: "voted Yes"

# Retrieve matches list
matches = api.get_matches_list()
print(matches)

# Get details for a specific match
match_details = api.get_matches_details("match_id_123")
print(match_details)
```
