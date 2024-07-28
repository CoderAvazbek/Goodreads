from django.urls import path
from .views import landing_page, BookView, BookDetail

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path("all/", BookView.as_view(), name="book-all"),
    path("detail/<int:pk>/", BookDetail.as_view(), name="book-detail")
]