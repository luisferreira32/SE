from django.views.generic import ListView, CreateView, DetailView
from .models import Post, Comment
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



class PostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'postdetail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        currentpost = get_object_or_404(Post, pk=self.kwargs['pk'])
        context['comment_list'] = Comment.objects.filter(related_post=currentpost)
        return context

    def commentpost(request, post_id):
        if request.user.is_authenticated:
            com = request.POST['com']
            post = get_object_or_404(Post, pk=post_id)
            commentpost = Comment(content=com,related_post=post,comment_owner=request.user)
            commentpost.save()
            return HttpResponseRedirect(reverse('apps:detail', args=[post_id]))
        else:
            return HttpResponseRedirect(reverse('login'))

    def upvote(request, post_id):
        if request.user.is_authenticated:
            post = get_object_or_404(Post, pk=post_id)
            post.upvotePost()
            return HttpResponseRedirect(reverse('apps:detail', args=[post_id]))
        else:
            return HttpResponseRedirect(reverse('login'))

    def downvote(request, post_id):
        if request.user.is_authenticated:
            post = get_object_or_404(Post, pk=post_id)
            post.downvotePost()
            return HttpResponseRedirect(reverse('apps:detail', args=[post_id]))
        else:
            return HttpResponseRedirect(reverse('login'))
