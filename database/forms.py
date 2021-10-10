from django import forms
from django.forms import ModelForm
from database.models import student
from django import forms


class Reg(forms.ModelForm):
	class Meta:
		model = student
		fields = ['Name','Roll_No','credits_used']
		widgets = {
			'Name':forms.TextInput(attrs= {'class':'form-control','placeholder':'Enter name'}),
			'Roll_No':forms.TextInput(attrs= {'class':'form-control','placeholder':'Enter Roll_No'}),
			
			'credits_used':forms.TextInput(attrs= {'class':'form-control','placeholder':'Enter credits_used'}),
			

		} 
