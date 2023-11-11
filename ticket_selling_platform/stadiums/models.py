from django.db import models


class Stadium(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    rows = models.PositiveIntegerField()
    columns = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        # Ensure capacity is a multiple of rows and columns
        if self.capacity % (self.rows * self.columns) != 0:
            raise ValueError("Capacity must be a multiple of rows and columns.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
