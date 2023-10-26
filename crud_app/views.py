from django.shortcuts import render, redirect
from .models import StudentDetails


# Create your views here.
def home(request):
    data = StudentDetails.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def insertData(request):
    if request.method == "POST":
        student_name = request.POST["student_name"]
        student_email = request.POST["student_email"]
        student_age = request.POST["student_age"]
        student_gender = request.POST["student_gender"]
        User = StudentDetails(
            name=student_name,
            email=student_email,
            age=student_age,
            gender=student_gender,
        )
        User.save()

    return redirect("homepage")

def updateData(request,id):
    update_data = StudentDetails.objects.get(id=id)
    context = {"update_data": update_data}
    if request.method == "POST":
        student_name = request.POST["student_name"]
        student_email = request.POST["student_email"]
        student_age = request.POST["student_age"]
        student_gender = request.POST["student_gender"]

        update_data = StudentDetails.objects.get(id=id)
        update_data.name = student_name
        update_data.email = student_email
        update_data.age = student_age
        update_data.gender = student_gender
        update_data.save()
        return redirect('homepage')
        
    return render(request,'update.html',context)

def deleteData(request,id):
    delete_data = StudentDetails.objects.get(id=id)
    delete_data.delete()
    return redirect('homepage')