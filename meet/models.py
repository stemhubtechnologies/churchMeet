
from django.db import models
#from django.template.defaultfilters import slugify
#from django.contrib.auth.models import User


# Create your models here.




class Post(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    title = models.CharField(max_length=200)
    message = models.TextField()
    image = models.ImageField(upload_to='images/') 
    created_on = models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.name

'''
    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_detail', (),
                {
                   'slug': self.slug,
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title


class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

 





class Post(models.Model):
    title= models.CharField(max_length=200, unique=True)
    content= models.TextField()


def __str__(self):
        return self.title
'''