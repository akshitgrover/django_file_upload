from django import forms

class uploadForm(forms.Form):
	name = forms.CharField()
	file = forms.FileField()