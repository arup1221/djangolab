from django.http import HttpResponse
from django.shortcuts import render
from ap3.models import *
from django.views import generic

def reg(request):
    if request.method=='POST':
        sid=request.POST.get("sname")
        cid=request.POST.get("cname")
        student=Student.objects.get(id=sid)
        course=Course.objects.get(id=cid)
        res = student.enrolment.filter(id=cid)
        if res:
            return HttpResponse("<h1>Student already enrolled Sucessfully</h1>")
        student.enrolment.add(course)
        return HttpResponse("<h1>Student enrolled Sucessfully</h1>")
    
    else:
        students=Student.objects.all()
        courses=Course.objects.all()
        return render(request,"reg.html",{"students":students,"courses":courses})
    
def course_search(request):
    if request.method=='POST':
        cid=request.POST.get("cname")
        s=Student.objects.all()
        student_list=list()
        for student in s:
            if student.enrolment.filter(id=cid):
                student_list.append(student)
        if len(student_list)==0:
            return HttpResponse("<h1>No students Enrolled</h1>")
        return render(request,"selected_student.html",{"student_list":student_list})
    else:
        courses = Course.objects.all()

        return render(request, "course_search.html",{"courses":courses})
    
def add_project(request):
    if request.method=="POST":
        form= ProjectReg(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Record inserted sucessfully</h1>")
        else: 
            return HttpResponse("<h1>Record Not Inserted</h1>")
    
    else: 
        form = ProjectReg()
        return render(request, "add_project.html", {"form":form})

class StudentListView(generic.ListView):
    model = Student
    template_name='Student_list.html'

class StudentDetailView(generic.ListView):
    model = Student
    template_name = 'Student_detail.html'