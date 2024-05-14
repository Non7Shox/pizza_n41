from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


class ProductModel(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products')
    description = models.TextField(default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
