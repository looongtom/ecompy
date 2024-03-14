from django.db import models

# Create your models here.

       
class Category(models.Model):
    name = models.CharField(verbose_name='Category Name', max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'category'
    
class Book(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    author = models.CharField(verbose_name='Author', max_length=255)
    price = models.PositiveIntegerField(verbose_name='Price')
    description = models.CharField(verbose_name='Description', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default.jpg',upload_to='books/')
    categories = models.ManyToManyField(Category, related_name='books', verbose_name='Categories')

    class Meta:
        __tablename__ = 'Book'
