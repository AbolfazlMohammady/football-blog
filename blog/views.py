import json
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog

from django.views.generic import ListView
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = context['page_obj']  
        return context



class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'


def search(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Blog.objects.filter(title__icontains=query)
    return render(request, 'blog/blog_search.html', {'results': results, 'query': query})




def blog_chart_view(request):
    blogs = Blog.objects.all().order_by('created_at')

    labels = [blog.title for blog in blogs]
    data = [blog.created_at.year for blog in blogs]

    
    chart_data = {
        'labels': labels,
        'data': data,
    }

   
    return render(request, 'blog/chart.html', {'chart_data': json.dumps(chart_data)})
