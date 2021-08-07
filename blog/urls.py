from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import*

router = DefaultRouter()
router.register('post', PostView)
router.register('comment', CommentView)

urlpatterns = [
    path('', include(router.urls)),
    path('getcomment/<int:user_id>/', GetCommentView),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]