from collections.abc import Iterable
from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class Snippet(models.Model):
    owner = models.ForeignKey("auth.User", related_name = "snippets", on_delete = models.CASCADE)
    title = models.CharField(max_length=100, default = "no title")
    code = models.TextField()
    linenos = models.BooleanField(default=True)
    language = models.CharField(max_length=50, choices = LANGUAGE_CHOICES, default="python" )
    style = models.CharField(choices = STYLE_CHOICES, max_length=50, default="friendly")
    created = models.DateTimeField(auto_now_add = True)
    highlighted = models.TextField()

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.title} | {self.language}"


    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
