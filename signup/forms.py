from django import forms
from django.contrib.auth.models import User
from validate_email import validate_email # need to do pip install validate_email pyDNS

class SignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        '''
        Overridds the clean method
        '''
        cleaned_data = super(SignupForm, self).clean()
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')

        if not validate_email(email):
        # if not validate_email(email, verify=True):
        # Use this if you want to check if the e-mail is really in the server. But it works only with SMTP servers, not IMAP 
        # If you don't want to verify if the e-mail is there, then don't install pyDNS

            raise forms.ValidationError("Put a valid e-mail address")
        elif password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        else:
            return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
