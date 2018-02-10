from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model import Base, Stats
from flask import Flask, render_template, url_for
from flask import request, redirect


app = Flask(__name__)

# connect to database
engine = create_engine('sqlite:///Stats.db')
Base.metadata.bind = engine

# create database session

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/playerlist')
def player_list():
	players = session.query(Stats).order_by(asc(Stats.player))
	return render_template('player_list.html', players=players)


@app.route('/createplayer', methods=['GET', 'POST'])
def create_player():
	if request.method == 'POST':
		new_name = request.form['name']
		new_player = Stats(player = new_name, game = 0, win = 0, lose = 0)
		session.add(new_player)
		session.commit()
		return redirect(url_for('player_list'))
	else:
		return render_template('create_player.html')


@app.route('/startgame', methods=['GET', 'POST'])
def start_game():
	if request.method == 'POST':
		player1 = request.form['player1']
		player2 = request.form['player2']
		if player1 == player2:
			return redirect(url_for('start_game'))
		else:
			return redirect(url_for('play_game', player1=player1, player2=player2))
	else:	
		players = session.query(Stats).order_by(asc(Stats.player))
		return render_template('start_game.html', players=players)


@app.route('/playgame/<string:player1>vs<string:player2>/', methods=['GET', 'POST'])
def play_game(player1,player2):
	

@app.route('/leaderboard')
def leaderboard():
	



if __name__ == '__main__':
    app.debug = True
    app.run()
