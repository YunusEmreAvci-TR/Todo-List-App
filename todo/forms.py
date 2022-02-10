from django import forms
from .models import Todos

class CreateForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ('title', 'description',)