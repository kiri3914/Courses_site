from django.shortcuts import render
from .models import Course
def index(request):

    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'index.html', context=context)
