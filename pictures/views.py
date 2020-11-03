from django.http import HttpResponse
import datetime
# Create your views here.


def current_datetime(request, pk):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)