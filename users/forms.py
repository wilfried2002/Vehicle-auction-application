from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, label="Je suis")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)

            profile.role = self.cleaned_data['role']
            profile.save()
        return user

