from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post/', views.post_question, name='post_question'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/<int:pk>/answer/', views.answer_question, name='answer_question'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
]
