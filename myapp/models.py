from django.db import models

# Create your models here.
class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    doc = models.FileField(upload_to='doc', default="")

    def __str__(self):
        return self.name

class Student(models.Model):
    std_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.IntegerField(default="")
    pswd = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

# Create your models here.
class Python(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    video = models.FileField(upload_to='videos/python', default="")

    def __str__(self):
        return self.desc
        
class C(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    video = models.FileField(upload_to='videos/C', default="")

    def __str__(self):
        return self.desc
        
class Html(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    video = models.FileField(upload_to='videos/Html', default="")

    def __str__(self):
        return self.desc

class Css(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    video = models.FileField(upload_to='videos/css', default="")

    def __str__(self):
        return self.desc

class Java(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    video = models.FileField(upload_to='videos/java', default="")

    def __str__(self):
        return self.desc

class Javascript(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    video = models.FileField(upload_to='videos/javascript', default="")

    def __str__(self):
        return self.desc

class Django(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    video = models.FileField(upload_to='videos/django', default="")

    def __str__(self):
        return self.desc
