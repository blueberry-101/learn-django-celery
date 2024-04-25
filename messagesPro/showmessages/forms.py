from django import forms
from showmessages.models import UserModel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"