from rest_framework import serializers
from user.models import ConsejoDirectivo

class ConsejoDirectivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsejoDirectivo
        fields = '__all__'

    