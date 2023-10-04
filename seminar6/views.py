import logging

from django.db.models import Sum
from django.shortcuts import render

from seminar6.models import Product

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='logger.log', filemode='a', format='%(levelname)s %(message)s')


def seminar6(request):
    logger.info(f'{request} request received')

    return render(request, 'seminar6.html')


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total['quantity__sum']}
    return render(request, 'seminar6.html', context)


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total}
    return render(request, 'seminar6.html', context)


def total_in_template(request):
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product}
    return render(request, 'seminar6.html', context)
