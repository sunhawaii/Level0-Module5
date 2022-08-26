"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    pet=simpledialog.askstring(title= "Pet Choice", prompt = "What type of pet do you want?(Dog, cat, fish, hamster, bird)")

    happiness_level = 0
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    while happiness_level < 100:
        activity_choice=simpledialog.askstring(title="Pet Activities", prompt="What do you you want to do to make your pet happier?(Feed, Walk, Play)")
        if activity_choice == 'feed':
            if pet == 'dog':
                happiness_level= happiness_level+20
            if pet == 'cat':
                happiness_level=happiness_level+15
            if pet == 'fish':
                happiness_level= happiness_level+30
            if pet == 'hamster':
                happiness_level= happiness_level+32
            if pet == 'bird':
                happiness_level= happiness_level+15
        if activity_choice == 'walk':
            if pet == 'dog':
                happiness_level= happiness_level+20
            if pet == 'cat':
                happiness_level= happiness_level-10
            if pet == 'fish':
                happiness_level= happiness_level-300
                messagebox.showerror("your fish has died")
                exit()
            if pet == 'hamster':
                happiness_level= happiness_level-20
            if pet == 'bird':
                happiness_level= happiness_level+500
                messagebox.showerror("your bird has run away")
                exit()
        if activity_choice == 'play':
            if pet == 'dog':
                happiness_level= happiness_level+30
            if pet == 'cat':
                happiness_level= happiness_level+20
            if pet == 'fish':
                happiness_level= happiness_level+5
            if pet == 'hamster':
                happiness_level= happiness_level+10
            if pet == 'bird':
                happiness_level= happiness_level+15
    if happiness_level >= 100:
        messagebox.showinfo(title=None, prompt="you made your pet happy!")
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pass
