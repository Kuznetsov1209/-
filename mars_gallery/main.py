from flask import Flask, render_template, redirect, url_for, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Создаем папку для загрузок, если ее нет
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def get_gallery_images():
    images = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if allowed_file(filename):
            images.append({
                "filename": filename,
                "title": "Марсианский пейзаж",
                "description": "Фотография с поверхности Марса"
            })
    return images


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return redirect(request.url)

        file = request.files['photo']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return redirect(url_for('carousel'))


@app.route('/carousel', methods=['GET', 'POST'])
def carousel():
    images = get_gallery_images()
    return render_template('gallery.html', images=images)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)