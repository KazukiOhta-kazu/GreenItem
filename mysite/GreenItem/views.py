from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Wallet, Item

@login_required
def index(request):
    money = Wallet.objects.get(user_id=request.user.id)
    wish_list = Item.objects.filter(user_id=request.user.id, pur_date__isnull=True).order_by('reg_date')
    my_list = Item.objects.filter(user_id=request.user.id, pur_date__isnull=False).order_by('reg_date')
    context = {
        'money': money,
        'wish_list': wish_list,
        'my_list': my_list
    }
    return render(request, 'greenitem/index.html', context)
