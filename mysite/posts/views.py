from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post
# Create your views here.

class New(CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:index')

    def form_valid(self,form):
        form.instance.author_id = self.request.user.id
        return super(New,self).form_valid(form)

class Index(ListView):
    model = Post
    template_name = 'posts/index.html'
    #paginate_by = 20
    queryset = Post.objects.order_by('created_at').reverse()
