from django.shortcuts import redirect, render
from streetview.models import StreetViewPost

# Create your views here.
def index(request):
    streetview_list = StreetViewPost.objects.all()
    return render(request, 'index.html', context={'streetview_list': streetview_list})


def show(request, id):
    print(id)
    streetview = StreetViewPost.objects.get(id=id)
    print(streetview)
    return render(request, 'show.html', context={'streetview': streetview})


def create(request):
    return render(request, 'create.html')


def store(request):
    title = request.POST.get('title')
    streetXY = request.POST.get('streetXY')

    streetview_post = StreetViewPost()
    streetview_post.title = title
    streetview_post.streetXY = streetXY
    streetview_post.save()

    return redirect('/')
