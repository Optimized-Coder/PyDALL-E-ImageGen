from flask import Flask, redirect, request
import openai
from dotenv import load_dotenv, find_dotenv
import os

def create_app():
    app = Flask(__name__)
    load_dotenv(find_dotenv())
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    @app.route('/')
    def index():
        # get default height if height is not specified
        def get_height():
            if request.args.get('height') == None:
                height = '512'
            else:
                height = request.args.get('height')
            return height
            
        
        height = get_height()
        width = height
        noun = request.args.get('noun')
        color = request.args.get('color')
        action = request.args.get('action')

        def create_image(prompt):
            generation_response = openai.Image.create(
                prompt=prompt,
                n=1,
                size=f'{height}x{width}',
                response_format = 'url'
            )
            generated_image_url = generation_response["data"][0]["url"]  

            return redirect(generated_image_url)

        img = create_image(f'{noun} {action} with main image color of {color}')
        return img
    
    return app