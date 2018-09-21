from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from loginpage.models import Loginpage


class RegistrationForm(ModelForm):
    username  = froms.Charfield(label=(u'User Name'))
    email     = froms.EmailField(label=(u'Email Address'))
    password  = forms.CharField(label=(u'password'), widget=forms.PasswordInput(render_value=false))
    password1 = forms.CharField(label=(u'Verify password'), widget=forms.PasswordInput(render_value=false))

    class meta:
            model = Loginpage
            exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist :
            return username
        raise forms.ValidationError("Username taken")

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("PASSWORD DOES NOT MATCH")
        return self.cleaned_data
class Loginform(forms.Form)
    username = froms.Charfield(label=(u'User Name'))
    password = forms.CharField(label=(u'password'), widget=forms.PasswordInput(render_value=false))
