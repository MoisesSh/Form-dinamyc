from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from core.models.tecnico_models import Equipo, Marca, Organismo
from core.models.analisis_models import Categoria
from core.serializers.equipos_serializers import (
    EquipoHomologadoListSerializer,
    EquipoHomologadoDetailSerializer,
    MarcaSerializer,
    CategoriaSerializer,
    OrganismoSerializer,
)



class EquipoHomologadoListView(generics.ListAPIView):
    """Listado paginado de equipos con homologación aprobada."""
    serializer_class = EquipoHomologadoListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['marca']
    search_fields = ['marca', 'modelo', 'cod_equipo']

    def get_queryset(self):
        return (
            Equipo.objects
            .filter(homologacion__estatus__nombre='APROBADO')
            .select_related('homologacion', 'homologacion__estatus')
            .order_by('-homologacion__fecha_emision')
        )


class EquipoHomologadoDetailView(generics.RetrieveAPIView):
    """Detalle completo de un equipo homologado."""
    serializer_class = EquipoHomologadoDetailSerializer

    def get_queryset(self):
        return (
            Equipo.objects
            .filter(homologacion__estatus__nombre='APROBADO')
            .select_related('homologacion', 'homologacion__estatus')
            .prefetch_related(
                'certificados', 'certificados__estatus',
                'parametros_transmision',
                'parametros_recepcion',
                'interfaces_alambricas',
                'evaluaciones',
                'certificaciones_externas', 'certificaciones_externas__organismo',
            )
        )




class MarcaListView(generics.ListAPIView):
    """Listado de marcas."""
    serializer_class = MarcaSerializer
    queryset = Marca.objects.all().order_by('nombre')
    pagination_class = None


class CategoriaListView(generics.ListAPIView):
    """Listado de categorías con subcategorías anidadas."""
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.prefetch_related('subcategoria_set').order_by('id')
    pagination_class = None


class OrganismoListView(generics.ListAPIView):
    """Listado de organismos certificadores."""
    serializer_class = OrganismoSerializer
    queryset = Organismo.objects.all().order_by('nombre')
    pagination_class = None
