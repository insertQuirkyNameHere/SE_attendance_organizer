from django.forms import ModelForm
from models.models import DepartmentMember
class DepartmentMemberCreationForm(ModelForm):
    class Meta:
        model = DepartmentMember
        fields = ['dept']
