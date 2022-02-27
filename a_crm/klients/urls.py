from django.urls import path
from klients.views import TableKlients, AddKlient, UpdateKlients, DeleteKlients, EditKlients

urlpatterns = [
    path("page/",TableKlients.as_view(), name="klients_table"),
    path("ajax/create/",AddKlient.as_view(),name="add_klient"),
    path("ajax/update/",UpdateKlients.as_view(),name="update_klient"),
    path("ajax/delete/",DeleteKlients.as_view(),name="delete_klient"),
    path("ajax/edit/",EditKlients.as_view(),name="edit_klient"),
]
