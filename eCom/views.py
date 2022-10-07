from django.shortcuts import render

from shop.forms import SearchForm


def page_not_found(request, exception):
    print(exception)
    return render(request, '404.html')

def FixPage(request):
    search_form = SearchForm()
    return render(request, 'fix_page.html',{
        'search_form': search_form
    })