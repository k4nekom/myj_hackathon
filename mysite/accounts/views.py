from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from .forms import SignUpForm
from .models import User
# サインアップ画面
class SignUpView(generic.CreateView):
    # 使うformクラス設定
    form_class = SignUpForm
    # 使うテンプレートファイル設定
    template_name = 'login/signup.html'
    # 成功時にログイン処理を行ってAccountDetailViewに飛ぶ
    def get_success_url(self):
        form = self.get_form()
        # usernameから登録したユーザー情報を参照
        user = User.objects.get(username=form.data.get('username'))
        # ログイン処理を行う
        login(self.request, user)
        return reverse(
            'accounts:userdetail',
            kwargs={'username': user.username })
# アカウント詳細画面設定
class AccountDetailView(DetailView):
    model = User
    # urlのパスクエリを引数に取る(後述)
    slug_field = 'username'
    slug_url_kwarg = 'username'