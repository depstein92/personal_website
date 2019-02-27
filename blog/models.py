from django.db import models

class Blog(models.Model):
      title = models.CharField(max_length=255)
      date = models.DateField()
      body = models.TextField()
      image = models.ImageField(upload_to="images/")

      def summary(self):
          return  self.body[:100]

      def pub_date_pretty(self):
          return self.pub_date.strftime('%b %e %Y')

      def __str__(self): # for django admin
           return self.title
