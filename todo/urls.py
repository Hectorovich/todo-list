from django.urls import path

from todo.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, task_complete, task_undo, TagList, \
    TagCreateView, TagUpdateView, TagDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("complete/<int:pk>/", task_complete, name="task-complete"),
    path("undo/<int:pk>/", task_undo, name="task-undo"),
    path("tags/", TagList.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
