from django.db import models

# Create your models here.
GROUP_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('O', 'O'),
    ('AB', 'AB'),
)

class Donor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    blood_group = models.CharField(max_length=2,choices=GROUP_CHOICES)
    rh_factor = models.BooleanField()
    phone_no = models.CharField(max_length=13)
    email = models.EmailField()
    address = models.CharField(max_length=50,null=True)
    last_donation = models.DateField()
    birth_year = models.IntegerField()