from django.contrib import messages
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm, PasswordChangeForm )
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden,HttpResponse,HttpResponseRedirect
from accounts.form import RegisterForm, EditProfileForm
from django.views.generic import CreateView,View
from django.contrib.auth import authenticate, login, update_session_auth_hash
from accounts.models import User
from django.contrib.auth.decorators import login_required

def RegisterView(request):
    template = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'alarm': 'Username đã tồn tại.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'alarm': 'Email đã tồn tại.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error': 'Passwords không trùng khớp.'
                })
            else:
                User.objects.create_user(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password']
                )
                return render(request, template,{
                    'user':form.cleaned_data['password'],
                    'success': 'Bạn đã đăng ký tài khoản thành công. Vui lòng liên hệ với người quản lý để tài khoản được kích hoạt'
                })

    else:
        form = RegisterForm()
    return render(request, template, {'form': form})
#
@login_required(login_url='/accounts/')
def profile_view(request):
    args = {'user': request.user}
    return render(request,'accounts/profile.html',args)

@login_required(login_url='/accounts/')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
# neu sua thanh redirect('account/profile') thi url se la http://127.0.0.1:8000/account/profile/edit/account/profile
    else:
        form = EditProfileForm(instance = request.user)
        args = {'form':form}
        return render(request,'accounts/edit_profile.html',args)

@login_required(login_url='/accounts/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
            # neu sua thanh redirect('account/profile') thi url se la http://127.0.0.1:8000/account/profile/edit/account/profile
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = PasswordChangeForm(request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

