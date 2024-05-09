import tkinter as tk
from tkinter import ttk
import time
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Define sound paths
sounds = {
    "fire": "fire_sound.mp3",
    "rain": "rain_sound.mp3",
    "waves": "waves_sound.mp3",
    "birds": "birds_sound.mp3",
    "storm": "storm_sound.mp3"
}

# Define a function to play background sound
def play_sound(sound_name):
    pygame.mixer.music.load(sounds[sound_name])
    pygame.mixer.music.play(-1)

# Define a function to stop background sound
def stop_sound():
    pygame.mixer.music.stop()


    def format_time(self, seconds):
        return time.strftime('%M:%S', time.gmtime(seconds))

    def update_timer(self):
        if self.running:
            self.current_time -= 1
            self.timer_label.config(text=self.format_time(self.current_time))
            self.master.after(1000, self.update_timer)

            # Update the countdown circle
            self.canvas.delete("all")
            # Create an empty circle (ring) with a white outline
            self.canvas.create_oval(10, 10, 190, 190, outline='white', width=2)
            # Create an arc inside the empty circle to represent the countdown
            # Calculate the color transition from white to brown
            color = self.calculate_color_transition(self.current_time, self.work_time)
            self.canvas.create_arc(10, 10, 190, 190, start=90, extent=-360 * (self.current_time / self.work_time), outline=color, width=2, style='arc')

            if self.current_time <= 0:
                self.stop_timer()
                if self.repetitions > 0:
                    self.repetitions -= 1
                    self.current_time = self.work_time
                    self.start_timer()

    def calculate_color_transition(self, current_time, total_time):
        # Define white and brown RGB values
        white = (255, 255, 255)
        brown = (165, 42, 42)
        # Calculate the ratio of the current time to the total time
        ratio = current_time / total_time
        # Calculate new RGB values based on the ratio
        new_red = int(white[0] + (brown[0] - white[0]) * (1 - ratio))
        new_green = int(white[1] + (brown[1] - white[1]) * (1 - ratio))
        new_blue = int(white[2] + (brown[2] - white[2]) * (1 - ratio))
        # Return the new color in hexadecimal format
        return f'#{new_red:02x}{new_green:02x}{new_blue:02x}'

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()
            play_sound(self.sound_var.get())

    def stop_timer(self):
        self.running = False
        stop_sound()

    def reset_timer(self):
        self.stop_timer()
        self.current_time = self.work_time
        self.timer_label.config(text=self.format_time(self.current_time))
        # Create an empty circle (ring) with a white outline
        self.canvas.create_oval(10, 10, 190, 190, outline='white', width=2)

# Ana pencereyi oluştur
root = tk.Tk()

# Pomodoro Timer uygulamasını oluştur
app = PomodoroTimer(root)

# Uygulamayı başlat
root.mainloop()
