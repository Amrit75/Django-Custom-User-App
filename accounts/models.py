from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from phonenumber_field import modelfields


class AccountsManager(BaseUserManager):
    def create_user(self, email, username, password=None):  # fields which are used when creating accounts
        if not email:
            raise ValueError("User must have an Email address")
        if not username:
            raise ValueError("User must have an Username ")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser):
    name = models.CharField(max_length=50, verbose_name="Full Name", null=True)
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    username = models.CharField(max_length=50, unique=True)
    # add user own fields to model account
    dob = models.DateField(verbose_name="Date of Birth", null=True)
    address = models.CharField(max_length=1024, verbose_name="Address", null=True)
    bio = models.CharField(max_length=1000, verbose_name="About", null=True)
    phone_number = modelfields.PhoneNumberField(blank=True)

    # ------------------ #
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # ------------------ #
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # ----------------------------------------------------#
    USERNAME_FIELD = 'email'  # field name which user should identifies Ex: email/username
    REQUIRED_FIELDS = ['username', ]  # field name which must be fill for creating accounts Ex: name, mobile, etc

    objects = AccountsManager()

    def __str__(self):
        return self.email  # data which should print when object of accounts class is printing

    def has_perm(self, perm, obj=None):
        return self.is_admin  # return true if user has permission to access Ex: it returns true if user is admin

    def has_module_perms(self, app_label):
        return True
