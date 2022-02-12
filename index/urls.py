from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('check_health/', views.check_health, name="check_health"),
    path('userid/', views.user_login, name="user_login"),
    path('result/', views.result, name="result"),
    path('all-result/', views.all_result, name="all_result"),
    path('result_chart/', views.chart, name="result_chart"),
    path('about/', views.about, name="about")
]
