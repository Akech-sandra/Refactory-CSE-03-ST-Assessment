from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from.models import *
from.forms import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your views here.

def std_app(request):
    if request.method == 'POST':
        form = Std_ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been submitted successfully! ')
            # return redirect('')
    else:
        form = Std_ApplicationForm()

    return render(request, 'myapp/stdapp.html', {'form': form})
