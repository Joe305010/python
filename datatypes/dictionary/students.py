sample_data = {
    'name': 'John',
    'location': {
        'country': 'Wonderland',
        'city': 'Heart City',
        'coordinates': {
            'latitude': 12.3456,
            'longitude': 65.4321
        }

    },
    "skills": [
        {"name": "Python", "level": "advanced"},
        {"name": "Machine Learning", "level": "intermediate"},
        {"name": "Data Analysis", "level": "beginner"},
    ],
    "experience": [
        {"company": "TechCorp", "role": "Software Engineer", "years": 3},
        {"company": "InnoLab", "role": "ML Engineer ", "years": 2},
    ]
}





print(sample_data['experience'][1]['years'])