from django.http import HttpResponse, HttpResponseRedirect
from  django.shortcuts import render
import datetime
from .forms import NameForm
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
