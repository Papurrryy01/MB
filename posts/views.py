from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# Create your views here.
class PostListView(ListView): #get method
    # PostListView is going to retrieve all of the objects from the Post table in the DB
   
    # template_name attribute is going to render an specific html file
    template_name = 'posts/list.html'
    # model is going to be from which table we want to retrieve the data
    model = Post
    # context_object_name allow us to modifythe name, on how we call it the
    context_object_name = 'posts'

class PostDetailView(DetailView): #get method
    # PostDetailView is going to retrieve a single object from the Post table in the DB
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'single_post'

class PostCreateView(CreateView): #get and post method
    # PostCreateView is going to create a new object in the Post table in the DB
    template_name = 'posts/new.html'
    model = Post
    #fields attribute allow us to control which elements to display on the form to. create a new object
    #the name of the fields have to match with the attributes of the model
    fields = ['title', 'subtitle', 'body']