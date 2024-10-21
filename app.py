from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory('images', filename)

@app.route('/portfolio/wedding_photography')
def wedding_photography():
    return render_template('portfolio/wedding_photography.html')

@app.route('/portfolio/portrait_photography')
def portrait_photography():
    return render_template('portfolio/portrait_photography.html')

@app.route('/portfolio/still_life')
def still_life():
    return render_template('portfolio/still_life.html')

# Блог
@app.route('/5_poriad_dlia_pochatkivtsiv')
def poriad():
    return render_template('blog/5_poriad_dlia_pochatkivtsiv.html')

@app.route('/chomu_vazhlyvo_obraty_styl')
def styl():
    return render_template('blog/chomu_vazhlyvo_obraty_styl.html')

@app.route('/osnovy_kompozytsii')
def kompozytsiia():
    return render_template('blog/osnovy_kompozytsii.html')

@app.route('/vybir_obladnannia')
def obladnannia():
    return render_template('blog/vybir_obladnannia.html')

@app.route('/robota_z_osvitlennyam')
def osvitlennia():
    return render_template('blog/robota_z_osvitlennyam.html')

if __name__ == '__main__':
    app.run(debug=True)
