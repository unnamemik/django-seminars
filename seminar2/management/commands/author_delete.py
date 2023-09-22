from django.core.management.base import BaseCommand

from seminar2.models import Author


class Command(BaseCommand):
    help = "Delete author by id"

    def add_arguments(self, parser):
        parser.add_argument('author_id', type=str, help='Author name')

    def handle(self, *args, **kwargs):
        author_id = kwargs.get('author_id')
        author = Author.objects.filter(id=author_id).first()
        if author is not None:
            author.delete()
        self.stdout.write(f'{author}')