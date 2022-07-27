from django.shortcuts import render

def home_static(request):
    return render(request,'index1.html')