from django.db import models
# Create your models here.
GROUP_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('O', 'O'),
    ('AB', 'AB'),
)

class Donor(models.Model):
    first_name = models.CharField(max_length=30,verbose_name="Full Name")
    last_name = models.CharField(max_length=30,verbose_name="Last Name")
    blood_group = models.CharField(max_length=2,choices=GROUP_CHOICES,verbose_name="Blood Group")
    rh_factor = models.CharField(max_length=1,verbose_name="RH")
    phone_no = models.CharField(max_length=13,verbose_name="Mobile")
    email = models.EmailField(verbose_name="Email")
    address = models.CharField(max_length=50,null=True,verbose_name="Address")
    last_donation = models.DateField(verbose_name="Last Donation")
    birth_year = models.IntegerField(verbose_name="Birth Year")