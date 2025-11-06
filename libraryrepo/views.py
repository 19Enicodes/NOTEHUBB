from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q
from .models import CreateMaterials


# ---------- Signup ----------
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # create user
            login(request, user)  # log them in immediately
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


# ---------- Login ----------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


# ---------- Logout ----------
def logout_view(request):
    logout(request)
    return redirect("login")


# ---------- Dashboard (Protected) ----------
@login_required(login_url="login")
def create_view(request):
    query = request.GET.get("q", "")
    if query:
        materials = CreateMaterials.objects.filter(
            Q(title__icontains=query)
            | Q(author__icontains=query)
            | Q(coursecode__icontains=query)
        )
    else:
        materials = CreateMaterials.objects.all()

    return render(request, "index.html", {"see": materials, "query": query})


