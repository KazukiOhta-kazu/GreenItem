from django.shortcuts import render
from .models import Item


def index(request):
    wish_list = Item.objects.filter(pur_date__isnull=True).order_by('reg_date')
    my_list = Item.objects.filter(pur_date__isnull=False).order_by('reg_date')
    context = {
        'wish_list': wish_list,
        'my_list': my_list
    }
    return render(request, 'greenitem/index.html', context)
