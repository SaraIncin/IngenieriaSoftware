from django.db import models

# Create your models here.

def artist_directory_path(instance, filename):
    """Get song directory path to save."""
    return f"media/artists/images/{instance.id}_{instance.name}_{filename}"
    
class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to=artist_directory_path)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
        
def song_directory_path(instance, filename):
    """Get song directory path to save."""
    return f"media/songs/{instance.id}_{instance.name}_{filename}"
    
class Song(models.Model):
    artists = models.ManyToManyField("music.Artist", related_name="songs")
    name = models.CharField(max_length=200)
    song_file = models.FileField(null=True, upload_to=song_directory_path)
    

    
