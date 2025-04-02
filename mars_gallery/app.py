from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mars_gallery():
    images = [
        {"filename": "mars1.jpg", "title": "Маск хочет туда перебраться"},
        {"filename": "mars2.jpg", "title": "Маск хочет туда перебраться"},
        {"filename": "mars3.jpg", "title": "Маск хочет туда перебраться"},
        {"filename": "mars4.jpg", "title": "Маск хочет туда перебраться"}
    ]
    return render_template('gallery.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)
