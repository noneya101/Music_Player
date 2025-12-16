import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from pydub import AudioSegment

def play_music(folder, song_name):
    file_path = os.path.join(folder, song_name)

    if not os.path.exists(file_path):
        print("File not found")
        return

    
    if file_path.endswith(".m4a"):
        song_wav = file_path.replace(".m4a", ".wav")
        audio = AudioSegment.from_file(file_path, format="m4a")
        audio.export(song_wav, format="wav")
        file_path = song_wav


    if not os.path.exists(file_path):
        print("File not found")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"\nNow playing: {song_name}")
    print("commands: [P]ause, [R]esume, [S]top")

    while True:

        command = input("> ").upper()

        if command == "P":
            pygame.mixer.music.pause()
            print("Paused")
        elif command == "R":
            pygame.mixer.music.unpause()
            print("Resumed")
        elif command == "S":
            pygame.mixer.music.stop()
            print("Stopped")
            return
        else:
            print("Invalid command")
def main():

    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio initialization failled! ", e)
        return

    folder = "music"

    if not os.path.isdir(folder):
       print(f"Folder '{folder}' not found")
       return

    music_files = [file for file in os.listdir(folder) if file.endswith((".mp3", ".m4a", ".wav", ".ogg"))]

    if not music_files:
        print("no .music files found!")

    while True:
        print("*****Music PLAYER *****")
        print("My song list:")

        for index, song in enumerate(music_files, start=1):
            print(f"{index}.{song}")

        choice_input = input("\nEnter the song # to play (or 'Q' to quit): ")

        if choice_input.upper() == "Q":
            print("BYE!")
            break

        if not choice_input.isdigit():
            print("Enter a valid number")
            continue

        choice = int(choice_input) - 1

        if 0 <= choice < len(music_files):
            play_music(folder,music_files[choice])
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()



