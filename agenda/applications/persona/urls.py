from django.urls import path, re_path
from . import views

app_name = 'personas_app'

urlpatterns = [
    path(
        'personas/',
        views.PersonaListView.as_view(),
        name='personas'
    ),

    path(
        'api/persona/lista',
        views.PersonaListAPIView.as_view(),

    ),


    path(
        'api/persona/create/',
        views.PersonCreateView.as_view(),
        name='create'
    ),
    path(
        'api/persona/detail/<pk>/',
        views.PersonRetrieveAPIView.as_view(),
        name='detail'
    ),
    path(
        'api/persona/delete/<pk>/',
        views.PersonDeleteAPIView.as_view(),
        name='delete'
    ),

    path(
        'api/persona/update/<pk>/',
        views.PersonUpdateAPIView.as_view(),
        name='update'
    ),

    path(
        'api/persona/modificar/<pk>/',
        views.PersonRetrieveUpdateAPIView.as_view(),
        name='modificar'
    ),
    path(
        'api/persona/lista-persona/',
        views.PersonListaAPIView.as_view(),
        name='lista-persona'
    ),

    path(
        'api/reunion/lista/',
        views.ReunionAPIList.as_view(),
        name='reunion'
    ),
    path(
        'api/persona-hobbie/lista/',
        views.PersonaListAPIViewHobbie.as_view(),
        name='hobbie'
    ),
    path(
        'api/reunion/lista2/',
        views.ReunionAPIList2.as_view(),
        name='reunion'
    ),
    path(
        'api/reunion/listalink/',
        views.ReunionAPIListLink.as_view(),
        name='reunion-link'
    ),
    path(
        'api/persona-hobbie/detail/<pk>/',
        views.HobbyDetailAPIView.as_view(),
        name='detail-hobby'
    ),
    path(
        'api/persona-link/list/',
        views.PersonaAPIListLink.as_view(),
        name='persona-link'
    ),
    path(
        'api/persona/pagination/',
        views.PersonPaginationListAPIView.as_view(),
        name='persona-pagination'
    ),
    path(
        'api/persona/reuniones/',
        views.ReunionByJobs.as_view(),
    ),

]
