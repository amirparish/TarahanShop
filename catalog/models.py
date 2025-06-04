from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان دسته‌بندی')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام محصول')
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='دسته‌بندی')
    is_featured = models.BooleanField(default=False, verbose_name='پیشنهاد ویژه')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title