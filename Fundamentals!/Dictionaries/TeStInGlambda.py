data = {"gosho": {"tank": 350, "mid": 150}, "pesho": {"support": 250, "heal": 100}}

# Nested loops to access each key, inner key, and value
for player, skills in data.items():
    print(f"Player: {player}")
    for skill, value in skills.items():
        print(f"  Skill: {skill}, Value: {value}")

