from django.shortcuts import render

def hello(request):
    return render(request, 'index.html' )

def showList(request):
    fruits = ["mango", "apple", "Banana"]
    student_names = ["tony","mony", "sony"]
    return render(request, 'showlist.html', {"fruits": fruits, "student_names": student_names })
def home(request):
    return render (request, 'home.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def contactus(request):
    return render(request, 'contactus.html')
