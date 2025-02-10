# terraform
#### Video Demo:  [https://www.youtube.com/watch?v=FrfoIvm_zII](https://www.youtube.com/watch?v=FrfoIvm_zII)
![The title page for the game Terraform, showing an astronaut or worker in a hazmat suit standing in front of a barren landscape](/images/backgrounds/start_background.png)

You are an astronaut, or perhaps a hazmat worker, and you are tasked with beautifying a barren landscape. The atmosphere is stable (even if you can't breathe it). The soil is clean. All you need to do at this point is plant and wait for the seedlings to grow.

Maybe one day, as the result of your efforts, you'll be able to take off your helmet and breathe the air. (That's for a future project though.)

<hr />

Terraform is a tiny game inspired in one part by flash mini games of the 2000s and in one part 2010s and 2020s interplantary exploration, desert beautification, and post-nuclear disaster rehabilitation futurism.

It's also my final project for [Harvard's CS50x course](https://cs50.harvard.edu/x/2025/) which I took in 2024 and finished in early 2025.

The game is coded in Python using the Pygame library.
All graphics are designed and illustrated by me (Sarah Hudson).

<hr />

## About

### Project Structure
* **files**
    * plant_library.py
        * contains all information on the individual plants, including dimensions and images.
    * setup.py
        * the bulk of the project code.
* **images**
    * backgrounds
        * all images related to the backgrounds of the game's canvas.
    * buttons
        * all images related to clickable buttons (including inactive and hover states)
    * plants
        * all images for each growable plant, grouped in folders by plant.
* **terraform.py**
    * the Python file that starts the game.

### Project Design
The parameters for the final project for CS50x are [very open](https://cs50.harvard.edu/x/2025/project/), so I wanted to take this opportunity to learn to use the Pygame library and explore basic game development.

I based the concept of this project around developing basic farm game mechanics, and I hope to apply what I learnt throughout development to making more games in the future.

#### Growing Plants
The plants are sprites, and are created using the Plant constructor.

When the player clicks on the ground, a new instance of the Plant constructor is added to the plants group.

To implement basic perspective, each plant has a layer which corresponds to the location on the screen clicked by the player. Plants placed towards the lower part of the screen are drawn over plants placed towards the upper part of the screen. The Layered Updates sprite group handles the placement on screen according to its layer.

Each plant instance keeps track of its in game age. The images for each growing plant are stored in the [Plant Library](files/plant_library.py), and the image drawn updates with the age of the selected plant until the plant is fully grown. (For example, on Day 0 the plant will be represented by Image 0, on Day 1 the plant will be represented by Image 1, and so on.)

#### Game Clock
The game is run at 60 frames per second, and each day in the game lasts 6 seconds.

The passing of each day is indicated visually through changing the colour of the sky from yellow (for morning) to blue (for midday) to purple (for evening).

At the end of each day, all plants are updated and "age" forward one day.

#### Button Design
All player interactivity involving buttons is text-based but uses images as buttons.

As a reference, while creating all the buttons in the game I followed [this video tutorial by Coding with Russ](https://www.youtube.com/watch?v=G8MYGDf_9ho).

I chose to do an onClick event for the buttons that select the plants to give some indication that the player selected a plant. I did not set this up for the start, exit, and reset buttons as there is an immediate action happens when these buttons are selected.

### Game Art
The game and art assets are designed and illustrated by me.

The exception is the font, Jack Armstrong BB, which I chose because it emulates comic book lettering.

I used Procreate to color and ink the title screen and backgrounds. The line art of the plants were drawn and inked by hand in my sketchbook and then digitally coloured in Procreate.

I opted for a 800x600 canvas size to emulate the lower resolution look of flash games from the 2000s.

My goal with the art was to create something that felt handmade and a bit retro, so I opted for a stylized, illustrated look.

### Future Goals
At the moment, this game is a small toy, and I'd like to expand it beyond the scope of CS50.

Here's some ways I'm thinking about doing this:

* Make game longer.
* Add story elements.
* Add challenge to plant growth.
* Add goal - maybe one day our astronaut will be able to take off their helmet and enjoy the air of the (currently toxic) enviroment.

Follow me on [Instagram](http://instagram.com/sarahhmakes) or [Mastodon](http://mastodon.art/@sarahhmakes) to see what happens next!