from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserProfileForm

def home(request):
    return render(request, 'main/home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'main/login.html')

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        phone_number = request.POST.get('phone_number')
        take_personality_test = request.POST.get('take_personality_test') == 'on'
        
        name_parts = full_name.split()
        if len(name_parts) > 1:
            first_name = name_parts[0]
            last_name = ' '.join(name_parts[1:])
        else:
            first_name = full_name
            last_name = ''
        
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            location=location,
            phone_number=phone_number
        )
        login(request, user)
        return redirect('dashboard')
    return render(request, 'main/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')

def features(request):
    return render(request, 'main/features.html')

def confession_matching(request):
    return render(request, 'main/confession_matching.html')

def compatibility_suggestions(request):
    return render(request, 'main/compatibility_suggestions.html')

def location_suggestions(request):
    return render(request, 'main/location_suggestions.html')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'main/profile.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html', {'user': request.user})