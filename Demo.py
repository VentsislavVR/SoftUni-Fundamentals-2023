import emoji
print("<3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3 <3<3 <3 <3")
print(emoji.emojize("          :red_heart:  :red_heart:  :red_heart:  :red_heart:  :red_heart:  :red_heart:  :red_heart:  :red_heart:"))

print("       Добре дошла в моята малък любовен QUIZ <3!")
print("<3 <3 <3                                    <3<3 <3 <3")
name = input("Напиши си името тук(можеи прякор,примерно слънце или Марли дъ шампиона:")
print("<3 <3 <3                                                                        <3 <3 <3")
print("                Здравей", name, "!Надявам се да си ексаийтед!!")
print("<3 <3 <3                                                           <3 <3 <3")
print("       Честит Св.Валентин! Нека видим как ще се справиш!(псс .. всичко с малки букви)")
print("<3 <3 <3 ----------------------------------------------------------------<3 <3 <3")
print("    П.С Сеймейната чест лежи на твоите плещи (но прешър)!!!Аз и Ариел те подкрепяме!")
print("<3 <3 <3 -------------------------------------------------------------------<3 <3 <3")

# Въпроси и отговори
questions = [
    "Къде ни беше първата целувка?",
    "ден от седмицата?",
    "От колко време сме заедно в месеци? (закръгли към голямото) ((Жокер ***далматинци))",
    "Ти си роза ти си?",
    "Какво момиченце искам да ни е първото бебе? (пол):Д",
    "Ще се омъжиш ли за мен..опе не друго беше...В колко..не..Фазата на луната когато ти се преца...каза ДА??",
    "Ако аз съм голяма мечка,ти си?",
    "1+1= ? ( мисли свети валентинино)",
    "Това бяха 8 въпроса == на 8 прекрасни години прекарани с теб!! Последен бонус : Ще ми бъдеш ли валентинка?"

]

answers = [
    "в парка",
    "неделя",
    "101",
    "крем",
    "момиче",
    "нарастващ полумесец",
    "малка мечка",
    "1",
    "да"
]

# Каунтър верни отговори
correct_answers = 0

# задаваме въпроси и проверяваме отговор ( мъгличка малко но работи)
for i, question in enumerate(questions):
    answer = input(question + ": ")
    if answer.lower() == answers[i].lower():
        print("Позна!", name, "! топ котка!")
        print()
        correct_answers += 1
    else:
        print("опа,Не", name, ". но поне си топ котка")
        print()

# смятане на резултат
score = correct_answers / len(questions) * 100
print("Позна", correct_answers, "от", len(questions), "въпроса.")
print("Имаш ейй толкова много точки", score, "%.", name, ".")

# Краен
if score >= 60:
    print("Евала", name,
          "! Шампион си!")
elif score >= 40:
    print("Много добрее!", name,
          "! Сребро<3!")
else:
    print("Няма страшно", name,
          "! Срещу 0.50 стотинки може пак да пробваш.")

# Търтълчето копи пейст :Д текста е променен
import turtle

pen = turtle.Turtle()

def curve():
	for i in range(200):

		pen.right(1)
		pen.forward(1)

import turtle as t
pen = t.Turtle()
t.bgcolor('#9966cc')
t.delay(8)
pen.color('#ffe4e1')
pen.begin_fill()
pen.left(40)
pen.forward(120)
pen.circle(80, 190)
pen.right(100)
pen.circle(80, 180)
pen.forward(160)
pen.left(90)
pen.forward(50)
pen.setpos(-60, 100)
pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-60, 100)
    pen.color('red')
    pen.write(f'Обичам те! {name}', font=("Comic Sans MS", 16))
txt()
pen.end_fill()
t.exitonclick()



