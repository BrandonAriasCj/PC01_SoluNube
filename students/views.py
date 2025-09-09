from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import StudentForm
from .models import Student


def student_list(request):
    students = Student.objects.all().order_by("last_name", "first_name")
    return render(request, "students/student_list.html", {"students": students})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("student_list"))
    else:
        form = StudentForm()
    return render(request, "students/student_form.html", {"form": form})
