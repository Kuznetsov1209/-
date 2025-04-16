from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('carousel'))  # Перенаправление на /carousel


@app.route('/carousel')
def carousel():
    images = [
        {"filename": "mars1.jpg", "title": "Маск хочет туда перебраться"},
        {"filename": "mars2.jpg", "title": "Маск хочет туда перебраться"},
        {"filename": "mars3.jpg", "title": "Маск хочет туда перебраться"},
        {"filename": "mars4.jpg", "title": "Маск хочет туда перебраться"}
    ]
    return render_template('gallery.html', images=images)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
