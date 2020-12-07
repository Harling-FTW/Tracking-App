from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# Create your models here.
class Clients(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    userId = models.IntegerField(null = False, blank = False, unique = True)
    username = models.CharField(max_length = 20, null = False, blank = False)
    email_address = models.CharField(max_length = 36, null = False, blank = False)
    password = models.CharField(max_length = 16, null = False, blank = False)
    isCustomer = models.BooleanField(default=True)
     
class Orders(models.Model):
    userId = models.IntegerField(null = False, blank = False)
    orderId = models.IntegerField(null = False, blank = False, unique = True)
    description = models.TextField(max_length = 123,)
    
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Orders, self).save(*args, **kwargs)
