from skills.models import Skill

# Clear existing skills
Skill.objects.all().delete()

skills_data = [
    # Languages
    {"name": "Python", "category": "Languages", "icon": "fa-brands fa-python", "percentage": 90, "order": 1},
    {"name": "JavaScript", "category": "Languages", "icon": "fa-brands fa-js", "percentage": 85, "order": 2},
    {"name": "SQL", "category": "Languages", "icon": "fa-solid fa-database", "percentage": 80, "order": 3},
    {"name": "HTML5", "category": "Languages", "icon": "fa-brands fa-html5", "percentage": 95, "order": 4},
    {"name": "CSS3", "category": "Languages", "icon": "fa-brands fa-css3-alt", "percentage": 90, "order": 5},

    # Frameworks
    {"name": "React.js", "category": "Frameworks", "icon": "fa-brands fa-react", "percentage": 80, "order": 6},
    {"name": "Flask", "category": "Frameworks", "icon": "fa-solid fa-flask", "percentage": 75, "order": 7},

    # Tools & Technologies
    {"name": "MySQL", "category": "Tools & Technologies", "icon": "fa-solid fa-database", "percentage": 80, "order": 8},
    {"name": "MongoDB", "category": "Tools & Technologies", "icon": "fa-solid fa-leaf", "percentage": 75, "order": 9},
    {"name": "Redis", "category": "Tools & Technologies", "icon": "fa-solid fa-database", "percentage": 70, "order": 10},
    {"name": "Git", "category": "Tools & Technologies", "icon": "fa-brands fa-git-alt", "percentage": 85, "order": 11},
    {"name": "GitHub", "category": "Tools & Technologies", "icon": "fa-brands fa-github", "percentage": 85, "order": 12},
    {"name": "Docker", "category": "Tools & Technologies", "icon": "fa-brands fa-docker", "percentage": 70, "order": 13},
    {"name": "Postman (API Testing)", "category": "Tools & Technologies", "icon": "fa-solid fa-paper-plane", "percentage": 80, "order": 14},
    {"name": "REST APIs", "category": "Tools & Technologies", "icon": "fa-solid fa-gears", "percentage": 85, "order": 15},
]

for skill in skills_data:
    Skill.objects.create(**skill)

print("Successfully populated skills data!")
