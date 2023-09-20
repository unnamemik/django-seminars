import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'{request} request received!')
    return HttpResponse('Index page')
