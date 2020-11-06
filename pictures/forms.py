from django import forms
from django.forms import ModelForm, Textarea
from .models import Picture, Hall
from django.utils.translation import gettext_lazy as _


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = '__all__'
        labels = {
            'name': _('Picture Name'),
        }
        help_texts = {
            'name': _("It's a picture name"),
        }
        error_messages = {
            'name': {
                'max_length': _("This picture name is too long"),
            }
        }


class HallForm(ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'
