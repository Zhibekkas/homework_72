from django.db import models
status_options = [('moderated', 'Moderated'), ('new', 'New')]


class Citation(models.Model):
    text = models.TextField(null=False, blank=False, verbose_name='Text', max_length=2000)
    name = models.CharField(verbose_name='Name', max_length=200, null=False, blank=False)
    email_address = models.EmailField(verbose_name='Email', null=False, blank=False)
    rating = models.PositiveBigIntegerField(null=False, blank=False, default=0)
    status = models.CharField(max_length=50, null=False, verbose_name='Status', default='new', choices=status_options)
    added_date = models.DateTimeField(auto_now=True, verbose_name="Date of addition")

    def __str__(self):
        return f'{self.name} - {self.text}'

    class Meta:
        verbose_name = 'Citation'
        verbose_name_plural = 'Citations'

