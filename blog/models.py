from django.db import models

# Create your models here.
# title
# pub_date
# body
# image

# Add the blog app to the settings
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Create a migration; run below command
# python manage.py makemigrations

# Migrate; run below command
# python manage.py migrate

# Add to admin
# go to admin.py under jobs and copy two lines and paste to admin.py in blog folder
