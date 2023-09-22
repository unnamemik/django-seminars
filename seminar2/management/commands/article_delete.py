from django.core.management.base import BaseCommand
from seminar2.models import Article


class Command(BaseCommand):
    help = "Delete article by id"

    def add_arguments(self, parser):
        parser.add_argument('article_id', type=str, help='Article id')

    def handle(self, *args, **kwargs):
        article_id = kwargs.get('article_id')
        article = Article.objects.filter(id=article_id).first()
        if article is not None:
            article.delete()
        self.stdout.write(f'{article}')
