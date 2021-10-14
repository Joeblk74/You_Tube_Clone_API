from django.urls import path
from . import views


urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('replies/', views.RepliesList.as_view())
]