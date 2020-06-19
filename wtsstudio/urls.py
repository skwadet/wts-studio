from django.contrib import admin
from django.urls import path, include
from wtsstudio_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'header', views.HeaderAPISet, basename='headerapi')
router.register(r'logo', views.LogoAPISet, basename='logoapi')
router.register(r'description', views.DescriptionAPISet, basename='descriptionapi')
router.register(r'pros', views.ProsAPISet, basename='prosapi')
router.register(r'header', views.HeaderAPISet, basename='headerapi')
router.register(r'service', views.ServiceAPISet, basename='serviceapi')
router.register(r'create', views.UserRequestAPISet, basename='userrequestapi')
router.register(r'review', views.ReviewAPISet, basename='reviewapi')
router.register(r'brief', views.BriefAPISet, basename='briefapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
