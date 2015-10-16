#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for

app = Flask(__name__)

players = [
    {
        'id': 1,
        'playerName': u'A. Uno',
        'ballControl': 9,
        'mileTime': u'5:10',
        'height': 67
    },
    {
        'id': 2,
        'playerName': u'J. Two',
        'ballControl': 6,
        'mileTime': u'8:15',
        'height': 72
    },
    {
        'id': 3,
        'playerName': u'D. Trio',
        'ballControl': 10,
        'mileTime': u'5:15',
        'height': 68
    },
    {
        'id': 4,
        'playerName': u'D. Quarter',
        'ballControl': 8,
        'mileTime': u'7:45',
        'height': 71
    },
    {
        'id': 5,
        'playerName': u'T. Five',
        'ballControl': 7,
        'mileTime': u'8:47',
        'height': 69
    }
]

playersByBallControl = []
playersByMileTime = []
playersByHeight = []


@app.route('/teamo/api/v1.0/players', methods=['GET'])
def get_players():
    return jsonify({'players': [make_public_player(player) for player in players]})


@app.route('/teamo/api/v1.0/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = [player for player in players if player['id'] == player_id]
    if len(player) == 0:
        abort(404)
    return jsonify({'player': player[0]})


@app.route('/teamo/api/v1.0/players', methods=['POST'])
def create_player():
    if not request.json or 'playerName' not in request.json:
        abort(400)
    player = {
        'id': players[-1]['id'] + 1,
        'playerName': request.json['playerName'],
        'ballControl': request.json.get('ballControl', ""),
        'mileTime': request.json.get('mileTime', ""),
        'height': request.json.get('height', "")
    }
    players.append(player)
    return jsonify({'player': player}), 201


@app.route('/teamo/api/v1.0/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    player = [player for player in players if player['id'] == player_id]
    if len(player) == 0:
        abort(404)
    players.remove(player[0])
    return jsonify({'result': True})


@app.route('/teamo/api/v1.0/players/sort/ballControl', methods=['GET'])
def sortByBallControl():
    topPlayer = {}
    usedPlayerNames = []
    for player in playersByBallControl:
        usedPlayerNames.append(player.get('playerName'))
    for player in players:
        if player.get('playerName') not in usedPlayerNames:
            if player.get('ballControl') > topPlayer.get('ballControl'):
                topPlayer = player
    playersByBallControl.append(topPlayer)
    if len(playersByBallControl) < len(players):
        sortByBallControl()
    return jsonify({'players': playersByBallControl})


@app.route('/teamo/api/v1.0/players/sort/mileTime', methods=['GET'])
def sortByMileTime():
    topPlayer = {}
    usedPlayerNames = []
    for player in playersByMileTime:
        usedPlayerNames.append(player.get('playerName'))
    for player in players:
        if player.get('playerName') not in usedPlayerNames:
            if player.get('mileTime') > topPlayer.get('mileTime'):
                topPlayer = player
    playersByMileTime.append(topPlayer)
    if len(playersByMileTime) < len(players):
        sortByMileTime()
    return jsonify({'players': playersByMileTime})


@app.route('/teamo/api/v1.0/players/sort/height', methods=['GET'])
def sortByHeight():
    topPlayer = {}
    usedPlayerNames = []
    for player in playersByHeight:
        usedPlayerNames.append(player.get('playerName'))
    for player in players:
        if player.get('playerName') not in usedPlayerNames:
            if player.get('height') > topPlayer.get('height'):
                topPlayer = player
    playersByHeight.append(topPlayer)
    if len(playersByHeight) < len(players):
        sortByHeight()
    return jsonify({'players': playersByHeight})


def make_public_player(player):
    new_player = {}
    for field in player:
        if field == 'id':
            new_player['uri'] = url_for('get_player', player_id=player['id'], _external=True)
        else:
            new_player[field] = player[field]
    return new_player


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
