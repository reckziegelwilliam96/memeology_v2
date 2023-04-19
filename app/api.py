from flask import Blueprint, jsonify, request, session
from .models import Images, ImageWords, GuessedImages, db
import requests

api_bp = Blueprint('api', __name__)

@api_bp.route('/caption-image', methods=['POST'])
def generate_meme():
    print("CAPTION_IMAGES CALLED!")
    print(request.get_data())
    print(request.get_json())
    print("Headers:", request.headers)
    print("Data:", request.data)
    print("JSON:", request.get_json())

    guess_image_id = session["guess_image"]
    guess_image = GuessedImages.query.filter_by(id=guess_image_id).first()
    template_id = guess_image.database_images.template_id;
    username = "memeoacct"
    password = "memeologyacct"
    text0 = request.json['topText']
    text1 = request.json['bottomText']

    payload = {
        'template_id' : template_id,
        'username' : username,
        'password' : password,
        'text0' : text0,
        'text1' : text1
    }

    url = "https://api.imgflip.com/caption_image"
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return "Internal Server Error", 500
