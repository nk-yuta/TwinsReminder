from django.urls import path, include
from . import views


# トップページの設定
app_name ='account'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'), # ログイン
    path('logout/', views.Logout.as_view(), name='logout'), # ログアウト
    path('my_page/<int:pk>/', views.MyPage.as_view(), name='my_page'), # マイページ
    path('signup/', views.Signup.as_view(), name='signup'), # サインアップ
    path('signup_done/', views.SignupDone.as_view(), name='signup_done'), # サインアップ完了
    path('user_update/<int:pk>', views.UserUpdate.as_view(), name='user_update'), # 登録情報の更新
    path('password_change/', views.PasswordChange.as_view(), name='password_change'), # パスワード変更
    path('password_change_done/', views.PasswordChangeDone.as_view(), name='password_change_done'), # パスワード変更完了
]