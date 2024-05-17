from django import forms
from .models import *

class Std_ApplicationForm(forms.ModelForm):
    
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    
    firstName = forms.CharField( required=True , widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="First Name" )
    lastName = forms.CharField( required=True , widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Last Name" )
    courseField = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"--select--", "class":"form-control"}), label="Course" )
    entryScheme = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"--select--", "class":"form-control"}), label="Entry Scheme" )
    intakeField = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"--select--", "class":"form-control"}), label="Intake" )
    SponsorField = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"--select--", "class":"form-control"}), label="Sponsorship" )
    gender = forms.ChoiceField(choices=GENDER, required=True, widget=forms.RadioSelect(attrs={"class": "form-check-input"}), label="Gender")
    date_of_birth = forms.CharField( required=True , widget=forms.widgets.TextInput(attrs={"placeholder":"YYYY/MM/DD", "class":"form-control"}), label="Date of Birth",)
    residence = forms.CharField( required=True , widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Residence" )
    
    class Meta:
        model = Std_Application
        fields = '__all__'
