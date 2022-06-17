from django.db import models


class AddOn(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Add Ons'
        ordering = ['-id']

    def __str__(self):
        return self.name


class EventType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    event_type = models.ForeignKey('EventType', on_delete=models.SET_NULL, null=True, blank=False)
    venue = models.ForeignKey('Venue', on_delete=models.SET_NULL, null=True, blank=False)
    add_ons = models.ManyToManyField(AddOn)
    no_of_persons = models.PositiveIntegerField(default=0)
    no_of_chairs = models.PositiveIntegerField(default=100)

    event_charge = models.FloatField(default=1000)
    venue_charge = models.FloatField(default=500)
    tax_charge = models.FloatField(default=100)
    total_charge = models.FloatField(default=0)

    transaction_id = models.CharField(
        max_length=1000, null=False, blank=False,
        help_text="Enter transaction id here, transaction id will be provided by your service provider "
                  "i.e EasyPaisa provide you through sms over a successful transaction", unique=True
    )
    single_split = models.BooleanField(default=False)
    double_split = models.BooleanField(default=False)
    triple_split = models.BooleanField(default=False)
    red_carpet = models.BooleanField(default=False)
    music = models.BooleanField(default=False)

    is_paid = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # _total_charge = self.event_charge + self.venue_charge + self.tax_charge
        # if self.add_ons:
        #     for add_on in self.add_ons.all():
        #         _total_charge += add_on.price
        # self.total_charge = _total_charge
        super(Event, self).save(*args, **kwargs)


class Video(models.Model):
    caption = models.CharField(max_length = 100)
    description = models.TextField()
    video = models.FileField(upload_to = 'videos/', null=True)

    def __str__(self):
        return f'{self.caption}'