from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.views.generic.edit import UpdateView

from .forms import SignUpForm
from .models import User
from posts.models import Post, Comment
from posts.views import Index
# サインアップ画面


class SignUpView(generic.CreateView):
    # 使うformクラス設定
    form_class = SignUpForm
    # 使うテンプレートファイル設定
    template_name = 'registration/signup.html'
    # 成功時にログイン処理を行ってAccountDetailViewに飛ぶ

    def get_success_url(self):
        form = self.get_form()
        # usernameから登録したユーザー情報を参照
        user = User.objects.get(username=form.data.get('username'))

        # ログイン処理を行う
        login(self.request, user)
        return reverse(
            'accounts:userdetail',
            kwargs={'username': user.username})
# アカウント詳細画面設定


class AccountDetailView(DetailView):
    model = User
    # urlのパスクエリを引数に取る(後述)
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['login_user'] = self.request.user
        context['post_list'] = Post.objects.all()
        login_user = self.request.user
        comment_list = {}
        comment_list2 = {}

        for post in context['post_list']:
            comment_list[post.id] = Comment.objects.filter(post=post)
        for post in context['post_list']:
            comments = []
            for comment in comment_list[post.id]:
                if post.author.id == login_user.id or comment.author.id == login_user.id:
                    comments.append(comment)
            comment_list2.update({post.id: comments})
        context['comment_list'] = comment_list2
        return context


class IconEdit(UpdateView):
    model = User
    template_name = 'accounts/icon_edit.html'
    fields = ['icon', 'message', 'twitter_url']

    def get_object(self):
        # ログイン中のユーザーで検索することを明示する
        return self.request.user

    def get_success_url(self):
        form = self.get_form()
        return reverse(
            'accounts:userdetail',
            kwargs={'username': self.request.user.username})
