from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from .forms import NameForm, ContactForm
from django.core.mail import send_mail
# Create your views here.


def current_datetime(request, pk):
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
