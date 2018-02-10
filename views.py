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
	

@app.route('/startgame', methods=['GET', 'POST'])
def start_game():
	

@app.route('/playgame/<string:player1>vs<string:player2>/', methods=['GET', 'POST'])
def play_game(player1,player2):
	

@app.route('/leaderboard')
def leaderboard():
	



if __name__ == '__main__':
    app.debug = True
    app.run()
