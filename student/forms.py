from django.forms import ModelForm
from models.models import Students

class StudentCreationForm(ModelForm):
    class Meta:
        model = Students
        fields = ['dept']
        
