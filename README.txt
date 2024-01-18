Hello and welcome to a very simple program that uses simpleaudio to play a .wav sound of coffee being poured into a mug
- and uses pyglet to display a gif of a coffee mug once the .wav file has finished playing.

Enter 'y' or 'Y' into the prompt to see the program, otherwise you'll get 'Okay, Bye!'

Additional setup information: The version of simpleaudio I had installed was 1.0.3 and the pyglet version was 1.5.8.
If the code is not working check to make sure you have these versions of the packages installed.

If you are using a MAC you may get the following error:
ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to (null)

To solve this enter this into the terminal after the $:
defaults write org.python.python ApplePersistenceIgnoreState NO

If you are finished with the program and experience errors with older programs be sure to change it back with the line:
defaults write org.python.python ApplePersistenceIgnoreState YES

(Thanks to Cbrnr on GitHub for finding the solution to this annoying bug!)

Credits:
The sole programmer for this program is myself, Nick Carlson @Nicks_Carlson on Twitter and CarlsonNicholas on Github.

I received major help with pyglet from this YouTube video:
https://www.youtube.com/watch?v=lEtdBsBFOxo&ab_channel=ParwizForogh (Thank you Parwiz!)

Special thanks to the creator of simpleaudio, Joe Hamilton and pyglet creator, Alex Holkner

Sound Source = http://soundbible.com/1244-Pouring-Hot-Tea.html (This is a open source .wav and .mp3 file)

(Don't mind the "Pouring-Hot-Tea" part it is totally coffee ;) )

The gif is my original art. Please credit me if you use it, thanks!