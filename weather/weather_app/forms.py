from django.forms import ModelForm,TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model=City
        fields=['name']
        widgest={'name':TextInput(attrs={'class':'input','placeholder':'Enter city name'})}
