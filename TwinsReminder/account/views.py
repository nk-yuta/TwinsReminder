from .forms import LoginForm
from django.shortcuts import redirect # 追加
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model # 追加
from django.contrib.auth.mixins import UserPassesTestMixin # 追加
from django.views import generic


#トップページ
class TopView(generic.TemplateView):
    template_name = 'account/top.html'

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


    template_name = 'account/signup_done.html'