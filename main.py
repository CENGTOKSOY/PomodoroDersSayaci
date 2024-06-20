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

# Define the Pomodoro Timer class
class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Ders Çalışma Sayacı")
        self.master.configure(bg='black')
        self.master.resizable(False, False)

        # Set default values
        self.work_time = 25 * 60  # 25 dakika
        self.break_time = 5 * 60  # 5 dakika
        self.repetitions = 4
        self.current_time = self.work_time
        self.running = False
        self.is_break = False

        # Create a canvas for the countdown circle
        self.canvas = tk.Canvas(master, width=200, height=200, bg='black', highlightthickness=0)
        self.canvas.pack(pady=20)

        # Create a label for the countdown timer
        self.timer_label = tk.Label(master, text=self.format_time(self.current_time), fg='white', bg='black', font=('Helvetica', 48))
        self.timer_label.pack(pady=20)

        # Create a combobox for sound selection with a label
        sound_label = tk.Label(master, text="🔊 Ses Seçimi", fg='white', bg='black', font=('Helvetica', 12))
        sound_label.pack(pady=5)
        self.sound_var = tk.StringVar()
        self.sound_combobox = ttk.Combobox(master, textvariable=self.sound_var, values=list(sounds.keys()), state='readonly')
        self.sound_combobox.set("fire")  # Default value
        self.sound_combobox.pack(pady=10)

        # Create a volume slider with a label
        volume_label = tk.Label(master, text="🔊 Ses Seviyesi", fg='white', bg='black', font=('Helvetica', 12))
        volume_label.pack(pady=5)
        self.volume_slider = ttk.Scale(master, from_=0, to=1, orient="horizontal", command=self.set_volume)
        self.volume_slider.set(0.5)  # Default volume
        self.volume_slider.pack(pady=10)

        # Create work time slider with a label
        work_time_label = tk.Label(master, text="⏰ Çalışma Süresi", fg='white', bg='black', font=('Helvetica', 12))
        work_time_label.pack(pady=5)
        self.work_time_slider = ttk.Scale(master, from_=1, to=60, orient="horizontal", command=self.update_work_time)
        self.work_time_slider.set(25)  # Default work time
        self.work_time_slider.pack(pady=10)

        # Create break time slider with a label
        break_time_label = tk.Label(master, text="☕ Mola Süresi", fg='white', bg='black', font=('Helvetica', 12))
        break_time_label.pack(pady=5)
        self.break_time_slider = ttk.Scale(master, from_=1, to=30, orient="horizontal", command=self.update_break_time)
        self.break_time_slider.set(5)  # Default break time
        self.break_time_slider.pack(pady=10)

        # Create start, stop, and reset buttons
        self.button_frame = tk.Frame(master, bg='black')
        self.button_frame.pack(pady=10)

        self.start_button = ttk.Button(self.button_frame, text="Başlat", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = ttk.Button(self.button_frame, text="Durdur", command=self.stop_timer)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.reset_button = ttk.Button(self.button_frame, text="Sıfırla", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=5)

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
            color = self.calculate_color_transition(self.current_time, self.work_time if not self.is_break else self.break_time)
            self.canvas.create_arc(10, 10, 190, 190, start=90, extent=-360 * (self.current_time / (self.work_time if not self.is_break else self.break_time)), outline=color, width=2, style='arc')

            if self.current_time <= 0:
                self.stop_timer()
                if not self.is_break:
                    self.is_break = True
                    self.current_time = self.break_time
                else:
                    self.is_break = False
                    self.current_time = self.work_time
                    self.repetitions -= 1
                if self.repetitions > 0:
                    self.start_timer()
                else:
                    self.show_completion_effect()

    def calculate_color_transition(self, current_time, total_time):
        # Define white and blue RGB values
        white = (255, 255, 255)
        blue = (0, 0, 255)
        # Calculate the ratio of the current time to the total time
        ratio = current_time / total_time
        # Calculate new RGB values based on the ratio
        new_red = int(white[0] + (blue[0] - white[0]) * (1 - ratio))
        new_green = int(white[1] + (blue[1] - white[1]) * (1 - ratio))
        new_blue = int(white[2] + (blue[2] - white[2]) * (1 - ratio))
        # Return the new color in hexadecimal format
        return f'#{new_red:02x}{new_green:02x}{new_blue:02x}'

    def show_completion_effect(self):
        # Show a green circle with a check mark
        self.canvas.delete("all")
        self.canvas.create_oval(10, 10, 190, 190, outline='green', width=2)
        self.canvas.create_text(100, 100, text="✔", fill='green', font=('Helvetica', 48))

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

    def update_work_time(self, val):
        self.work_time = int(float(val)) * 60
        if not self.running and not self.is_break:
            self.current_time = self.work_time
            self.timer_label.config(text=self.format_time(self.current_time))

    def update_break_time(self, val):
        self.break_time = int(float(val)) * 60
        if not self.running and self.is_break:
            self.current_time = self.break_time
            self.timer_label.config(text=self.format_time(self.current_time))

