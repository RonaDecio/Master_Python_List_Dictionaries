universities = [
    {"name": "University of the Philippines", "location": "Quezon City", "established year": 1908, "id": 1, "type": "Public", "website": "www.up.edu.ph"},
    {"name": "Ateneo de Manila University", "location": "Quezon City", "established year": 1859, "id": 2, "type": "Private", "website": "www.ateneo.edu"},
    {"name": "De La Salle University", "location": "Manila", "established year": 1911, "id": 3, "type": "Private", "website": "www.dlsu.edu.ph"},
    {"name": "University of Santo Tomas", "location": "Manila", "established year": 1611, "id": 4, "type": "Private", "website": "www.ust.edu.ph"},
    {"name": "Polytechnic University of the Philippines", "location": "Manila", "established year": 1904, "id": 5, "type": "Public", "website": "www.pup.edu.ph"}
]
for university in universities:
    print(f"Name: {university['name']}, Location: {university['location']}")