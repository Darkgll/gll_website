from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from users.models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            
        self.fields['username'].widget.attrs.update({'placeholder': 'Your Login Username', 'type': 'text'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your Email address', 'type': 'email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Your password', 'type': 'password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password', 'type': 'password'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'short_info', 'interests_info', 'profile_image']
