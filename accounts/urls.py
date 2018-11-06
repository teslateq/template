from django.urls import path
# from django.contrib.auth import views as auth_views
from accounts import views
# from django.contrib.auth.views import (
#     login, logout, password_reset,
#     password_reset_done,
#     password_reset_confirm,
#     password_reset_complete
# )

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
app_name = 'accounts'
urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name= 'accounts/logout.html'), name='logout'),
    path('register/', views.RegisterView, name='register'),
    path('profile/',views.profile_view,name='profile_view'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),

]


