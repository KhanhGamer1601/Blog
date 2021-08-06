from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import*

router = DefaultRouter()
router.register('post', PostView)
router.register('comment', CommentView)

urlpatterns = [
    path('', include(router.urls)),
    path('GetComment/<int:user_id>/', GetCommentView),
]