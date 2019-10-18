from django.shortcuts import render, HttpResponse, redirect
from apps.shows.models import Show
from datetime import datetime
def newShow(request):

    return render(request, "shows_app/newshow.html")

    # return HttpResponse("this is where we add new shows")

def newShowPass(request):

    errors = Show.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/new")
    else:

        Show.objects.create(title=request.POST["newTitle"], network=request.POST["newNetwork"], desc = request.POST["newDesc"])
    
    # , release_date=request.POST["newRelDate"]
    return redirect("/shows")

    # return HttpResponse("this is where we add new shows")

def infoShow(request, show_id):
    thisShow = Show.objects.get(id=show_id)
    # released = thisShow.release_date.strftime('%d %B, %Y')
    context = {
        "shows" : thisShow,
    }

    return render(request, "shows_app/showinfo.html", context)
    # return HttpResponse("this is where we view info about a given show")

def updateShow(request, show_id):
    thisShow = Show.objects.get(id=show_id)
    context = {
        "shows" : thisShow,
    }
    
    return render(request, "shows_app/showupdate.html", context)


    return HttpResponse("this is where we update existing shows")

def updateShowPass(request, show_id):
    
    # errors = Show.objects.basic_validator(request.POST)

    # if len(errors):
    #     for tag, error in errors.iteritems():
    #         messages.error(request, error, extra_tags=tag)
    #     return redirect("new")
    # else:

    # thisShow = 
    Show.objects.get(id=show_id)
    context = {
        "shows" : thisShow,
    }
    
    show = Show.objects.get(id=show_id)
    show.save()
    return redirect("/shows")


    # return HttpResponse("this will be how we PASS updated show info")

def deleteShow(request, show_id):

    show = Show.objects.get(id=show_id)
    show.delete()
    
    return redirect("/shows")

    # return HttpResponse("this is how we delete shows")

def shows(request):
    context = {
        "shows": Show.objects.all()
    }
        
    return render(request, "shows_app/shows.html", context)

    # return HttpResponse("this is the index page")

def index(request):

    return redirect("/shows")