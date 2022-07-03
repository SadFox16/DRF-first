from django.contrib import admin
from django.urls import path, include
from women.views import WomenAPIList, WomenAPIUpdate, WomenAPIDetailView, WomenAPIDestroy
#from women.views import WomenViewSet
from rest_framework import routers
from rest_framework import urls


#создаем и регистрируем роутер
# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet, basename='women')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women-auth/', include('rest_framework.urls')), #http://127.0.0.1:8000/api/v1/women-auth/login/ для регистрации
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    #path('api/v1/', include(router.urls)), #http://127.0.0.1:8000/api/vi/women/
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    # path('api/v1/womenlist/', WomenAPIList.as_view()),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
]
