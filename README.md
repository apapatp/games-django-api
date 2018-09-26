To see the list of generated tables that are created after running a migrate command.
Note this is only for sqllite commands. Do the command below:

sqlite3 db.sqlite3 '.tables'

To specify a particular table, run this:
sqlite3 db.sqlite3 '.schema <table name>'

To do a normal query to see the content in a file, do this:
sqlite3 db.sqlite3 'SELECT * FROM <table_name> ORDER BY name'

We can launch our default Python interactive shell and make all the Django project modules available before it starts. This way, we can check that the serializer works as expected. In addition, it will help us understanding how serialization works in Django. Run the following command to launch the interactive shell. Make sure you are within the gamesapi folder in the Terminal or command prompt:

python manage.py shell
You will notice that a line that says (InteractiveConsole) is displayed after the usual lines that introduce your default Python interactive shell. Enter the following code in the Python interactive shell to import all the things we will need to test the Game model and its serializer. The code file for the sample is included in the restful_python_chapter_01_01 folder, in the serializers_test_01.py file:

from datetime import datetime
from django.utils import timezone
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from games.models import Game
from games.serializers import GameSerializer

gamedatetime = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
game1 = Game(name='Smurfs Jungle', release_date=gamedatetime, game_category='2D mobile arcade', played=False)
game1.save()
game2 = Game(name='Angry Birds RPG', release_date=gamedatetime, game_category='3D RPG', played=False)
game2.save()

print(game_serializer1.data)
game_serializer.data prints the dictionary version of the game model that has been serializer

JSONRenderer in the rest framework renderer helps to render data into Json. For example:
renderer = JSONRenderer()

rendered_g1 = renderer.render(game_serializer1.data)
rendered_g2 = renderer.render(game_serializer2.data)

# The other way around we can parse a json into a dictionary that can be saved in our serializer
json_string_for_new_game = '{"name":"Tomb Raider Extreme Edition","release_date":"2016-05-18T03:02:00.776594Z","game_category":"3D RPG","played":false}'
json_bytes_for_new_game = bytes(json_string_for_new_game , encoding="UTF-8") # stores it in bytes
stream_for_new_game = BytesIO(json_bytes_for_new_game) # Creates in memory for bytes
parser = JSONParser() # intializes the JSONParser class
parsed_new_game = parser.parse(stream_for_new_game) # parses the json into a dict
print(parsed_new_game)

# In order to save the newly parse game into the serializer, we use the
new_game_serializer = GameSerializer(data=parsed_new_game)
if new_game_serializer.is_valid():
    new_game = new_game_serializer.save()
    print(new_game_serializer)

Leveraging curl in our api tests. In the command line, you can leverage curl bty
putting int he command below:

curl -X GET <url>
curl -iX GET <url> - This gets all the data along with our request

Curl is awesome, but a better way to get clearer data in the terminal is through httpie,
which allows for a smoother version.
To install httpie via pip, do the command below:
pip install --upgrade httpie

and now you can run
http :8000/games/ and you should see a better more readable result.

If we want options to return value in django other than json, we can run the command:

http OPTIONS :8000/games/ after making some changes in the code