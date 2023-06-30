def winner(valid_submissions):
    high_score = 0
    top_baller = ""

    for name, points in valid_submissions.items():

        if sum(points.values()) > high_score:
            high_score = sum(points.values())
            top_baller = name

    return f"Best candidate is {top_baller} with total {high_score} points."


def to_be_validated_contest():
    not_validated = {}
    while True:
        line = input()
        if line == "end of contests":
            break
        line = line.split(":")
        initial_contest, initial_password = line[0], line[1]
        not_validated[initial_contest] = initial_password

    return not_validated


def valid_or_not(not_validated):
    submissions = {}
    while True:
        data = input()
        if data == "end of submissions":
            break
        data = data.split("=>")
        contest, password, username, points = data[0], data[1], data[2], int(data[3])
        if contest in not_validated and password == not_validated[contest]:
            if username not in submissions:
                submissions[username] = {contest: points}
            else:
                if contest not in submissions[username]:
                    submissions[username][contest] = points

                elif submissions[username][contest] < points:
                    submissions[username][contest] = points

    return submissions


def ranking(submissions):
    print("Ranking:")
    for key, value in sorted(submissions.items()):
        print(key)
        for points in sorted(value.items(), key=lambda x: x[1], reverse=True):
            print(f"#  {points[0]} -> {points[1]}")


not_validated = to_be_validated_contest()
valid_submissions = valid_or_not(not_validated)
print(winner(valid_submissions))
ranking(valid_submissions)
