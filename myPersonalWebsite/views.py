from django.shortcuts import render


def home(request):
    context = {}
    # TODO
    return render(request=request, template_name="main.html", context=context)
