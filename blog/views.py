from django.shortcuts import render
from .models import Post
from django.views import generic
# from django.db.models import QuerySet
# Create your views here.

class PostList(generic.ListView):
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html/"
    
    # For the search bar
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.filter(status=1).order_by('-created_on')

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html/"


