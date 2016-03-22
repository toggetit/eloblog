from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Entry
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    latest_posts = Entry.objects.order_by('-cdate')[:5]
    context = {'latest_posts': latest_posts}
    return render(request, 'blog/index.html', context)

def post(request, entry_id):
    post = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blog/post.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')

def listing(request, pagenum):
    posts = Entry.objects.order_by('-cdate')
    paginator = Paginator(posts, 5) # Show 10 contacts per page

    #page = request.GET.get('page')
    try:
        postlist = paginator.page(pagenum)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        postlist = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        postlist = paginator.page(paginator.num_pages)
        
    return render(request, 'blog/page.html', {'postlist':postlist})
