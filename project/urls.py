from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('api.urls'), name='Financas'),
    path('admin', admin.site.urls),
]
