from django.db import models


class User (models.Model):
    email = models.EmailField(max_length=100)
    fam = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    otc = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

class Level(models.Model):
    winter = models.CharField(max_length=100, blank=True, null=True)
    spring = models.CharField(max_length=100, blank=True, null=True)
    summer = models.CharField(max_length=100, blank=True, null=True)
    autumn = models.CharField(max_length=100, blank=True, null=True)

class Pereval(models.Model):
    SELECT_STATUS = (
        ("new", "новый"), ("pending", "в работе"),
        ("accepted", "принят"), ("rejected", "отклонён"),
    )
    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_title = models.CharField(max_length=100)
    content = models.CharField(max_length=100, blank=True, null=True)
    add_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=SELECT_STATUS, default="new")

class Images(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=1000)
    data = models.URLField()


"""
{
    "beauty_title": "beauty_title",
    "title": "title",
    "other_title": "other_title",
    "content": "",
    "add_time": "2021-09-22 13:18:13",
    "user": {
        "email": "email@email.ru",
        "fam": "fam",
        "name": "name",
        "otc": "otc",
        "phone": "890009990"
    },
    "coords": {
        "latitude":12567.00,
        "longitude": 112344.00,
        "height": 123455
    },
    "level": {
        "winter": "1А",
        "spring": "1А",
        "summer": "1А",
        "autumn": "1А"
    },
    "images": [{"data": "https://static.tildacdn.com/tild3937-3232-4637-b532-336534396163/1650925841_40-vsegda.jpeg", "title": "Седловина"}, {"data": "https://image.fonwall.ru/o/tg/landscape-lake-nature-svqv.jpeg?auto=compress&fit=resize&h=313&w=500&display=thumb&domain=img3.fonwall.ru", "title": "Подъём"}]
}
"""