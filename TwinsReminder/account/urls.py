from django.urls import path, include
from . import views


# トップページの設定
app_name ='account'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'), # ログイン
    path('logout/', views.Logout.as_view(), name='logout'), # ログアウト
    path('my_page/<int:pk>/', views.MyPage.as_view(), name='my_page'), # マイページ
]