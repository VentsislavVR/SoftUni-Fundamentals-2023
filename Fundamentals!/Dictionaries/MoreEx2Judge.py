def contest_participents():
    contest_students = {}
    while True:
        line = input()
        if line == "no more time":
            break
        line = line.split(" -> ")
        name, contest, points = line[0], line[1], int(line[2])
        if contest not in contest_students:
            contest_students[contest] = {name: points}
        else:
            if contest not in contest_students[contest]:
                contest_students[contest][name] = points

            elif contest_students[contest][name] < points:
                contest_students[contest][name] = points

    return contest_students


def total_points_per_student(contest):
    for submission, cont in contest.items():
        print(f"{submission}: {len(cont)} participants")
        for index in range(len(cont)):
            sorted_contest = sorted(cont.items(), key=lambda con: con[1], reverse=True)
            print(f"{index + 1}. {sorted_contest[index][0]} <::> {sorted_contest[index][1]}")


def final_ranking(contest):
    current_best = 0
    print("Individual standings:")
    name_totals = {}
    for course, results in contest.items():
        for name, score in results.items():
            if name not in name_totals:
                name_totals[name] = 0
            name_totals[name] += int(score)
    # final = sorted(name_totals,key=lambda x:x in contest.values())
    count = 1
    for name, total in sorted(name_totals.items(), key=lambda item: item[1], reverse=True):
        print(f"{count}. {name} -> {total}")
        count += 1


individual_ranking = contest_participents()
total_points_per_student(individual_ranking)
final_ranking(individual_ranking)

# Peter -> OOP -> 350
# George -> OOP -> 250
# Simo -> Advanced -> 600
# George -> OOP -> 300
# Prakash -> OOP -> 300
# Prakash -> Advanced -> 250
# Ani -> JSCore -> 400
# no more time
