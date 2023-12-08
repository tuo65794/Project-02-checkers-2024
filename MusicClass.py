import pygame
import pygame.mixer

pygame.mixer.init()
class BackgroundMusic:

    def __init__(self, tracks):
        self.tracks = tracks
        self.current_track = 0
        self.SONG_END = pygame.USEREVENT + 1

        pygame.mixer.music.set_endevent(self.SONG_END)

    def play_music(self):
        pygame.mixer.music.load(self.tracks[self.current_track])
        pygame.mixer.music.set_volume(0.1)  # Adjust volume between 0.1 and 1.0
        pygame.mixer.music.play()
        self.current_track = (self.current_track + 1) % len(self.tracks)

    def start_music_loop(self):
        self.play_music()

    def handle_event(self, event):
        if event.type == self.SONG_END:
            self.play_music()

