from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import  reverse_lazy
from core.models import Movie

# Create your views here.

#https://www.agiliq.com/blog/2017/12/when-and-how-use-django-listview/



class MovieList(ListView):
    #as ´template_name´ is not defined template code should be in entities/movie_list.html
    #the following is the same that queryset = Movie.objects.all()
    model = Movie
    #as ´context_object_name´ is not defined, this will be "object_list" or "object"

class MovieDetail(DetailView):
    #as ´template_name´ is not defined template code should be in core/movie_detail.html
    #the following is the same that queryset = Movie.objects.all()
    model = Movie
    #as ´context_object_name´ is not defined, this will be "object_list" or "object"

class MovieCreateView(CreateView):
    template_name = 'core/movie_new.html'
    #the following is the same that queryset = Movie.objects.all()
    model = Movie
    #class of CreateView without the 'fields' attribute is prohibited.
    fields = ['title','plot','year','rating','runtime','website']


class MovieUpdateView(UpdateView):
        #the following is the same that queryset = Movie.objects.all()
        model = Movie
        template_name = 'core/movie_edit.html'
        fields = '__all__'

class MovieDeleteView(DeleteView):
        model = Movie
        template_name = 'core/movie_delete.html'
        #we use reverse_lazy to redirect the user to 'MovieList' inside 'core' app upon successful deletion.
        success_url = reverse_lazy('core:MovieList')
