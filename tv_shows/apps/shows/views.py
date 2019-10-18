from django.shortcuts import render, HttpResponse, redirect
from apps.shows.models import Show
from django.contrib import messages
from datetime import datetime

def index(request):
    return HttpResponse("Your index route works. Great Success.")

def newShow(request):
    return render(request, "shows/newshow.html")

def createShow(request):
    errors = Show.objects.new_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/newShow")
    else:
        created_object = Show.objects.create(title=request.POST["newTitle"], network=request.POST["newNetwork"], release_date=request.POST["newRelDate"], desc = request.POST["newDesc"])
        show_id = created_object.id
        return redirect(f"/shows/{show_id}")

def viewShow(request, id):
    context = {
        "shows" : Show.objects.get(id=id)
    }
    return render(request, "shows/viewshow.html", context)

def editShow(request, id): 
    show_id = Show.objects.get(id=id).id
    context = {
        "shows" : Show.objects.get(id=id)
    }

    return render(request, "shows/editshow.html", context)

def saveEdit(request, id): 
    errors = Show.objects.new_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/" + id + "/edit")
    else:
        s = Show.objects.get(id=id)
        s.title = request.POST["newTitle"]
        s.network = request.POST["newNetwork"]
        s.release_date = request.POST["newRelDate"]
        s.desc = request.POST["newDesc"]
        s.save()
    return redirect("/shows")

def deleteShow(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    
    return redirect("/shows")

def shows(request):
    context = {
        "shows": Show.objects.all()
    }
        
    return render(request, "shows/shows.html", context)