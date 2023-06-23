from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "Arsha.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

def blog(request):
    return render(request, "blog.html")

# def nav(request):
#     data={
#         'title': "about",
#     }
#     return render(request, "header.html", data)

# def about(request):
#     return HttpResponse("welcome to website building plateform ")