from django.forms import ModelForm
from .models import UserRegistration

class MyForm(ModelForm):
    class Meta:
        model=UserRegistration
        fields=['username','usernumber','useremail','date']