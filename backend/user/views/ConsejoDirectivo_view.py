from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from user.models.firmar_models import ConsejoDirectivo
from user.serializers.ConsejoDirectivo_serializers import ConsejoDirectivoSerializer

class ConsejoDirectivoView(GenericAPIView):
    serializer_class = ConsejoDirectivoSerializer

    def get(self, request):

        consejo = ConsejoDirectivo.objects.filter(is_active=True).first()
        if consejo:
            serializer = self.get_serializer(consejo)
            return Response(serializer.data)
        return Response({'message': 'No se encontro ningun consejo directivo activo'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Consejo directivo creado exitosamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)