from django.shortcuts import render, redirect
from cart.cart import Cart
# Create your views here.
from orders.forms import OrderCreateForm
from orders.models import OrderItem
from .tasks import order_created
from userprofile.models import UserProfile

def order_create(request):
    cart = Cart(request)
    data = {}
    if request.user.is_authenticated:
        profile = UserProfile.objects.filter(user=request.user).first()
        data = {'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'address': profile.address,
                'postal_code': profile.post_code,
                'city': profile.city,
                'phone': profile.phone
                }
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            if request.user.is_authenticated:
                order.client = request.user
                order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            print(request.user)
            order_created.delay(order.id)
            return redirect('/shop/')
            #return render(request, 'new_orders/create.html', {'order': order, 'page_title': 'Заказ'})
    else:
        form = OrderCreateForm(initial=data)
    return render(request, 'new_orders/create.html', {'cart': cart, 'form': form, 'page_title': 'Заказ'})