def students_credits(*courses_info,needed_credits = 240):
        student_book = {} # course:name , credits
        result = []

        for course_info in courses_info:
            course_name,course_credits,max_pts,student_pts= course_info.split("-")

            current_percentege = int(student_pts) / int(max_pts)
            credits_taken = current_percentege * int(course_credits)
            student_book[course_name] = credits_taken

        total_credits = sum(student_book.values())
        if total_credits >= needed_credits:
            result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
        else :
            result.append(f"Diyan needs {needed_credits - total_credits:.1f} credits more for a diploma.")


        # return '\n'.join(f"{course_name} - {course_credits:.1f}"
        #                  for course_name,course_credits in
        #                  sorted(student_book.items(),key=lambda x:-x[1] ))

        for course_name, course_credits in sorted(student_book.items(),key=lambda x:-x[1] ):
            result.append(f"{course_name} - {course_credits:.1f}")
        return '\n'.join(result)



print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
from unittest import TestCase, main


class Test(TestCase):
    def test_students_credits(self):
        result = students_credits(
            "Computer Science-12-300-250",
            "Basic Algebra-15-400-200",
            "Algorithms-25-500-490"
        )

        self.assertEqual(
            result.strip(),
            """Diyan needs 198.0 credits more for a diploma.
Algorithms - 24.5
Computer Science - 10.0
Basic Algebra - 7.5"""
        )


if __name__ == '__main__':
    main()