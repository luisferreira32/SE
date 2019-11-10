from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm

from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class ScrollView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'posts'
    template_name = 'home.html'

    def upvote(request, post_id):
        if request.user.is_authenticated:
            post = get_object_or_404(Post, pk=post_id)
            post.upvotePost()
            return HttpResponseRedirect(reverse('apps:home'))
        else:
            return HttpResponseRedirect(reverse('login'))

    def downvote(request, post_id):
        if request.user.is_authenticated:
            post = get_object_or_404(Post, pk=post_id)
            post.downvotePost()
            return HttpResponseRedirect(reverse('apps:home'))
        else:
            return HttpResponseRedirect(reverse('login'))

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'upload.html'
    success_url = reverse_lazy('apps:home')
