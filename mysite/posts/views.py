from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from django.views import View


from .forms import PostForm
from .models import Post, Like, Comment

# Create your views here.


class New(CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:index')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(New, self).form_valid(form)


class Index(ListView):
    model = Post
    template_name = 'posts/index.html'
    #paginate_by = 20
    queryset = Post.objects.order_by('created_at').reverse()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        like_list = {}
        comment_list = {}
        comment_list2 = {}
        login_user = self.request.user
        # すでに取得されている投稿リストを一件づつ取り出す
        for post in context['post_list']:
            # 取り出したものから「いいね!」を探してlike_listに格納する
            like_list[post.id] = Like.objects.filter(post=post)
            comment_list[post.id] = Comment.objects.filter(post=post)
        for post in context['post_list']:
            comments = []
            for comment in comment_list[post.id]:
                if post.author.id == login_user.id or comment.author.id == login_user.id:
                    comments.append(comment)
            comment_list2.update({post.id: comments})
        context['like_list'] = like_list
        context['login_user'] = login_user
        context['comment_list'] = comment_list2
        return context


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:index')
    template_name = 'posts/delete.html'


class Likes(View):
    model = Like

    slug_field = 'post'

    slug_url_kwarg = 'postId'

    def get(self, request, postId):
        post = Post.objects.get(id=postId)

        like = Like.objects.filter(author=self.request.user, post=post)

        like_list = {}
        comment_list = {}

        if like.exists():
            like.delete()
        else:
            like = Like(author=self.request.user, post=post)
            like.save()

        like_list[post.id] = Like.objects.filter(post=post)

        comment_list[post.id] = Comment.objects.filter(post=post)

        return render(request, 'posts/like.html', {
            'like_list': like_list,
            'post': post,
            'comment_list': comment_list
        })


class AddComment(View):

    def post(self, request, postId):
        like_list = {}
        comment_list = {}

        post = Post.objects.get(id=postId)

        text = request.POST["comment"]

        comment = Comment(author=self.request.user, post=post, text=text)

        comment.save()

        like_list[post.id] = Like.objects.filter(post=post)

        comment_list[post.id] = Comment.objects.filter(post=post)

        return render(request, 'posts/like.html', {
            'like_list': like_list,
            'post': post,
            'comment_list': comment_list
        })
