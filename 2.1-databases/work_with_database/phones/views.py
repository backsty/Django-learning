from django.shortcuts import render, redirect

from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_catalog = request.GET.get('sort')
    if sort_catalog == 'name':
        phones_obj = Phone.objects.order_by('name')
    elif sort_catalog == 'min_price':
        phones_obj = Phone.objects.order_by('price')
    elif sort_catalog == 'max_price':
        phones_obj = Phone.objects.order_by('-price')
    else:
        phones_obj = Phone.objects.all()

    context = {}
    phone_lst = []
    for phone in phones_obj:
        phone_lst.append({
            'name': phone.name,
            'price': phone.price,
            'image': phone.image,
            'release_date': phone.release_date,
            'lte_exists': phone.lte_exists,
            'slug': phone.slug
        })
    context = {
        'phones': phone_lst
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.GET.get(slug=slug)
    phone_dict = {
        'name': phone.name,
        'price': phone.price,
        'image': phone.image,
        'release_date': phone.release_date,
        'lte_exists': phone.lte_exists,
        'slug': phone.slug
    }
    context = {
        'phones': phone_dict
    }
    return render(request, template, context)
