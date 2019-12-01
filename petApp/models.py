from django.db import models

class Pet(models.Model):

    KIND_CHOICES = [
        ("C", "Cat"),
        ("D", "Dog")
    ]

    nickname = models.CharField(max_length=100)
    breed = models.CharField(max_length=50)
    description = models.TextField()
    admission_date = models.DateTimeField(auto_now=True)
    kind = models.CharField(max_length=1, choices=KIND_CHOICES, default="Dog")
    photo = models.ImageField(upload_to="images", blank=True)
    city = models.CharField(max_length=50)

    def __str__(self):
        return "%s (%s)" % (self.nickname, self.kind)
