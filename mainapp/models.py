from django.db import models
from django.urls import reverse

from django.utils.text import slugify
from time import time


# Create your models here.

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    time_slug = str(int(time()))
    return f'{new_slug}-{time_slug}'


class Vacancy(models.Model):
    class Meta:
        ordering = ('title',)
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        index_together = (('id', 'slug'),)

    title = models.CharField(verbose_name='Название вакансии', max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, db_index=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('index:vacancy_detail', kwargs={'slug': self.slug})


class Documents(models.Model):
    class Meta:
        ordering = ('title',)
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        index_together = (('id', 'slug'),)

    title = models.CharField('Название документа', max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, db_index=True, blank=True, unique=True)
    description = models.CharField('Опиписание документа', max_length=250, blank=True, null=True)
    doc_file = models.FileField('Загруженный документ', upload_to='documents')

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


class SendContacts(models.Model):
    class Meta:
        ordering = ('pub_date', 'name')
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    name = models.CharField('Имя', max_length=60, db_index=True)
    email = models.EmailField()
    phone = models.CharField('Телефон', max_length=14)
    description = models.TextField('Сообщение', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}-{self.name}'