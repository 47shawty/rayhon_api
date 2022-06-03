from django.urls import path
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register("product", views.ProductViewSet, 'products')
router.register("category", views.CategoryViewSet, 'category')
router.register("top_worker", views.TopWorkerViewSet, 'top_worker')
router.register("statistics", views.StatisticsViewSet, 'statistics')
router.register("review", views.ReviewViewSet, 'review')


urlpatterns = router.urls
