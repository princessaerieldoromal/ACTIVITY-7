from django.shortcuts import render, redirect
from .firebase import db

# View to add student via form
def add_student_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        score = int(request.POST.get("score"))
        subject = request.POST.get("subject")
        exam_date = request.POST.get("exam_date")

        student_data = {
            "name": name,
            "score": score,
            "subject": subject,
            "exam_date": exam_date
        }

        db.collection("students").add(student_data)
        return redirect("dashboard")

    return render(request, "add_student.html")


# Dashboard view to display chart and table
def dashboard(request):
    students_ref = db.collection("students").stream()

    students = []
    labels = []
    scores = []

    for student in students_ref:
        data = student.to_dict()
        students.append(data)
        labels.append(data["name"])
        scores.append(data["score"])

    context = {
        "students": students,  # for table
        "names": labels,       # for chart.js
        "scores": scores       # for chart.js
    }

    return render(request, "dashboard.html", context)