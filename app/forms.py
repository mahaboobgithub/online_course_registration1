from django import  forms
from app.models import Coursemodel,Studentmodel

class Courseform(forms.ModelForm):
    class Meta:
        model=Coursemodel
        fields="__all__"


class StudentRegiserform(forms.ModelForm):

    class Meta:
        model=Studentmodel
        fields = ["name","contact_no","emailid","password"]
