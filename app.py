from flask import Flask, redirect,render_template,url_for,abort,request

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    search_query = request.url
    # search_query = request.path
    return render_template('404.html', search_query=search_query), 404

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/get_started')
def get_started():
    return render_template('get_started.html')

# @app.errorhandler(404)
# def page_not_found(e):
#     return "404 Page Not Found", 404


# @app.route('/web')
# def redirect_to_website():
#     target_website = "https://www.google.com"  # Replace with your desired website
#     return redirect(target_website)

if __name__ == '__main__':
    app.run(debug=True)
