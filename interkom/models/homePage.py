from django.db import models
from interkom.utils import AbstractUUID, AbstractTimeTracker


class Home(AbstractUUID, AbstractTimeTracker):
    title = models.CharField(max_length=500,
                             blank=True,
                             null=True,
                             verbose_name='Главный заголовок')
    welcome = models.CharField(max_length=1000,
                               blank=True,
                               null=True,
                               verbose_name='Приветствие')
    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главные'

    def __str__(self):
        return self.title


class Galvanize(AbstractUUID, AbstractTimeTracker):
    title = models.CharField(max_length=500,
                             blank=True,
                             null=True,
                             verbose_name='Цинкование: Название')
    description_galvanize = models.CharField(max_length=500,
                             blank=True,
                             null=True,
                             verbose_name='Краткое описание')
    zink_image_1 = models.ImageField(verbose_name='Фото1')
    description_image1 = models.CharField(max_length=500,
                             blank=True,
                             null=True,
                             verbose_name='Краткое описание фото1')
    zink_image_2 = models.ImageField(verbose_name='Фото2')
    description_image2 = models.CharField(max_length=500,
                                          blank=True,
                                          null=True,
                                          verbose_name='Краткое описание фото2')
    zink_image_3 = models.ImageField(verbose_name='Фото3')
    description_image3 = models.CharField(max_length=500,
                                          blank=True,
                                          null=True,
                                          verbose_name='Краткое описание фото3')
    class Meta:
        verbose_name = 'Цинкование'
        verbose_name_plural = 'Цинкование'

    def __str__(self):
        return self.title


class Cuprum(AbstractUUID, AbstractTimeTracker):
    title = models.CharField(max_length=500,
                             blank=True,
                             null=True,
                             verbose_name='Меднение: Название')

    description_cuprum = models.CharField(max_length=500,
                             blank=True,
                             null=True,
                             verbose_name='Краткое описание')
    cuprum_set = models.CharField(max_length=500,
                                  blank=True,
                                  null=True,
                                  verbose_name='Комплекты - Медь: Название')
    cuprum_image_1 = models.ImageField(verbose_name='Фото1')
    description_image1 = models.CharField(max_length=500,
                             blank=True,
                             null=True,
                             verbose_name='Краткое описание фото1')
    cuprum_image_2 = models.ImageField(verbose_name='Фото2')
    description_image2 = models.CharField(max_length=500,
                                          blank=True,
                                          null=True,
                                          verbose_name='Краткое описание фото2')
    cuprum_image_3 = models.ImageField(verbose_name='Фото3')
    description_image3 = models.CharField(max_length=500,
                                          blank=True,
                                          null=True,
                                          verbose_name='Краткое описание фото3')

    class Meta:
        verbose_name = 'Заземление'
        verbose_name_plural = 'Заземления'

    def __str__(self):
        return self.title


class ZinkSetModel(AbstractUUID, AbstractTimeTracker):
    title = models.CharField(max_length=500,
                             blank=True,
                             null=True,
                             verbose_name='Название')
    zinks_image_1 = models.ImageField(verbose_name='Фото1')
    description_image1 = models.CharField(max_length=500,
                                          blank=True,
                                          null=True,
                                          verbose_name='Краткое описание фото1')
    zinks_image_2 = models.ImageField(verbose_name='Фото2')
    description_image2 = models.CharField(max_length=500,
                                          blank=True,
                                          null=True,
                                          verbose_name='Краткое описание фото2')
    zinks_image_3 = models.ImageField(verbose_name='Фото3')
    description_image3 = models.CharField(max_length=500,
                                          blank=True,
                                          null=True,
                                          verbose_name='Краткое описание фото3')

    class Meta:
        verbose_name = 'Цинковый комплект'
        verbose_name_plural = 'Цинковые комплекты'

    def __str__(self):
        return self.title
