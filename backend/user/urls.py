from django.urls import path

from user.views.ConsejoDirectivo_view import ConsejoDirectivoView

urlpatterns = [
    path('consejo-directivo/', ConsejoDirectivoView.as_view(), name='consejo-directivo'),
]
