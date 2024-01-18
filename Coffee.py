import pyglet
import os
import simpleaudio as sa

try:

    choice = input("Do you like coffee? (Y/N) ")
    choice.title()

    if choice.title() == "Y":

        gif_directory = os.path.dirname(__file__)
        gif_filename = os.path.join(gif_directory, 'CoffeeMug.gif')

        animation = pyglet.image.load_animation(gif_filename)
        animSprite = pyglet.sprite.Sprite(animation)

        w = animSprite.width
        h = animSprite.height

        window = pyglet.window.Window(width=w, height=h)

        r, g, b, omega = 0.5, 0.5, 0.8, 0.5

        pyglet.gl.glClearColor(r, g, b, omega)


        @window.event
        def on_draw():
            window.clear()
            animSprite.draw()


        directory = os.path.dirname(__file__)
        filename = os.path.join(directory, 'HotCoffee.wav')
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()

        pyglet.app.run()

        print("Come back soon!")

    else:
        print("Okay, Bye!")

except KeyboardInterrupt:
    print()
    print("User exited, Come back soon for another cup!!")
except Exception as x:
    print(f"Unknown Error: {x}")
