contest_and_pass = {}
while True:
    line = input()
    if line == "end of contests":
        break
    line = line.split(":")
    initial_contest, initial_password = line[0], line[1]
    contest_and_pass[initial_contest] = initial_password
name_and_points = {}
name_and_courses = {}
while True:
    data = input()
    if data == "end of submissions":
        break
    data = data.split("=>")
    contest, password, username, points = data[0], data[1], data[2], data[3]
    for _ in range(len(contest_and_pass)):
        if contest in contest_and_pass and password == contest_and_pass[contest]:
            if username not in name_and_courses:
                name_and_courses[username] = []
            name_and_courses[username].append(contest)
            if username not in name_and_points:
                name_and_points[username] = []
            name_and_points[username].append(points)
            break
almost_final_result = {}
result = {username: (name_and_points[username], name_and_courses[username]) for username in name_and_points}
for username, (points, contest) in result.items():
    almost_final_result[username] = list(zip(points, contest))
name_score = {}
for key, value in sorted(almost_final_result.items()):
    course_points = {}
    for points, course in (value):
        if course not in course_points:
            course_points[course] = int(points)
        else:
            course_points[course] = max(course_points[course], int(points))
    total = sum(course_points.values())
    name_score[key] = total
winner = max(name_score, key=name_score.get)
highest_score = name_score[winner]

print(f"Best candidate is {winner} with total {highest_score} points.")
print("Ranking:")
for key, value in sorted(almost_final_result.items()):
    print(key)
    printed = set()
    for points, course in sorted(value, reverse=True):
        if course not in printed:
            print(f"#  {course} -> {points}")
            printed.add(course)
