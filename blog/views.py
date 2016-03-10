from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Entry

def index(request):
    latest_posts = Entry.objects.order_by('-cdate')[:5]
    context = {'latest_posts': latest_posts}
    return render(request, 'blog/index.html', context)
