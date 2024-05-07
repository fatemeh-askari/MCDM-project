from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    answer_admin = models.TextField(null=True, blank=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
        verbose_name = "Contact us"
        verbose_name_plural = "Contact us"

    def __str__(self):
        return f'{self.name} by {self.email} on {self.subject}'
