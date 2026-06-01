from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from .models import Student

# Create your views here.
@login_required
def view(request):

    is_teacher = request.user.groups.filter(name='Teacher').exists()

    if is_teacher:
        stud = Student.objects.all()
    else:
        stud = Student.objects.filter(user=request.user)

    return render(request, "view.html", {
        "students": stud,
        "is_teacher": is_teacher
    })

def update(request,id):
    studentt = Student.objects.get(id=id)
    if request.method == "POST":
        studentt.name = request.POST.get('name')
        studentt.student_id = request.POST.get('student_id')
        studentt. gpa = request.POST.get('gpa')
        studentt.attendance = request.POST.get('attdendance')
        studentt.avg_grade = request.POST.get('avg_grade')
        
        studentt.save()
        return redirect('view')
    return render(request,"update.html",{"student":studentt})

def delete(request,id):
    studentt=Student.objects.get(id=id)
    if request.method == "POST":
        studentt.delete()
        return redirect('view')

    return render(request, "delete.html", {"student": studentt})


def home(request):
    if request.user.is_authenticated:
        return render(request,"home.html")   # logged in → go to dashboard
    else:
        return redirect('login')  # not logged in → login



def search(request):
    result = None

    if request.method == "POST":
        student_id = request.POST.get("student_id")

        result = Student.objects.filter(student_id=student_id)

    return render(request, "search.html", {"result": result})
        
    
def logout_page(request):
    return render(request, "logout.html")

'''def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        # Create user
        user = User.objects.create_user(username=username, password=password)

        # Assign group
        group = Group.objects.get(name=role)
        user.groups.add(group)

        # Create student profile only if role is student
        if role == "Student":
            Student.objects.create(
                user=user,
                sname=username,
                sid=0,
                eng=0,
                hindi=0,
                physic=0,
                math=0,
                chemistry=0
            )

        return redirect('login')

    return render(request, "signup.html")'''