class Son:
    """Class to represent a song

    Attributes:
    tittle(str): The title of the song
    artist(Artist) : An artist object represnting the songs creator.
    duration(int) : The duration of the song in seconds.May be zero
    """

    def __init__(self,title,artist,duration=0):
        """song init method
        Args:
        title(str):Intialises the 'title' attribute
        artist(Artist) : At Artist object represnting the song's creator
        duration (Optional(int)): Initial value for the 'duration' attribute
            will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration

