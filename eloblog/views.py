from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Entry
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


postsPerPage = 5

def index(request):
    latest_posts = Entry.objects.order_by('-cdate')[:postsPerPage]
    hasNext = True if Entry.objects.count() > postsPerPage else False
    return render(request, 'index.html', {'latest_posts': latest_posts, 'hasNext' : hasNext})

def post(request, entry_id):
    post = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'post.html', {'post': post})

def about(request):
    return render(request, 'about.html')

def page(request, pagenum):

    posts = Entry.objects.order_by('-cdate')
    paginator = Paginator(posts, 5)
    try:
        postlist = paginator.page(pagenum)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        postlist = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        postlist = paginator.page(paginator.num_pages)
        
    return render(request, 'page.html', {'postlist':postlist})
