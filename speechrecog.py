import speech_recognition as sr
import pygame
import os

def play_music(song_name):
    pygame.mixer.init()
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Voice-controlled Music Player: Listening for commands...")
        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()

                if "play" in command:
                    song_name = command.replace("play", "").strip()
                    play_music(f"{song_name}.mp3")
                elif "stop" in command:
                    stop_music()
                elif "exit" in command:
                    print("Exiting Voice-controlled Music Player.")
                    break
                else:
                    print("Unknown command. Try 'play', 'stop', or 'exit'.")

            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Error with the speech recognition service: {e}")

if __name__ == "__main__":
    main()
