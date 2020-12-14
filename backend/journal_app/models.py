from django.db import models
from django.conf import settings

# class User(models.Model):
#     first_name = models.CharField(max_length=255, blank=True, null=True)
#     last_name = models.CharField(max_length=255, blank=True, null=True)
#     username = models.CharField(max_length=255, blank=True, null=True)
#     birthdate = models.CharField(max_length=255, blank=True, null=True)
#     email = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.username

class Entry(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries') #use built-in user model
    entry_title = models.CharField(max_length=255, blank=True, null=True)
    written_body = models.TextField(blank=True, null=True)
    # voice_body = models.FileField(blank=True, null=True)
    voice_body_temp = models.CharField(max_length=255, blank=True, null=True)
    voice_text = models.TextField(blank=True, null=True)
    medium = models.CharField(max_length=7)
    location_tags = models.CharField(max_length=255, blank=True, null=True)
    text_tags = models.TextField(blank=True, null=True)
    # created_date = models.DateTimeField(auto_now_add=True)
    # edited_date = models.DateTimeField(auto_now=True)
    published_date = models.CharField(max_length=255, blank=True, null=True)
    privacy = models.CharField(max_length=255, blank=True, null=True)

    class Meta: 
        ordering = ['published_date']

    def __str__(self):
        return self.entry_title

# class Location(models.Model):
#     street_address = models.CharField(max_length=255, blank=True, null=True)
#     city = models.CharField(max_length=255, blank=True, null=True)
#     state = models.CharField(max_length=255, blank=True, null=True)
#     zip_code = models.CharField(max_length=255, blank=True, null=True)
#     country = models.CharField(max_length=255, blank=True, null=True)
#     location_title = models.CharField(max_length=255, blank=True, null=True)
#     entries = models.ManyToManyField(Entry) 
# # django ORM method to "find it if it exists, or create it if it doesn't"

#     def __str__(self):
#         return self.location_title