import time
import datetime
import platform

def play_alarm_sound():
    if platform.system() == 'Windows':
        import winsound
        winsound.Beep(1000, 1000)  # Beep sound for 1 second
    else:
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load("alarm_sound.wav")  # Replace "alarm_sound.wav" with your sound file
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            play_alarm_sound()
            break
        else:
            print("Current Time:", current_time)
            time.sleep(1)  # Check every second

def main():
    # Set the alarm time
    alarm_time = input("Enter the alarm time (HH:MM:SS format): ")

    # Validate the input format
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format! Please use HH:MM:SS format.")
        return

    print("Alarm set for:", alarm_time)

    # Start the alarm clock
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
