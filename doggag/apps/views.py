from django.views.generic.list import ListView
from .models import Post

class ScrollView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'posts'
    template_name = 'home.html'
