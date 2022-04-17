from django.shortcuts import get_object_or_404, render
from .forms import CommentForm
from .models import Post
from django.core.paginator import Paginator

# Create your views here.


def postlist(request):
    # === Popular posts ===
    popularposts = Post.objects.filter(status=1).order_by('-created_on')

    # ===  Search Function ===
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query) or Post.objects.filter(
            content__icontains=query)
    else:
        posts = Post.objects.filter(status=1).order_by('-created_on')

    # === pagination ===
    page = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)

    return render(request, 'index.html', {'posts': posts, 'page_obj': page_obj, 'popularposts': popularposts})


# === post detail function ===
def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    popularposts = Post.objects.filter(status=1).order_by('-created_on')
    comments = post.comments.filter(active=True)
    new_comment = None

    # comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # create comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment
            new_comment.post = post
            # save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'popularposts': popularposts,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
