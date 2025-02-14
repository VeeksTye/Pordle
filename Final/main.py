#
#     (X) Include comments throughout the program (10 points)
#     (X) Use variables and list to store and access data. You can use tuple or dictionary in place of a list (20 points)
#     (X) Use string object to display and control text output. (10 points)
#     (X) Define 2 or more functions and use function calls to execute tasks in the program. (30 points)
#     (X) Implement loop (for or while or both) (20 points)
#     (X) Include conditional statement (if or if-else or if-elif-else) (10 points)
#     (X) Use a non-built-in module, custom module. (20 points)
#     (X) Contains at least 2 classes and 1 sub-class (30 points)
#     (X) Includes 1 or more objects and 1 or more methods in each class. (20 points)
#     (X) Implement error detection using Python built-in exceptions. (10 points)
#     (X) Implement file operations and file output. (20 points)
#     (X?) Integrate UI (optional): Bonus 30 points
#     Did UI as a joke, don't have to give me points
#

# custom libraries
import generator

# importing tkinter libraries for window usage
import tkinter as tk
import cv2
import pygame
from PIL import Image, ImageTk

# class that stores the user data and gets inputs
class User:
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins

    # function to get input
    def get_input(self):
        return input("Input: ")

    # return the amount of wins the user has
    def get_wins(self):
        return self.wins

# function to print out menu at the start of the program
def print_menu():
    print("Welcome to Pordle (Python Wordle)")
    print(
        "1. Play Game\n"
        "2. Rules\n"
        "3. Don't Click\n"
        "4. Profile\n"
        "5. Quit\n")

# checks to see if the user guess was the same as the word
def check_guess(guess, word, correct):
    if guess.lower() == word.lower():
        return True
    else:
        for i in range(5):
            # shows the correct guess of words
            correct[i] = guess[i] == word[i]

# class to show gif
def play_gif():
    root = tk.Tk()
    logo = tk.PhotoImage(file='Getting_Lobstered_Blue_Lobster_Jump_Scare_V2.gif')

    w1 = tk.Label(root, image=logo).pack(side='right')

    explanation = '''lobstar'''

    w2 = tk.Label(root,
                  justify=tk.LEFT,
                  padx=10,
                  text=explanation).pack(side="left")

    root.mainloop()
# class to play sound
def play_sound():
    window = tk.Toplevel()
    window.title("Video Player")
    window.geometry("800x600")  # adjust window size

    # Load the video
    video_path = r"C:\Users\scary\PycharmProjects\PythonProject\Final\Getting_Lobstered_Blue_Lobster_Jump_Scare_V1.mp3"
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Initialize Pygame for audio playback
    pygame.mixer.init()
    pygame.mixer.music.load(video_path)
    pygame.mixer.music.play()

    label = tk.Label(window)
    label.pack()

    def update_frame():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(image=img)
            label.img_tk = img_tk  # Prevent garbage collection
            label.config(image=img_tk)
            window.after(33, update_frame)  # Refresh at ~30 FPS
        else:
            cap.release()  # Release the video when done
            pygame.mixer.music.stop()  # Stop audio playback

    update_frame()
    window.mainloop()



def main():
    # asks for the users name and sets their wins to 0
    get_name = input("What is your name?: ")
    player = User(get_name, 0)

    while True:
        # keeps tracks of tries
        tries = 0
        print_menu()
        user_input = player.get_input()

        if user_input == "1":
            # creates a instance of the class and generates a random word
            word = generator.Generator()
            correct_word = word.generate_word()
            correct_guess = [False] * 5
            #print(correct_word) #(use for debugging)

            # loops the amount of guesses over and over again for 6 tries
            while True:
                tries += 1
                guess = input("Guess: ")
                if check_guess(guess, correct_word, correct_guess):
                    print("You Guessed Correctly!\n")
                    break
                else:
                    print(f"WRONG! Correct Letters: {correct_guess}")
                if tries == 6:
                    print(f"The word was: {correct_word}\n")
                    break

        elif user_input == "2":
            # prints out the rules of the game
            print("The rules of the game are:\n"
                  "You guess a 5 letter word and it will check to see if you got it right\n"
                  "If you did not, it will show what letters in that word were in the final product\n"
                  "Try to guess it before 3 tries or else you'll lose!\n")
        elif user_input == "3":
            play_gif()
            play_sound()

        elif user_input == "4":
            print(f"Name: {player.name}, Wins:{player.wins}\n")
        elif user_input == "5":
            print(f"Goodbye {player.name}!")
            break
        else:
            print("Invalid input\n\n")

if __name__ == '__main__':
    main()