from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'ttours'
urlpatterns = [
    path('', views.IndexView.as_view(), name='ttindex'),
    path('<int:pk>/', views.SeasonView.as_view(), name='season'),
    path('<int:pk>/match', views.MatchView.as_view(), name='match',),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)