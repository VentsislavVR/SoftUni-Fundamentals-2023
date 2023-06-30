results = {}
languages = {}

while True:
    command = input()
    if command == "exam finished":
        break
    command = command.split("-")
    username, language = command[0], command[1]
    if language == "banned":
        del results[username]
    else:
        points = int(command[2])
        if username not in results.keys():
            results[username] = []
        results[username].append(points)

        if language not in languages.keys():
            languages[language] = 0
        languages[language] += 1

print("Results:")
for user, max_points in results.items():
    print(f"{user} | {max(max_points)}")
print("Submissions:")
for language, submissions_count in languages.items():
    print(f"{language} - {submissions_count}")