from django.shortcuts import get_object_or_404, render

from .forms import CommentForm
from .models import Post
from django.views import generic
# Create your views here.

class PostList(generic.ListView):
    template_name = "index.html/"
    paginate_by = 9

    # For the search bar
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Post.objects.filter(title__icontains=query) or Post.objects.filter(content__icontains=query)
        else:
            object_list = Post.objects.filter(status=1).order_by('-created_on')

        return object_list

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html/"

def post_detail(request,slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post,slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    #comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            #create comment object but dont save to database yet
            new_comment = comment_form.save(commit=False)
            #assign the current post to the comment
            new_comment.post = post
            #save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()
    return render (request,template_name,{'post': post,
                                            'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form})



