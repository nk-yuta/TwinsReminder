from .forms import LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView, LogoutView
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