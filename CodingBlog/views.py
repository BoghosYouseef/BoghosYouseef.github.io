from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    context = {}
    return render(request=request, template_name="mainCodingBlog.html", context=context)

    # return HttpResponse("SUCCESS!")