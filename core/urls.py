from django.urls import path

from .views import (MovieList,
                    MovieDetail,
                    MovieCreateView,
                    MovieUpdateView,
                    MovieDeleteView,
                    )

app_name = 'core'
#CBVs are not callable, so the base View class has a static as_view()
urlpatterns = [
    path('movie/<int:pk>/delete/',MovieDeleteView.as_view(),name='movie_delete'),
    path('movie/<int:pk>/edit/',MovieUpdateView.as_view(),name='movie_edit'),
    path('movies',MovieList.as_view(),name='MovieList'),
    path('movie/<int:pk>/',MovieDetail.as_view(),name='MovieDetail'),
    path('movie/new',MovieCreateView.as_view(),name='movie_new')

]
