"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from taskboardapp.views import WorkProjectViewSet, TaskBoardViewSet
from usersapp.views import UserViewSet
#from usersapp.views import UserModelViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('project', WorkProjectViewSet)
router.register('taskboard', TaskBoardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    re_path(r'^api/(?P<version>.\d)', UserViewSet.as_view({'get': 'list'}))
    # path('api/get/', UserViewSet.as_view()),
    # path('api/get/<int:pk>/', UserViewSet.as_view()),
    # path('api/post/', post_view)
]
