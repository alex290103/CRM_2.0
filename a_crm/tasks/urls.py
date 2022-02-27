from django.urls import path
from tasks.views import TaskView, CreateTask, UpdateTask, DeleteTask, OnCheck, EditTask

urlpatterns = [
    path("page/",TaskView.as_view(), name="task_table"),
    path("ajax/create/",CreateTask.as_view(),name="task_create"),
    path("ajax/update/",UpdateTask.as_view(),name="update_task"),
    path("ajax/delete/",DeleteTask.as_view(),name="delete_task"),
    path("oncheck/",OnCheck.as_view(),name="on_check"),
    path("ajax/edit/",EditTask.as_view(),name="edit_task"),
]
