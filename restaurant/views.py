from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomerRegistrationForm

# ✅ Home View
def home(request):
    return render(request, 'home.html')  # Ensure this file exists

# ✅ Registration View
def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, "Registration successful! Welcome to GoTable.")
            return redirect('home')  # Ensure 'home' is defined in urls.py
    else:
        form = CustomerRegistrationForm()
    
    return render(request, 'register.html', {'form': form})  # Ensure this file exists

# ✅ Profile Update View
@login_required
def profile_update(request):
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile_update')  # Ensure 'profile_update' URL name exists in urls.py
    else:
        form = CustomerUpdateForm(instance=request.user)

    return render(request, 'restaurant/profile.html', {'form': form})  # Ensure this file exists

# ✅ Catalog View
def catalog_view(request):
    return render(request, 'restaurant/catalog.html')  # Ensure this file exists

# ✅ Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome back! You have successfully logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    
    return render(request, 'login.html')  # Ensure this file exists

# ✅ Logout View
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # Ensure 'login' is defined in urls.py
