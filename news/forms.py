from news.models import ContactUs, Subscribe
from django import forms

"""
contact us form
"""
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('first_name','last_name','email','phone','feedback_message')


"""
Subscribe form
"""      
class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ("email",)