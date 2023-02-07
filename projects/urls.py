from rest_framework_nested import routers
from . import views

router = routers.SimpleRouter()
router.register('projects', views.ProjectViewSet, basename='projects')

project_router = routers.NestedSimpleRouter(router, 'projects', lookup='project')
project_router.register('reviews', views.ReviewViewSet, basename='project-reviews')

urlpatterns = router.urls + project_router.urls

