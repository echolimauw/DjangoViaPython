from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

def index(request):
    return render(request, "index.html")

def process_reg(request):
    print("reached register route")
    errors = User.objects.reg_validator(request.POST)

    if len(errors) > 0:
        print("You have errors! reached if statement")
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        print("No validation errors! Reached else")
        new_user = User.objects.create()
        new_user.first_name = request.POST['first_name']
        new_user.last_name = request.POST['last_name']
        new_user.email = request.POST['email']
        new_user.password = request.POST['password']
        new_user.save()
        print(f"new_user = {new_user}")
        id = new_user.id
        request.session['user_id'] = id
        # messages.success(request, "successfully added user")
        return redirect(f'/success/{id}')

def process_log(request):
    user_result = User.objects.filter(email=request.POST["login_email"])
    if not user_result[0]:
        # error goes here
        messages.error(request, "User not found")
        return redirect("/")
    
    hashed_password = user_result[0].password
    password = request.POST["login_pw"]
    if bcrypt.checkpw(password.encode(), hashed_password.encode()):
        request.session['user_id'] = user_result[0].id
        id = user_result[0].id
        return redirect(f'/dash/{id}')
        # You may need to update this url, depending on if you rename dash.html
    else:
        print("email and password do not match")
        return redirect("/")

def success(request, id):

    if 'user_id' in request.session:
        context = {
            "thisUser" : User.objects.get(id=id)
        }
        return render(request, "dash.html", context)

    else:
        return redirect("/")

def logout(request):
    request.session.flush()
    return redirect("/")