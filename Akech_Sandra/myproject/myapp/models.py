from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
import re

def validate_letters(value):
    if not re.match(r"^([a-zA-Z]+\s)*[a-zA-Z]+$", value):
        raise ValidationError("Only letters are allowed.")
    
class Courses(models.Model):
    course_name = models.CharField(max_length=50)    
    
class EntryScheme(models.Model):
    entryScheme_name = models.CharField(max_length=50)
    
class IntakeField(models.Model):
    intakefield_name = models.CharField(max_length=50)          
    
class SponsorField(models.Model):
    sponsorfield_name = models.CharField(max_length=50)    

class Std_Application(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    firstName = models.CharField(
        validators=[MinLengthValidator(3), validate_letters], 
        max_length=30, 
        null=True, 
        blank=True
    )
    lastName = models.CharField(
        validators=[MinLengthValidator(3), validate_letters], 
        max_length=30, 
        null=True, 
        blank=True
    )
    courseField = models.ForeignKey(Courses, on_delete=models.CASCADE)
    entryScheme = models.ForeignKey(EntryScheme, on_delete=models.CASCADE)
    intakeField = models.ForeignKey(IntakeField, on_delete=models.CASCADE)
    sponsorField = models.ForeignKey(SponsorField, on_delete=models.CASCADE)
    gender = models.CharField(
        null=True, 
        blank=True, 
        max_length=15, 
        choices=GENDER
    )
    date_of_birth = models.DateField()
    residence = models.CharField(
        validators=[MinLengthValidator(2), validate_letters], 
        null=True, 
        blank=True, 
        max_length=250
    )
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName
