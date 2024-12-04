from django.shortcuts import render, redirect

from .forms import RequestForm
from .models import Request

def request_list(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        form.save()
        return redirect('request_list.html')

    requests = Request.objects.all()
    form = Request()
    context = {'requests': requests, 'form': form}
    return render(request, "request_list.html", context)


def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        form.save()
        return redirect('request_list')

    form = RequestForm()
    data = {
        'form': form
    }
    return render(request, "create_request.html", data)

