from django.urls import path
from statistika.views import view_func
urlpatterns = [
    path("",view_func, name="statistika_table")
]