from guizero import App, Text, TextBox, Picture, PushButton
#import pokebase as pb
from requests import get
from PIL import Image
from io import BytesIO

def fetch_pokemon():
    name = input_box.value
    poke = pokemon(name)
    pic = get(poke.sprites.front_default).content
    image = Image.open(BytesIO(pic))
    image.save('260.png')
    icon.value = '260.png'

app = App(title="Pokemon Fetcher", width=350, height=300,bgcolor=None)
welcome = Text(app, text="Which Pokemon would you like to fetch?")
input_box = TextBox(app)
submit = PushButton(app, text="Fetch", comman=fetch_pokemon)
icon = Picture(app, image='260.png')
app.display()