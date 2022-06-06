import datetime
from multiprocessing import context
from .forms import LoginForm
from .forms import LoginForm, SignupForm
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import LoginForm, SignupForm, UserUpdateForm
from django.shortcuts import redirect, resolve_url
from django.views import generic
from .forms import LoginForm, SignupForm, UserUpdateForm, MyPasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy # 遅延評価用
from django.shortcuts import render
from django.http.response import HttpResponse


#トップページ
class TopView(generic.TemplateView):
    template_name = 'account/top.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_login =self.request.user.last_login.strftime('%d')
        now = datetime.datetime.now().strftime('%d')
        context['from_lastlogin'] = int(last_login) - int(now)
        return context


# ログイン
class Login(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'

# ログアウト
class Logout(LogoutView):
    template_name = 'account/logout_done.html'

# 自分しかアクセスできないようにするMixin(My Pageのため)
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']

# マイページ
class MyPage(OnlyYouMixin, generic.DetailView):
    # ユーザーモデルの取得
    User = get_user_model()
    model = User
    template_name = 'account/my_page.html'
    # モデル名小文字(user)でモデルインスタンスがテンプレートファイルに渡される


# サインアップ
class Signup(generic.CreateView):
    template_name = 'account/user_form.html'
    form_class =SignupForm

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        return redirect('account:signup_done')

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context

# サインアップ完了
class SignupDone(generic.TemplateView):
    template_name = 'account/signup_done.html'

# ユーザー登録情報の更新
class UserUpdate(OnlyYouMixin, generic.UpdateView):
# ユーザーモデルの取得
    User = get_user_model()
    model = User
    form_class = UserUpdateForm
    template_name = 'account/user_form.html'

    def get_success_url(self):
        return resolve_url('account:my_page', pk=self.kwargs['pk'])

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Update"
        return context

# パスワード変更
class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('account:password_change_done')
    template_name = 'account/user_form.html'

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Change Password"
        return context


# パスワード変更完了
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'
