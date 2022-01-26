from dataclasses import fields
from rest_framework import serializers, pagination
from .models import Hobby, Person, Reunion


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')


class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    estado = serializers.BooleanField(required=False)


class ReunionSerializer(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=False)
    persona = PersonaSerializer()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'activo'
        )


class HobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby
        fields = ('__all__')


class PersonSerializerHobbie(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobby'

        )


class ReunionSerializer2(serializers.ModelSerializer):

    # Campos que sea nresultado de operar campos ya existentes
    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'fecha_hora'

        )

    def get_fecha_hora(self, obj):
        # Obj hace referencia al objeto que se esta iterando.
        return str(obj.fecha) + '-' + str(obj.hora)


class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',

        )
        extra_kwargs = {
            'persona': {
                'view_name': 'personas_app:detail',
                'lookup_field': 'pk'
            }
        }


class PersonaLink(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobby'

        )
        extra_kwargs = {
            'hobby': {
                'view_name': 'personas_app:detail-hobby',
                'lookup_field': 'pk'
            }
        }


class PersonPagination(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 100


class CountReunionSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()
