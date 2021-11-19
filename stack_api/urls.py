
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import ProblemViewSet, ReplyViewSet, CommentViewSet

router = DefaultRouter()
router.register('problems', ProblemViewSet)
router.register('replies', ReplyViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
