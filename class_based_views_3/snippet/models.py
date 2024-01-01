from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=100, default = "no title")
    code = models.TextField()
    linenos = models.BooleanField(default=True)
    language = models.CharField(max_length=50, choices = LANGUAGE_CHOICES, default="python" )
    style = models.CharField(choices = STYLE_CHOICES, max_length=50, default="friendly")
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.title} | {self.language}"
