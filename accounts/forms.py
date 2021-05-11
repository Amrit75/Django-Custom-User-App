from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts.models import Accounts


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required a valid email address')

    # TODO: form editing

    class Meta:
        model = Accounts
        fields = ('email', 'username', 'password1', 'password2')


class AccountAuthenticateForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Accounts
        fields = ('email', 'password')

    def clean(self):
        try:
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid email or password.")
        except KeyError:
            raise forms.ValidationError('Invalid credentials')


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ('email', 'username', 'name', 'dob', 'address', 'bio', 'phone_number', 'image')

    def clean_email(self):
        if self.is_valid():
            try:
                email = self.cleaned_data['email']
                account = Accounts.objects.exclude(pk=self.instance.pk).get(email=email)
            except KeyError:
                raise forms.ValidationError('Invalid Email')
            except Accounts.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)

    def clean_username(self):
        if self.is_valid():
            try:
                username = self.cleaned_data['username']
                account = Accounts.objects.exclude(pk=self.instance.pk).get(username=username)
            except KeyError:
                raise forms.ValidationError('Invalid Username')
            except Accounts.DoesNotExist:
                return username
            raise forms.ValidationError('Username: "%s" is not available to use.' % username)
