from this import d
from django.views.generic import ListView, TemplateView
from .models import (
    Person,
    Reunion
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,  # Equivalente al detailview
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView  # Trae los datos y luego los actualiza


)

from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    ReunionSerializer,
    PersonSerializerHobbie,
    ReunionSerializer2,
    ReunionSerializerLink,
    HobbySerializer,
    PersonaLink,
    PersonPagination,
    CountReunionSerializer

)


class PersonaListView(ListView):
    template_name = 'persona/personas.html'
    model = Person
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()


class PersonaListAPIView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer


class PersonRetrieveAPIView(RetrieveAPIView):

    serializer_class = PersonSerializerHobbie
    queryset = Person.objects.all()


class PersonDeleteAPIView(DestroyAPIView):
    seriazer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonUpdateAPIView(UpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonListaAPIView(ListAPIView):
    serializer_class = PersonaSerializer

    def get_queryset(self):
        return Person.objects.all()


class ReunionAPIList(ListAPIView):
    serializer_class = ReunionSerializer

    def get_queryset(self):
        return Reunion.objects.all()


class PersonaListAPIViewHobbie(ListAPIView):
    serializer_class = PersonSerializerHobbie

    def get_queryset(self):
        return Person.objects.all()


class ReunionAPIList2(ListAPIView):
    serializer_class = ReunionSerializer2

    def get_queryset(self):
        return Reunion.objects.all()


class ReunionAPIListLink(ListAPIView):
    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        return Reunion.objects.all()


class HobbyDetailAPIView(RetrieveAPIView):
    serializer_class = HobbySerializer
    queryset = Person.objects.all()


class PersonaAPIListLink(ListAPIView):
    serializer_class = PersonaLink

    def get_queryset(self):
        return Person.objects.all()


class PersonPaginationListAPIView(ListAPIView):
    """Paginación en listas"""
    serializer_class = PersonSerializer
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()


class ReunionByJobs(ListAPIView):
    serializer_class = CountReunionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones()
