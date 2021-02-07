from django.shortcuts import render, redirect
from .models import Category, Photo
# Create your views here.


def gallery(request):

    category = request.GET.get('category')

    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    context = {'categories': categories, 'photos': photos}

    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})


def addPhoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['cat'] != 'none':
            category = Category.objects.get(id=data['cat'])
        elif data['new_cat'] != '':
            category, created = Category.objects.get_or_create(
                name=data['new_cat'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category, desc=data['desc'], image=image)

        return redirect('/')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)
