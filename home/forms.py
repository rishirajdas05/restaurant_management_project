from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email"]
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Your name",
                "class": "form-control"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Your email",
                "class": "form-control"
            }),
        }