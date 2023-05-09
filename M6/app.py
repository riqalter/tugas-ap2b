from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        return render_template('result.html', nama=nama, email=email)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)