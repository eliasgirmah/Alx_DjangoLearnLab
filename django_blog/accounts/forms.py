from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        email = self.cleaned_data.get('email')
        if email and self.instance.user:
            self.instance.user.email = email
            self.instance.user.save()
        if commit:
            profile.save()
        return profile
