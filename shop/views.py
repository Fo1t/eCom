from django.core.files.base import ContentFile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from django.views import generic, View
from django.views.decorators.http import require_POST
from cart.forms import CartAddProductForm
from .models import Product, Category, Image
from .forms import LoginForm, EditForm, SearchForm, SideBarForm
from django.contrib.auth import authenticate, login


def MainPage(request):
    paginate = 6

    try:
        if request.session['cat_id'] != request.GET.get('cat_id'):
            request.session['cat_id'] = request.GET.get('cat_id')
    except:
        request.session['cat_id'] = request.GET.get('cat_id')

    try:
        if request.session['search'] != request.GET.get('search'):
            request.session['search'] = request.GET.get('search')
    except:
        request.session['search'] = request.GET.get('search')

    form = SideBarForm(
        initial={'minamount': Product.objects.values('discounted_price').order_by('discounted_price').first(),
                 'maxamount': Product.objects.values('discounted_price').order_by('discounted_price').last(),
                 })
    search_form = SearchForm()
    min_price = Product.objects.values('discounted_price').order_by('discounted_price').first()['discounted_price']
    max_price = Product.objects.values('price').order_by('price').last()['price']

    if request.GET.get('minamount') is not None or request.GET.get('maxamount') is not None:
        min_price = float(request.GET.get('minamount')[:-2])
        max_price = float(request.GET.get('maxamount')[:-2])

    if request.session['cat_id'] is None:
        prod_list = Product.objects.filter(price__lte=max_price + 1).exclude(discounted_price__lte=min_price - 1)
    else:
        prod_list = Product.objects.filter(category=request.session['cat_id'], price__lte=max_price + 1).exclude(
            discounted_price__lte=min_price - 1)

    if request.session['search'] is not None:
        prod_list = Product.objects.filter(title__contains=request.session['search'])

    if request.POST.get('input'):
        prod_list = Product.objects.filter(title__contains=request.POST.get('input').upper())

    paginator = Paginator(prod_list, paginate)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'shop/product_list.html', {
        'side_form': form,
        'search_form': search_form,
        'page_title': 'Органический магазин',
        'sale_list': Product.objects.all().exclude(sale=0),
        'category_list': Category.objects.all(),
        'price_range': [Product.objects.values('discounted_price').order_by('discounted_price').first(),
                        Product.objects.values('price').order_by('price').last()],
        'page_obj': page_obj,
    }
                  )


class ProductListView(generic.ListView):
    model = Product
    template_name = "shop/product_list.html"
    paginate_by = 6
    category = None
    search = ''
    form = None

    def get_queryset(self):
        print("in 0")
        # print()
        try:
            category = Category.objects.get(id=self.kwargs['cat_id'])
            print("in 1")
            print(category)
            return Product.objects.all().filter(category=category)
        except KeyError:
            print("in 2")
            return Product.objects.all()


    def post(self, request):
        self.search = self.form.input
        print(self.search)
        return HttpResponse(200)

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['sale_list'] = Product.objects.all().exclude(sale=0)
        context['category_list'] = Category.objects.all()
        context['page_title'] = "Органический магазин"
        context['price_range'] = [Product.objects.values('price').order_by('price').first(),
                                  Product.objects.values('price').order_by('price').last()]
        # print(context)
        return context


class EIndexView(View):

    def get(self, request):
        context = {}
        all_product = Product.objects.all().order_by('created_date')
        current_page = Paginator(all_product, 6)
        page = request.GET.get('page')
        try:
            context['product_lst'] = current_page.page(page)
        except PageNotAnInteger:
            context['product_lst'] = current_page.page(1)
        except EmptyPage:
            context['product_lst'] = current_page.page(current_page.num_pages)
        return render('shop/grid_content.html', context)


def index(request):
    sale_list = Product.objects.all().exclude(sale=0)
    prod_list = Product.objects.all()
    return render(
        request,
        '404.html',
        context={'sale_list': sale_list,
                 'prod_list': prod_list,
                 }
    )


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['sale_list'] = Product.objects.all().exclude(sale=0)
        context['category_list'] = Category.objects.all()
        context['page_title'] = "О Продукте"
        context['price_range'] = [Product.objects.values('price').order_by('price').first(),
                                  Product.objects.values('price').order_by('price').last()]
        context['cart_product_form'] = CartAddProductForm()
        return context

    def product_detail_view(request, pk):
        try:
            product_id = Product.objects.get(pk=pk)
            print(Product.objects.get(pk=pk))
        except Product.DoesNotExist:
            raise Http404("Product does not exist")
        return render(request, 'product_detail.html', context={'product': product_id})


def ProductEditView(request, pk):
    product = Product.objects.get(pk=pk)
    if not request.user.is_anonymous and (request.user.is_staff or request.user.userprofile.editor):
        if request.method == 'POST':
            form = EditForm(request.POST, request.FILES)
            if form.is_valid():
                print(request.FILES['file'])
                for f in request.FILES.getlist('file'):
                    # data = f.read()
                    # print(data)
                    print(product)
                    image = Image(product=product, file=f)
                    image.save()
                return HttpResponseRedirect('/shop/product/edit/' + pk + '/')
            return HttpResponse(504)
        else:
            print(1)
            data = {'price': product.price,
                    'description': product.description,
                    'discounted_price': product.discounted_price,
                    'sale': product.sale,
                    'title': product.title,
                    'weight': product.weight
                    }
            form = EditForm(initial=data)
            return render(request, 'shop/product_edit.html', context={'form': form,
                                                                      'page_title': 'Редактор',
                                                                      'product': product})
    else:
        return redirect('/shop/404/')


def page404(request):
    return render(request, '404.html')


def ProductRemove(request, pk):
    print('in ProductRemove')


def ProductSave(request, pk):
    print('in ProductSave')


def image_remove(request, pk, prod_id):
    image = Image.objects.get(pk=pk)
    image.delete()
    return redirect('shop:product-edit', prod_id)

# return render(
#         request,
#         'index.html',
#         context={'num_books': num_books, 'num_instances': num_instances,
#                  'num_instances_available': num_instances_available, 'num_authors': num_authors,
#                  'num_visits': num_visits},  # num_visits appended
#         )
