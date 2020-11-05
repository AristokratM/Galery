from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime

from django.urls import reverse

from .forms import NameForm, ContactForm, PictureForm, HallForm
from django.core.mail import send_mail
from  .models import Picture
# Create your views here.


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/picture/1/')
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
            return HttpResponseRedirect('/picture/1/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def picture_form(request):
    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            picture = form.save()
            return HttpResponseRedirect(reverse('picture', args=(picture.id,)))
    else:
        form = PictureForm()
    return render(request, 'pictures.html', {'form': form})


def get_picture(request, pk):
    picture = Picture.objects.get(pk=pk)
    return render(request, 'picture.html', {'picture': picture})
