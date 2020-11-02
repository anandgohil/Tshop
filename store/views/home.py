
from django.shortcuts import render, HttpResponse, redirect

from store.models import Tshirt, Occasion,Brand,Colour,IdealFor,NeckType,Sleeve

from django.core.paginator import Paginator

from urllib.parse import urlencode

def home(request):
    query = request.GET
    tshirts = []
    tshirts = Tshirt.objects.all()

    brand = query.get('brand')
    neck = query.get('neck')
    colour = query.get('colour')
    idealfor = query.get('idealfor')
    sleeve = query.get('sleeve')
    occasion = query.get('occasion')

    page = query.get('page')

    if page is None and page == "":
        page=1


    if brand != "" and brand is not None :
        tshirts = tshirts.filter(brand__slug=brand)

    if neck != "" and neck is not None:
        tshirts = tshirts.filter(neck_type__slug=neck)

    if colour != "" and colour is not None:
        tshirts = tshirts.filter(colour__slug = colour)

    if idealfor != "" and idealfor is not None:
        tshirts = tshirts.filter(ideal_for__slug=idealfor)

    if sleeve != "" and sleeve is not None:
        tshirts = tshirts.filter(sleeve__slug=sleeve)

    if occasion != "" and occasion is not None:
        tshirts = tshirts.filter(occasion__slug=occasion)

    occasion=Occasion.objects.all()
    brands = Brand.objects.all()
    colour = Colour.objects.all()
    idealfor = IdealFor.objects.all()
    necktype = NeckType.objects.all()
    sleeve = Sleeve.objects.all()

    # cart = request.session.get('cart')

    paginator = Paginator(tshirts,2)
    page_object = paginator.get_page(page)

    query = request.GET.copy()
    query['page'] = ''
    print(urlencode(query),"query")
    pageurl = urlencode(query)

    context = {
        'page_object': page_object,
        'occasion': occasion,
        'brands': brands,
        'colour': colour,
        'idealfor': idealfor,
        'necktype': necktype,
        'sleeve': sleeve,
        'pageurl': pageurl

    }
    return render(request, template_name='store/home.html', context=context)
