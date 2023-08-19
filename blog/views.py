from django.shortcuts import render, get_object_or_404
from .models import Post
    # needed for the first detail method
# from django.http import Http404

# Create your views here.
def post_list(request):
    posts = Post.Published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_details(request, id):
    # try:
        # post = Post.Published.get(id = id)
    # except Post.DoesNotExist:
    #     raise http404('Post not found')
            # or the one bellow
    post = get_object_or_404( Post,
                                 id = id,
                                 status = Post.status.PUBLISHED)
    return render(request,
                'blog/post/list.html',
                {'posts': posts})