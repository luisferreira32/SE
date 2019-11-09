from django.views.generic.list import ListView
from .models import Post
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

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

def upload(request):
    context = {} #this line if want to display name of uploaded file
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        #to display uploaded file name in html view
        context['url'] = fs.url(name)
    return render(request,'upload.html',context)
