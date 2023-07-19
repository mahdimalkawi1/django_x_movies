from django.urls import path
from .views import MoviesListView,MoviesDetailView,MoviesCreateView,MoviesUpdateView , MoviesDeleteView
urlpatterns = [
    path('', MoviesListView.as_view(),name = 'movies_list'),
    path('<int:pk>/', MoviesDetailView.as_view(),name = 'movies_detail'),
    path('create/', MoviesCreateView.as_view(),name = 'movies_create'),
    path('update/<int:pk>/',MoviesUpdateView.as_view(),name = 'movies_update'),
    path('delete/<int:pk>/', MoviesDeleteView.as_view(),name = 'movies_delete')

]