from flask import Blueprint, render_template, request, jsonify, session, g, redirect
from .models import User, GuessedImages, InProgressImages, Images, GameRecord, db
from sqlalchemy import func
import requests

game_bp = Blueprint('game', __name__)

@game_bp.before_app_request
def add_user_to_g():
    """If user is logged in, add the user object to Flask global."""
    if "user_id" in session:
        g.user = User.query.get(session["user_id"])
    else:
        g.user = None

@game_bp.route('/')
def index():
    """Show index page."""

    if not g.user:
        return redirect('/signup')
    
    if not session:
        return redirect('/select-game-meme')
    else:
        return render_template('/game/welcome.html')

@game_bp.route('/home')
def render_home_page():
    
    if not g.user:
        return redirect('/login')

    round = session["round"]
    round_meme = session["round_meme"]
    
    guess_image_id = session["guess_image"]
    guess_image = GuessedImages.query.filter_by(id=guess_image_id).first()

    if round_meme is None or round == 4 or guess_image.completed == True:
        return redirect('/select-game-meme')

    src = session["src"]
    
    return render_template("/game/welcome.html", src=src)

@game_bp.route('/game-over')
def render_game_over_page():
    # send player score graphics
    src = session["src"]

    return render_template("/game/postgame.html", src=src)

@game_bp.route('/select-game-meme')    
def select_meme_for_game():

    if not g.user:
        return redirect('/login')

    user = g.user
    # SELECT RANDOM IMAGE FROM DATABASE
    current_image = Images.query.order_by(func.random()).first()

    # INSTANTIATE IMAGE FOR ROUND 
    round_meme = InProgressImages(
                image_id = current_image.id,
                user_id = user.id,
                in_round = True
                )
    guess_image = GuessedImages(
                image_id = current_image.id,
                user_id = user.id,
                round = 0,
                completed = False
                )

    db.session.add(round_meme)
    db.session.add(guess_image)
    db.session.commit()

    print(guess_image.round)

    # SAVE TO SESSION FOR REFERENCE ON INDEX
    session["round_meme"] = round_meme.id
    session["round"] = 0

    session["guess_image"] = guess_image.id
    session["src"] = guess_image.database_images.image_data

    return redirect('/home')
    

@game_bp.route('/update-game-meme')
def update_guessed_image():

    # ROUND NEEDS TO BE REFERENCED -  UPDATE GUESSEDIMAGE ROUND
    round = session['round']
    round_meme_id = session["round_meme"]
    round_meme = InProgressImages.query.filter_by(id=round_meme_id).first()
    guess_image_id = session["guess_image"]
    guess_image = GuessedImages.query.filter_by(id=guess_image_id).first()

    update_image = round_meme.guessed_images[0]

    if guess_image != update_image:
        return 'Internal Reference Error: Session and Database'

    # FROM GAME.JS
    keyword = request.args['keyword']

    if update_image is None or round_meme.in_round == False or update_image.completed == True:
        return 'No game meme found in session'

    image = update_image.database_images

    if image is None:
        return 'No image found for game meme'

    words = {word.word.lower() for word in image.image_words}
    if keyword.lower() in words:
        round += 1
        session["round"] = round

        update_image.round = round
        phrase = update_image.database_images.phrase
        guess_image.completed = True
        db.session.commit()

        game_record = GameRecord(user_id=g.user.id, guessed_image_id=guess_image.id, round=round)
        db.session.add(game_record)
        db.session.commit()


        return jsonify({'result': 'correct', 'message': 'You are a Lord over Lords.', 'phrase': phrase})

    else:
        # Update the game round and save the updated object
        if round == 4:
            phrase = update_image.database_images.phrase
            update_image.completed = True
            db.session.commit()

            game_record = GameRecord(user_id=g.user.id, guessed_image_id=guess_image.id, round=round)
            db.session.add(game_record)
            db.session.commit()

            return jsonify({'result': 'game-over', 'message': "You've run out of guesses.", 'phrase': phrase})
            
        else:
            round += 1
            session["round"] = round
            update_image.round = round
            db.session.commit()
            # Return the updated game_meme object in the JSON response
            return jsonify({'result': 'not-correct', 'message': 'Better luck next time.'})

@game_bp.route('/get-game-record', methods=['GET'])
def get_game_record():
    """Return the most recent GameRecord for the logged-in user."""
    if not g.user:
        return jsonify({'error': 'User not logged in'}), 401

    latest_game_record = (
        GameRecord.query
        .filter_by(user_id=g.user.id)
        .order_by(GameRecord.id.desc())
        .first()
    )

    if latest_game_record:
        record_data = {
            'id': latest_game_record.id,
            'user_id': latest_game_record.user_id,
            'guessed_image_id': latest_game_record.guessed_image_id,
            'round': latest_game_record.round
        }
        return jsonify(record_data)
    else:
        return jsonify({'error': 'No GameRecord found for user'}), 404