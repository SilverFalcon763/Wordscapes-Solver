Wordscapes Solver

A solver for the mobile game "Wordscapes" using computer vision

About
>This project is a solver for the mobile game "Wordscapes" to be used on a computr running Windows OS. The solver requires that you have the android emulator "Bluestacks" downloaded and on it, have "Wordscapes" dowloaded. I decided to make this project because I always see my mom playing it and she is at a very high level, so my goal was to see if I could build a solver for it and see how long it would take it to catch up to the same level as my mom. While I was unable to completely finish the project, I am proud of what I was able to complete, and despite the program not being able to actually guess the words and be completely automated, it still provides guesses that significantly help the person playing.


Goals and requirements
>Design Doc: https://docs.google.com/document/d/1Q90GQIqPvT8YkVg-ud_bCqOer_MYdidJw1zG0qGWNXg/edit
>
>Goals:
>> Have the program recognize how many letters there are in a level, the amount of words that exist for each length of word, and what letters are given
>> Have the program sort through a dictionary text file and comprise a list of all words containing the given letters, then guess those words by using a MouseClick or similar method
>> Have the program check the board each time and use clues to guess words, such as letters from a different word intersecting with the current word a providing a letter of the current word

>Non-goals: 
>> Make a program that randomly chooses letters in any order or combination


Sprint Goal
> Have the program be able to compile a list of words based on given word lengths and letters for game levels WITHOUT duplicate letters
> Have the program use the list of words to guess letters by finding the location of letters and interacting with the mouse of the computer
> If both these goals have been completed, go back and attempt to make the program able to compile a list of words based on given word lengths and letters for game levels WITH duplicate letters
> Clean up code/make it look nicer and be easier to read


Key learnings
>I learned a lot of things from this project, the biggest being: check how old the libraries you decide to use are, because when you're almost done with your project and one of them decides to stop working, it's not fun. On the bright side, I learned a lot more about python that I already knew, such as how to write for loops, sort through arrays, and how to optimize and refactor code. Overall, I learned that projects don't always work out in the way that you want them to, but I also learned that they don't have to in order for you to get value from them.


Running your project
>To run this project, you would first download the project and extract is to your desktop. Once that has been completed, you would have to download Bluestacks from "https://www.bluestacks.com/bluestacks-5.html" and install Wordscapes from the app store within Bluestacks. Once that has been done, it should simply be a matter of opening Wordscapes and double clicking the solver.py file.


Copyright
>This project is licensed under the terms of the MIT license and protected by Udacity Honor Code and Community Code of Conduct. See license and disclaimer.
