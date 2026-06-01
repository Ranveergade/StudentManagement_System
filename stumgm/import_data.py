import csv
from django.contrib.auth.models import User, Group
from stumgm.models import Student
def run():
   
       with open("D:\myapp2\myapp\myapp\stumgm\students.csv", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        student_group = Group.objects.get(name='Student')

        for row in reader:
            # ✅ define student_id correctly
            student_id = row['student_id']

            username = f"student{student_id}"
            password = f"stu{student_id}"

            # check if user exists
            if not User.objects.filter(username=username).exists():

                user = User.objects.create_user(
                    username=username,
                    password=password
                )

                # assign group
                user.groups.add(student_group)

                # create student record
                Student.objects.create(
                    user=user,
                    name=f"Student {student_id}",
                    student_id=student_id,
                    gpa=float(row['GPA']),
                    attendance=float(row['attendance_rate']),   # check exact column name
                    avg_grade=float(row['avg_course_grade'])    # FIXED
                )

                print(f"Created: {username} / {password}")

        print("DATA IMPORTED SUCCESSFULLY ")