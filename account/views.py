from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account:profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile(request):
    # Custom logic for the user's profile view
    user = request.user  # Get the current logged-in user

    context = {
        'user': user,
        # Add any additional context data you want to pass to the template
    }

    return render(request, 'registration/profile.html', context)

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/change_password.html'

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'
