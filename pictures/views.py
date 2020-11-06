from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime

from django.urls import reverse

from .forms import NameForm, ContactForm, PictureForm
from django.core.mail import send_mail
from  .models import Picture
from  django.forms import  modelformset_factory
# Create your views here.


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('pictures'))
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ["olrgparistokrat@gmail.com"]

            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect(reverse('pictures'))
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def pictures(request):
    PictureFormSet = modelformset_factory(Picture, form=PictureForm, extra=2, max_num=20)
    if request.method == 'POST':
        formset = PictureFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    print(form.save())
    else:
        formset = PictureFormSet()
    return render(request, 'pictures.html', {'formset': formset})


def get_picture(request, pk):
    picture = Picture.objects.get(pk=pk)
    if request.method == 'POST':
        form = PictureForm(request.POST, instance=picture)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pictures'))
    else:
        form = PictureForm(instance=picture)
    return render(request, 'picture.html', {'form': form})
