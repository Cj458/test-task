from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


from django.http import HttpResponse

def index_page(request):
    # create a HttpResponse object and return it.
    response = HttpResponse('Hello World', content_type="text/plain")
    return response

# def login_user(request):
#     if request.method == "POST":
#         number = request.POST["number"]

#         user = authenticate(request, number=number)
#         if user is not None:
#             login(request, user)
#             return redirect("home")
#         else:
#             messages.success(request, ("There Was An Error Logging In, Try Again..."))
#             return redirect("login")

#     else:
#         return render(request, "authenticate/login.html", {})


# def logout_user(request):
#     logout(request)
#     messages.success(request, ("You Were Logged Out!"))
#     return redirect("home")


# def register_user(request):
#     if request.method == "POST":
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data["username"]
#             number = form.cleaned_data["number1"]
#             user = authenticate(username=username, number=number)
#             login(request, user)
#             messages.success(request, ("Registration Successful!"))
#             return redirect("home")
#     else:
#         form = RegisterUserForm()

#     return render(
#         request,
#         "authenticate/register_user.html",
#         {
#             "form": form,
#         },
#     )
    
