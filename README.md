# TeamoAPI
The API for Teamo! Housing the backend API code that will change the game of soccer.

View our frontend work [here](https://github.com/justinpotts/teamo/), and our final product [here](https://justinpotts.github.io/teamo/).

## How to Install Teamo API
The only prerequisite is to have Flask installed.

This can be done through `pip install flask`.

## How to Use
Note: At this point in time, the API is using default test data included with the code. In future versions,
you will be able to send your own JSON data through the API.

To start the web server, run `python app.py`, then either access the API through a browser by visiting `http://127.0.0.1:5000/` or using curl from the command line.

### Stucture
All JSON data sent to and from the Teamo API will be in the following structure.

```
[
  {
    'id':1
    'playerName':'John Smith'
    'ballControl':10
    'mileTime':'6:37'
    'height':'72'
  }
]
```
`id`: int, automatically defined

`playerName`: String, user-defined

`ballControl`: int, user-defined

`mileTime`: String, user-defined (Will be converted to a Python datettime object in the API)

`height`: int, user-defined

To make a call to the Teamo API, use any request module to make an API call creating player, passing in
JSON data. Make a call to sort one of three ways and Teamo will return the player roster sorted. Only
make one sort call per instance to avoid errors in sorting.

### API Calls

#### Get players
`curl -i http://localhost:5000/teamo/api/v1.0/players`

Returns players in JSON data in structure presented above

#### Get individual player
`curl -i http://localhost:5000/teamo/api/v1.0/players/<id>`

Returns an individual player with id in JSON data in structure presented above. If no player matches given id, returns 404 error in JSON.

#### Create player
`curl -i -H "Content-Type: application/json" -X POST -d “{“””playerName”””:”””<name>”””}” http://localhost:5000/todo/api/v1.0/players`

Creates a player with playerName element. The other elements will be implemented shortly.

#### Sort players by ball control
`curl -i http://localhost:5000/teamo/api/v1.0/players/sort/ballControl`

Sorts players in database by ballControl element

##### Sort players by mile time
`curl -i http://localhost:5000/teamo/api/v1.0/players/sort/mileTime`

Sorts players in database by mileTime element

##### Sort players by height
`curl -i http://localhost:5000/teamo/api/v1.0/players/sort/height`

Sorts players in database by height element

## Build on Teamo API
Want to build on our API? We use a Java applet as our main service to run with Teamo, but you're welcome to build your own! All you need to do is build the front-end and user input system, pass Teamo API the JSON data, then interpret the response.

You can start from scratch, or fork our build [here](https://github.com/justinpotts/teamo/)!
