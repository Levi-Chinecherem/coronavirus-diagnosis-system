from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup, profile, CustomPasswordChangeView, CustomPasswordChangeDoneView
from django.urls import reverse_lazy

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('change-password/', CustomPasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    path('password-change-done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
]
