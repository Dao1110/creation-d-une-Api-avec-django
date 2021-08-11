from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.allBooks),
    path('book/<int:id>/',views.getBook),
    path('addbooks/',views.addBooks),
    path('updatebook/<int:id>/',views.updateBook),
    path('deletbook/<int:id>/',views.deleteBook)
]
