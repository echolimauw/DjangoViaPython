from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "baseapp/index.html")

def success(request):
    if "username" in request.session:
        return redirect("/error")
    context = {
        "username": request.session["username"]
    }
    return render(request,"baseapp/success.html", context)

def error(request):
    return render(request, "baseapp/error.html")

def show_animal(request, animal):
    return render(request, "baseapp/animal.html")

def process(request):
    request.session["username"] = request.POST["username"]
    return redirect["/success"]

def logout(request):
    pass