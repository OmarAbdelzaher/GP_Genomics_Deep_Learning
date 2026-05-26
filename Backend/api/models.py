from django.db import models
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager


def upload_location(instance,filename):
    return filename

# Defining the choices of the radio button 
GENDER_CHOICES = (
    ('Male','male'),
    ('Female','female')
)

# Creating a Patient Model to accept the patient entered data
class Patient_1(models.Model):
    name = models.CharField(max_length = 50)
    birthdate = models.DateField(null=True)
    nationality = models.CharField(max_length = 50,null = True)
    gender = models.CharField(max_length = 50, choices = GENDER_CHOICES,null = True)
    visitReason = models.TextField(null=True)
    captured_image = models.CharField(max_length = 100000000,null=True)
    consent = models.BooleanField(default=False)

# Creating a linked table for the patients' images which allow storing multi-entered images by the user
class PatientImage(models.Model):
    patient = models.ForeignKey(Patient_1, on_delete = models.CASCADE,related_name="images") # Patient have several images, when it is deleted we should determine what we will do with its children, Cascade delete its children, Null set the parent of the children to null, protect will disable deleteing because the parent has children
    image_upload = models.ImageField(null=True, upload_to = 'Patient Images/')

# Creating a model for the Doctor to accept his entered data
class DoctorData(AbstractBaseUser):
    user_name = models.CharField(max_length = 50 , unique=True, default = "Doctor Name")
    email = models.EmailField(max_length = 50, unique=True)
    phone_number = models.IntegerField(null=True)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self,*args,**kwargs):
        self.set_password(self.password)
        super().save(*args,**kwargs)

# Creating a linked table for the patient's reports to easily retrieve the algorithm result
class ReportResult(models.Model):
    patient = models.ForeignKey(Patient_1, on_delete = models.CASCADE,related_name="results",null=True,default=None)
    result = models.CharField(max_length = 100)