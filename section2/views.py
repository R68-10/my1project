from django.shortcuts import render

# Create your views here.

def section2(request):
    return render(request,'section2/quiz.html')