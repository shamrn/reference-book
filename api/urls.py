from django.urls import path
from . import views

urlpatterns = [
    path('book-list/',views.ReferenceBookList.as_view()),
    path('item/',views.ItemDetailView.as_view()),
]
