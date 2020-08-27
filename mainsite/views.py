from django.template.loader import get_template
from .models import Post
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime

# Create your views here.

#def homepage(request):
#    posts = Post.objects.all()
#    post_list = list()
#    for count, post in enumerate(posts):
#        post_list.append("No.{}:".format(str(count)) + str(post) + "<hr>")
#        post_list.append("<small>" + str(post.body) + "</small><br><br>")
#    return HttpResponse(post_list)

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')