from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from taskboardapp.views import WorkProjectViewSet, TaskBoardViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from usersapp.views import UserViewSet
#from usersapp.views import UserModelViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='TaskBoard',
        default_version='v1',
        description='',
        contact=openapi.Contact(email='test@test.com'),
        license=openapi.License(name='MIT')
    ),
    public=True,
    permission_classes=(AllowAny,)
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('project', WorkProjectViewSet)
router.register('taskboard', TaskBoardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    # re_path(r'^api/(?P<version>.\d)', UserViewSet.as_view({'get': 'list'})),
    # path('api/usersv1', include('usersapp.urls', namespace='v1')),
    # path('api/usersv2', include('usersapp.urls', namespace='v2')),
    # path('api/get/', UserViewSet.as_view()),
    # path('api/get/<int:pk>/', UserViewSet.as_view()),
    # path('api/post/', post_view)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0))
]
