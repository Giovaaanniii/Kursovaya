from django.db import models
from django.utils.html import mark_safe
from simple_history.models import HistoricalRecords



class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='images/', null=True, blank=True,verbose_name='Фотография')
    task = models.TextField(blank=True, verbose_name='Описание')
    short_task = models.TextField(max_length=255, verbose_name="Краткое описание")
    cena = models.CharField(max_length=255, verbose_name='Cтоимость')
    time_create = models.DateTimeField(verbose_name="Время создания",auto_now_add=True)
    time_update = models.DateTimeField(verbose_name="Время изменения",auto_now=True)
    
    
    def image_preview (self):
        if self.image:
            return mark_safe('<img src="%s" width="300" height="300" />' % self.image.url)
        else:
            return 'Изображения нет'
    image_preview.short_description = 'Превью фотографиии'
    image_preview.allow_tags = True
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Главная'
        ordering = ['-time_create']
        


#------------------------------------------------

class Events(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='images/',verbose_name='Фотография')
    task = models.TextField(blank=True, verbose_name='Описание')
    short_task = models.TextField(max_length=255, verbose_name="Краткое описание")
    cena = models.CharField(max_length=255, verbose_name='Cтоимость')
    time_create = models.DateTimeField(verbose_name="Время создания",auto_now_add=True)
    time_update = models.DateTimeField(verbose_name="Время изменения",auto_now=True)
    
    def image_preview (self):
        if self.image:
            return mark_safe('<img src="%s" width="300" height="300" />' % self.image.url)
        else:
            return 'Изображения нет'
    image_preview.short_description = 'Превью фотографиии'
    image_preview.allow_tags = True
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'

#------------------------------------------------

class Excursions(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='images/',verbose_name='Фотография')
    task = models.TextField(blank=True, verbose_name='Описание')
    short_task = models.TextField(max_length=255, verbose_name="Краткое описание")
    cena = models.CharField(max_length=255, verbose_name='Cтоимость')
    time_create = models.DateTimeField(verbose_name="Время создания",auto_now_add=True)
    time_update = models.DateTimeField(verbose_name="Время изменения",auto_now=True)
    
    def image_preview (self):
        if self.image:
            return mark_safe('<img src="%s" width="300" height="300" />' % self.image.url)
        else:
            return 'Изображения нет'
    image_preview.short_description = 'Превью фотографиии'
    image_preview.allow_tags = True

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Экскурсии'
        verbose_name_plural = 'Экскурсии'

#------------------------------------------------

class Master(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='images/',verbose_name='Фотография')
    task = models.TextField(blank=True, verbose_name='Описание')
    short_task = models.TextField(max_length=255, verbose_name="Краткое описание")
    cena = models.CharField(max_length=255, verbose_name='Cтоимость')
    time_create = models.DateTimeField(verbose_name="Время создания",auto_now_add=True)
    time_update = models.DateTimeField(verbose_name="Время изменения",auto_now=True)
    
    def image_preview (self):
        if self.image:
            return mark_safe('<img src="%s" width="300" height="300" />' % self.image.url)
        else:
            return 'Изображения нет'
    image_preview.short_description = 'Превью фотографиии'
    image_preview.allow_tags = True

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Мастер-классы'
        verbose_name_plural = 'Мастер-классы'

#------------------------------------------------

class Contacts(models.Model):
    title = models.CharField(max_length=100)
    short_task = models.CharField(max_length=200)
    task = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    
    history = HistoricalRecords()

    def __str__(self):
        return self.title

#------------------------------------------------

class Graduation(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='images/', null=True, blank=True,verbose_name='Фотография')
    task = models.TextField(blank=True, verbose_name='Описание')
    short_task = models.TextField(max_length=255, verbose_name="Краткое описание")
    cena = models.CharField(max_length=255, verbose_name='Cтоимость')
    time_create = models.DateTimeField(verbose_name="Время создания",auto_now_add=True)
    time_update = models.DateTimeField(verbose_name="Время изменения",auto_now=True)
    
    
    def image_preview (self):
        if self.image:
            return mark_safe('<img src="%s" width="300" height="300" />' % self.image.url)
        else:
            return 'Изображения нет'
    image_preview.short_description = 'Превью фотографиии'
    image_preview.allow_tags = True
    

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Выпускные'
        verbose_name_plural = 'Выпускные'
    

