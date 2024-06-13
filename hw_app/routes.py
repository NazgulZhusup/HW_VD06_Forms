from flask import render_template, request, redirect, url_for

from hw_app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobie = request.form.get('hobie')
        age = request.form.get('age')

        if name and city and hobie and age:
            posts.append({'name': name, 'city': city, 'hobie': hobie, 'age': age})

        return redirect(url_for('index'))
    return render_template('anketa.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
