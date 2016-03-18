from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Entry
from django.shortcuts import get_object_or_404

def index(request):
    latest_posts = Entry.objects.order_by('-cdate')[:5]
    context = {'latest_posts': latest_posts}
    return render(request, 'blog/index.html', context)

def post(request, entry_id):
    post = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blog/post.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')

def prevposts(request, page):
    if (page == '0') or (page == '1'):
        return index(request)
    else:
        return HttpResponse(page)
