from django import forms
from .models import ContactForm
from django_recaptcha.fields import ReCaptchaField


class ContactFormClass(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'message', 'captcha')
        widgets = {
        'name': forms.TextInput(attrs={'id': 'name', 'placeholder':'Name', 'type':'text'}),
        'email': forms.EmailInput(attrs={'id': 'email', 'placeholder':'Email', 'type':'email'}),
        'message': forms.Textarea(attrs={'id': 'message', 'placeholder':'Message'}),
        }