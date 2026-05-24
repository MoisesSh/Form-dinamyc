from django.urls import path

from core.views.equipos_views import (
    EquipoHomologadoListView,
    EquipoHomologadoDetailView,
    MarcaListView,
    CategoriaListView,
    OrganismoListView,
)
from core.views.pdf_views import ComprobanteHomologacionPDFView

urlpatterns = [
    # Equipos homologados
    path('equipos-homologados/', EquipoHomologadoListView.as_view(), name='equipo-homologado-list'),
    path('equipos-homologados/<int:pk>/', EquipoHomologadoDetailView.as_view(), name='equipo-homologado-detail'),

    # Catálogos
    path('marcas/', MarcaListView.as_view(), name='marca-list'),
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('organismos/', OrganismoListView.as_view(), name='organismo-list'),

    # Generación de PDFs
    path('comprobante-homologacion/pdf/', ComprobanteHomologacionPDFView.as_view(), name='comprobante-homologacion-pdf'),
]
