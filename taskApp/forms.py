from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Project, Task

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    dob = forms.DateField(required=True)
    skills = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user.profile.dob = self.cleaned_data["dob"]
            user.profile.skills = self.cleaned_data["skills"]
            user.profile.save()
        return user

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'deadline']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']
