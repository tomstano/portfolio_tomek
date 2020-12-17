from django.shortcuts import render
from django.utils import timezone
from .forms import PostForm
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Post


# Create your views here.
class PostListView(generic.ListView):
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(created_on__lte=timezone.now()).order_by('-created_on')


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_edit.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PostCreateView, self).dispatch(request, *args, **kwargs)


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_edit.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PostUpdateView, self).dispatch(request, *args, **kwargs)