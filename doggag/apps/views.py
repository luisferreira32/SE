from django.views.generic.list import ListView
from .models import Post
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

class ScrollView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'posts'
    template_name = 'home.html'

    def upvote(request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.upvotePost()
        return HttpResponseRedirect(reverse('apps:home'))

    def downvote(request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.downvotePost()
        return HttpResponseRedirect(reverse('apps:home'))
