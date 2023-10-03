import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='logger.log', filemode='a', format='%(levelname)s %(message)s')


def seminar5(request):
    logger.info(f'{request} request received')
    return HttpResponse('<h1>Seminar5</h1>')


from django.shortcuts import render
from django import forms
from .models import Data


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"


def home_page(request):
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SalaryForm()
    return render(request, 'home_page.html', {'form': form})
