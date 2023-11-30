from django.db import models

# Each Class is a table in our db

# Profile -> Links som associeras med profilerna.

# Profile class
class Profile(models.Model):
    # BG_Choices is a variable that holds values for background-colors. The left one is what's saved to the DB and the right one is what's gonna show as a choice in admin etc.
    BG_CHOICES = (
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('gray', 'Gray'),
        ('pink', 'Pink'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('purple', 'Purple'),
    )
    
    # name, slug, bg_color
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)
    
    # Overriding dunder-method
    def __str__(self):
        return self.name
    
# Link model
class Link(models.Model):
    # text, url, profile that it's connected to
    text = models.CharField(max_length=100)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='links')


# Many to many - I detta fall betyder detta att många länkar kommer va associerade med många profiler.
# one to one - I detta fall så betyder det att en profil kommer vara länkad till en länk
# many to one - I detta fall så betyder det att en många länkar kommer att vara associerade med en profil. DETTA VILL DU HA FÖR EN LINKTREE KOPIA
