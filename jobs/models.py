from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to="")
    summary = models.CharField(max_length=200)
    url = models.CharField(max_length=300)

class Blog(models.Model):
      title = models.CharField(max_length=255)
      date = models.DateField()
      body = models.TextField(max_length=120)
      image = models.ImageField(upload_to="images/")
      url = models.CharField(max_length=300)


      def summary(self):
          return  self.body[:100]

      def pub_date_pretty(self):
          return self.pub_date.strftime('%b %e %Y')

      def __str__(self): # for django admin
           return self.title


class Education(models.Model):
    school = models.CharField(max_length=75)
    degree = models.CharField(max_length=150)
    years_attended = models.CharField(max_length=30)
    description = models.TextField()

class Experience(models.Model):
    company_name = models.CharField(max_length=75)
    position = models.CharField(max_length=30)
    date = models.CharField(max_length=50)
    description = models.TextField()
