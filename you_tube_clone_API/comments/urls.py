from django.urls import path
from . import views


urlpatterns = [
    path('comments/', views.VideoComments.as_view()),
    path('comments/<str:video>', views.VideoCommentsDetail.as_view()),
    path('replies/', views.Replies.as_view())
]