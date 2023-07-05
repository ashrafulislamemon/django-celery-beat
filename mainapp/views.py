from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from .tasks import run_script1_and_save_output


def test_scripts(request):
    run_script1_and_save_output.delay()
    return HttpResponse("Done")