from django.views.generic import ListView, CreateView, DetailView
from .models import Post, Comment
from .forms import PostForm

from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class ScrollView(ListView):
    """ Extension of a generic list view to display all posts by upvotes """
    model = Post
    paginate_by = 5
    context_object_name = 'posts'
    template_name = 'home.html'

    def get_queryset(self):
        """ Do a query organized by voting """
        return Post.objects.order_by('-votes')

    def upvote(request, post_id):
        """ Upvote a post, i.e. give +1 vote to a post if user is authenticated """
        if request.user.is_authenticated:
            post = get_object_or_404(Post, pk=post_id)
            post.upvotePost()
            return HttpResponseRedirect(reverse('apps:home'))
        else:
            return HttpResponseRedirect(reverse('login'))

    def downvote(request, post_id):
        """ Downvote a post, i.e. give -1 vote to a post if user is authenticated """
        if request.user.is_authenticated:
            post = get_object_or_404(Post, pk=post_id)
            post.downvotePost()
            return HttpResponseRedirect(reverse('apps:home'))
        else:
            return HttpResponseRedirect(reverse('login'))



class CreatePostView(CreateView):
    """ Extension of a generic create view to upload a post to the site """
    model = Post
    form_class = PostForm
    template_name = 'upload.html'
    success_url = reverse_lazy('apps:home')

    def form_valid(self, form):
        """ Make the user who uploaded it the owner of the post """
        obj = form.save(commit=False)
        obj.post_owner = self.request.user
        obj.save()
        return HttpResponseRedirect(self.success_url)



class PostView(DetailView):
    """ Extension of a generic detail view to display the post with all its comments """
    model = Post
    context_object_name = 'post'
    template_name = 'postdetail.html'

    def get_context_data(self, **kwargs):
        """ Get the related comments to the post besides the post itself and return the context variable """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        currentpost = get_object_or_404(Post, pk=self.kwargs['pk'])
        context['comment_list'] = Comment.objects.filter(related_post=currentpost)
        return context

    def commentpost(request, post_id):
        """ Comment a post if user is authenticated """
        if request.user.is_authenticated:
            com = request.POST['com']
            post = get_object_or_404(Post, pk=post_id)
            commentpost = Comment(content=com,related_post=post,comment_owner=request.user)
            commentpost.save()
            return HttpResponseRedirect(reverse('apps:detail', args=[post_id]))
        else:
            return HttpResponseRedirect(reverse('login'))

    def upvote(request, post_id):
        """ Upvote a post, i.e. give +1 vote to a post if user is authenticated """
        if request.user.is_authenticated:
            post = get_object_or_404(Post, pk=post_id)
            post.upvotePost()
            return HttpResponseRedirect(reverse('apps:detail', args=[post_id]))
        else:
            return HttpResponseRedirect(reverse('login'))

    def downvote(request, post_id):
        """ Downvote a post, i.e. give -1 vote to a post if user is authenticated """
        if request.user.is_authenticated:
            post = get_object_or_404(Post, pk=post_id)
            post.downvotePost()
            return HttpResponseRedirect(reverse('apps:detail', args=[post_id]))
        else:
            return HttpResponseRedirect(reverse('login'))
