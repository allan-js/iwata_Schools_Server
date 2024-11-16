from django.db import models

class StudentWork(models.Model):
    name = models.CharField(max_length=255, verbose_name='File Name')
    student = models.CharField(max_length=255)
    file = models.FileField(upload_to='Images/%Y/%M/')
    is_archived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    

    class Meta:
        verbose_name = "Student's Work"
        verbose_name_plural = "Student's Works"

