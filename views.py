from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model import Base, Stats
from flask import Flask, render_template, url_for
from flask import request, redirect, flash


app = Flask(__name__)

# connect to database
engine = create_engine('sqlite:///Stats.db')
Base.metadata.bind = engine

# create database session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# home page
@app.route('/')
def home():
	return render_template('home.html')

# create player page
@app.route('/createplayer', methods=['GET', 'POST'])
def create_player():
	if request.method == 'POST':
		player = request.form['name']
		# checking for existing player
		existing = session.query(Stats).filter_by(player=player).scalar() is not None
		# show flash message if player already exist
		if existing:
			flash("Player already exist. Try entering different name")
			return redirect(url_for('create_player'))
		# if player not exist then create new player in database
		else:
			new_player = Stats(player = player, game = 0, win = 0, lose = 0)
			session.add(new_player)
			session.commit()
			return redirect(url_for('start_game'))
	else:
		return render_template('create_player.html')


# start game page
@app.route('/startgame', methods=['GET', 'POST'])
def start_game():
	if request.method == 'POST':
		# redirect to the play game page
		player1 = request.form['player1']
		player2 = request.form['player2']
		return redirect(url_for('play_game', player1=player1, player2=player2))
	else:
		# if get rquest then show the start game page
		players = session.query(Stats).order_by(asc(Stats.player))
		return render_template('start_game.html', players=players)


@app.route('/playgame/<string:player1>vs<string:player2>/', methods=['GET', 'POST'])
def play_game(player1,player2):
	if request.method == 'POST':
		if request.form["player"] == player1:
			winner = session.query(Stats).filter_by(player=player1).one()
			loser = session.query(Stats).filter_by(player=player2).one()
			winner.game = winner.game + 1
			winner.win = winner.win + 1
			loser.game = loser.game + 1
			loser.lose = loser.lose + 1
			session.commit()
			return redirect(url_for('leaderboard'))
		elif request.form["player"] == player2:
			winner = session.query(Stats).filter_by(player=player2).one()
			loser = session.query(Stats).filter_by(player=player1).one()
			winner.game = winner.game + 1
			winner.win = winner.win + 1
			loser.game = loser.game + 1
			loser.lose = loser.lose + 1
			session.commit()
			return redirect(url_for('leaderboard'))
	return render_template('play_game.html', player1=player1, player2=player2)


@app.route('/leaderboard')
def leaderboard():
	players = session.query(Stats).order_by(Stats.win.desc(),Stats.lose.asc()).all()
	return render_template('leaderboard.html',players=players)



if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run()
