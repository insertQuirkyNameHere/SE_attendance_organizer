from django.forms import ModelForm
from models.models import Clubs

class ClubCreationForm(ModelForm):
    class Meta:
        model = Clubs
        fields = ['name']