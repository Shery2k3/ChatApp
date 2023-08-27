from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        print(self.fields['password1'].help_text)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
