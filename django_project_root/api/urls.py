from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteListCreate.as_view(), name='note-list-create'),
    path('delete/<int:ok>', views.NoteDelete.as_view(), name='note-delete')
]
