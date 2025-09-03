from django.db import models

 # Create your models here.

class Nation(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=5) 

    def __str__(self):
        return f"{self.flag} {self.name}"


class League(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.flag} {self.name}"


class Club(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=5)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="clubs")

    def __str__(self):
        return f"{self.flag} {self.name} ({self.league.name})"


class Position(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code} - {self.name}"


class CardRarity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    background_image = models.ImageField(upload_to="card_backgrounds/")

    def __str__(self):
        return self.name


class PlayerCard(models.Model):
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    nation = models.ForeignKey(Nation, on_delete=models.SET_NULL, null=True)
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    rarity = models.ForeignKey(CardRarity, on_delete=models.SET_NULL, null=True)
    player_image = models.ImageField(upload_to="player_images/")

    # Player states
    pace = models.PositiveIntegerField()
    shooting = models.PositiveIntegerField()
    passing = models.PositiveIntegerField()
    dribbling = models.PositiveIntegerField()
    defending = models.PositiveIntegerField()
    physicality = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.rating})"
