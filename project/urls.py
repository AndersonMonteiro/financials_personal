from django.urls import path, include
from graphene_django.views import GraphQLView
from django.contrib import admin

urlpatterns = [
    path('', include('api.urls'), name='Financas'),
    path('graphql', GraphQLView.as_view(graphiql=True)),
    path('admin', admin.site.urls),
]
