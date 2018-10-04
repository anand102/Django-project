from django import forms
from . import models

class CreateSocio(forms.ModelForm):
	class Meta:
		model = models.Social
		fields = ['title','body','slug','thumb']