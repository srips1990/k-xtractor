from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .core import compute
# Create your views here.

def home(req):
    resp = ""
    if req.method=='POST':
        job_desc = req.POST.get('job_desc', '')
        num_words = req.POST.get('num_words', '')
        file1_name, file2_name = compute(job_desc, num_words)
        params = {'file1_name': file1_name, 'file2_name': file2_name}
        resp = render(request=req, template_name='kxtractorApp/home.html', context=params)
    else:
        resp = render(req, 'kxtractorApp/home.html')

    return resp
    # HttpResponse(render(req,'resp.html'))

def process(req):
    job_desc = req.POST.get('job_desc', '')
    num_words = req.POST.get('num_words', '')
    file1_name, file2_name = compute(job_desc, num_words)
    params = {'file1_name': file1_name, 'file2_name': file2_name}
    return JsonResponse(params)

