from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .core import compute
from . import validate
from . import customExceptions
import logging
# Create your views here.
logger = logging.getLogger(__name__)


def home(req):
    resp = ""
    if req.method == 'POST':
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
    try:
        job_desc = req.POST.get('job_desc', '')
        num_words = req.POST.get('num_words', '')
        if not validate.validate_job_description(job_desc):
            err_obj = customExceptions.get_validation_exception_obj(
                "Should be less than 10000 characters, but not empty", "job_desc"
            )
            raise Exception(err_obj)
        if not validate.validate_num_words(num_words):
            err_obj = customExceptions.get_validation_exception_obj(
                "Number should be a valid integer between 1 and 100", "num_words"
            )
            raise Exception(err_obj)

        file1_name, file2_name = compute(job_desc, num_words)
        params = {'file1_name': file1_name, 'file2_name': file2_name}
        return JsonResponse(params)
    except Exception as e:
        if hasattr(e, 'args') and e.args[0]:
            if isinstance(e.args[0], str):
                return JsonResponse({'error': e.args[0]}, status=500)
                logger.error(e.args[0])
            else:
                return JsonResponse(e.args[0], status=500)
                logger.error(e.args[0])
        else:
            return JsonResponse({'error': 'Internal Server Error'}, status=500)