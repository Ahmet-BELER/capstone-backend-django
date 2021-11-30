from django.db import models
from django.contrib.auth.models import User 
from django.utils.text import slugify 



# Create your models here.
class Category(models.Model): 
      
      name = models.CharField(max_length=200)
      description = models.TextField()  
      images = models.ImageField(upload_to="categories",blank=True, null=True)
      bg_image_url=models.URLField(max_length=200)

      def __str__(self): 
          return self.name      



class Course(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    images = models.ImageField(upload_to="courses",blank=True, null=True)
    bg_image_url=models.URLField(max_length=200)    
    def __str__(self): 
        return self.name
 
    
class Lesson(models.Model): 
 
    name = models.CharField(max_length=200)    
    description = models.TextField(max_length=200)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    images = models.ImageField(upload_to="lessons",blank=True, null=True)
    bg_image_url=models.URLField(max_length=200)
    
    def __str__(self): 
        return self.name 
 
        
class Post(models.Model): 
     
    name=models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    slug= models.SlugField(blank=True,unique=True)
    topics = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    images = models.ImageField(upload_to="topics",blank=True, null=True)
    bg_image_url=models.URLField(max_length=200)
    
    created_date= models.DateField(auto_now_add=True) 
    last_update_date= models.DateField(auto_now=True)
    
    STATUS_CHOICES=(
        (1,"Publish"),
        (0,"Draft")
    )
    status= models.IntegerField(choices=STATUS_CHOICES)
    
     
     
    def __str__(self): 
        return self.name 
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)
        
        
        
class Like(models.Model): 
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    post= models.ForeignKey(Lesson,on_delete=models.CASCADE)
    text   = models.TextField(max_length=200)
    
       
    def __str__(self):
        return self.user.username  +" "+    self.post.name  
    
    class Meta : 
        constraints=[
            models.UniqueConstraint(fields=['user','post'], name="unique_like")
        ]
    
    
class Comment(models.Model):
   user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
   post= models.ForeignKey(Lesson,on_delete=models.CASCADE)
   timestamp= models.DateTimeField(auto_now_add=True)
   

class PostView(models.Model): 
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)   
    post= models.ForeignKey(Lesson,on_delete=models.CASCADE)
    timestamp= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
    
    
    