from django import forms

from .models import ContactMessage, Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "email", "phone", "rating", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}
        labels = {"name": "Your name (optional)", "email": "Email (optional)",
                  "phone": "Phone (optional)", "message": "Your feedback"}


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}
