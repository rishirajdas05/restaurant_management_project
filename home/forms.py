from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["comment"]
        widgets = {
            "comment": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Share your feedback…",
                "style": "width:100%; padding:12px; border-radius:8px; border:1px solid #ccc;"
            })
        }
        labels = {
            "comment": "Your feedback"
        }