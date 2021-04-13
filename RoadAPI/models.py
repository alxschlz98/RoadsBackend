from django.db import models


class Road(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Point(models.Model):
    road = models.ForeignKey(Road, on_delete=models.CASCADE)
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return "%s: %s, %s on road %s" % (str(self.order), str(self.x_coord), str(self.y_coord), self.road)

    class Meta:
        unique_together = ['road', 'order']
