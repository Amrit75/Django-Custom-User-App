from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationForm, AccountAuthenticateForm, AccountUpdateForm


# Create your views here.


def index_view(request):
    return render(request, "indexbase.html", {})


def privacy_policy_view(request):
    return render(request, "PrivacyPolicy.html", {})


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save User data
            # login user with newly register data
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)


def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = AccountAuthenticateForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get("next"))
                else:
                    return redirect('index')
        else:
            context['login_form'] = form
    else:
        form = AccountAuthenticateForm()
        context['login_form'] = form
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required()
def account_view(request):
    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            context['success_message'] = 'Data Updated'
    else:
        form = AccountUpdateForm(initial={
            'email': request.user.email,
            'username': request.user.username,
            'image': request.user.image.url,
            'name': request.user.name,
            'dob': request.user.dob,
            'address': request.user.address,
            'bio': request.user.bio,
            'phone_number': request.user.phone_number,
        }
        )
    context['account_form'] = form
    return render(request, 'accounts/profile.html', context)
