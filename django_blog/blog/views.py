from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserUpdateForm


# ✅ Registration view
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # built-in login URL
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})

# ✅ Profile view (only for logged-in users)
@login_required
def profile(request):
    return render(request, "registration/profile.html")

@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "registration/profile.html", {"form": form})

