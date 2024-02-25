from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
# Create your models here.

'''
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
'''

phone_regex = RegexValidator(
    regex=r"^\d{10}", message="phone must be 10 digits only"
)
CLASS_CHOICE = (
    ('CLASS ONE','CLASS ONE'),
    ('CLASS TWO','CLASS TWO'),
    ('CLASS THREE', 'CLASS THREE'),
    ('CLASS FOUR', 'CLASS FOUR'),
    ('CLASS FIVE','CLASS FIVE'),
    ('CLASS SIX','CLASS SIX'),
    ('CLASS SEVEN','CLASS SEVEN'),
    ('CLASS EIGHT','CLASS EIGHT'),
    ('CLASS NINE','CLASS NINE'),
    ('MATRIC','MATRIC')
)



class MyAccountManager(BaseUserManager):
    def create_user(self,phone, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not phone:
            raise ValueError('User shold have Phone Number')
        user  = self.model(
            email=self.normalize_email(email),
            phone= phone,
            username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone, email, username, password):
        user  = self.create_user(
                phone=phone,
                email=self.normalize_email(email),
                password=password,
                username=username,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class StudentUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(unique=True, max_length=10, null=False, blank = False, validators=[phone_regex])
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='uploaded_img', blank=True)
    class_name = models.CharField(choices=CLASS_CHOICE, max_length=20)
    status = models.BooleanField(default=False)
    is_admin= models.BooleanField(default=False)
    is_active= models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username','email']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True