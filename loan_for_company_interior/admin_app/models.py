from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    dob = models.DateField(default="2000-12-12", blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    email = models.EmailField(db_index=True, max_length=50, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    pin_code = models.IntegerField(default=0, blank=True)
    mobile = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="customer/user/", default=0, blank=True)
    signature = models.ImageField(upload_to="customer/user/", default=0, blank=True)
    role = models.CharField(max_length=50, default='customer', choices=ROLE_CHOICES)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
