from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Customer(AbstractUser):  # Extending Django's User model
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    # Resolve conflicts by setting unique related names
    groups = models.ManyToManyField(Group, related_name="customer_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customer_permissions", blank=True)

    REQUIRED_FIELDS = ['phone_number', 'address', 'gender']

    def __str__(self):
        return self.username
