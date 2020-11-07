from djongo import models

# Create your models here.
# isbn,title,author_last_name,author_first_name,page_count,description
class Book(models.Model):
    isbn = models.CharField(max_length=17, blank=False, default='')
    title = models.CharField(max_length=100, blank=False, default='')
    author_last_name = models.CharField(max_length=50, blank=False, default='')
    author_first_name = models.CharField(max_length=50, blank=False, default='')
    page_count = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=500,blank=False, default='')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):     
        return f"/api/books/{self.id}/"
