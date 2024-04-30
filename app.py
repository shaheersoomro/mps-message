from flask import Flask, render_template, url_for, make_response, jsonify, request
import datetime

app = Flask(__name__)

data = [
    {
        "name": "Rehman Jawed",
        "email": "rehman.jawed1@gmail.com   ",
        "subject": "Hello",
        "message": "Hello my name is Shaheer"
    },
      {
        "name": "Sarmad",
        "email": "sarmad@gmail.com   ",
        "subject": "Hello World",
        "message": "Hello my name is Sarmad"
    },
]


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/blogs')
def blogs():
    return render_template('blog.html')
@app.route('/blog-12894')
def blog1():
    return render_template('blog1.html')
@app.route('/blog-12994')
def blog2():
    return render_template('blog2.html')
@app.route('/messages')
def messages():
    return render_template('messages.html')

@app.route('/sitemap.xml')
def sitemap():
    """Generate sitemap.xml. Makes a list of urls and date modified."""
    pages = []
    ten_days_ago = datetime.datetime.now() - datetime.timedelta(days=10)
    ten_days_ago = ten_days_ago.date().isoformat()

    # static routes
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments) == 0:
            pages.append(
                [url_for(rule.endpoint, _external=True), ten_days_ago]
            )

    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"    

    return response

@app.route('/data', methods=['GET', 'POST'])
def manage_data():
    global data
    if request.method == 'POST':
        # Update data based on form submission
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        new_item = {
            "name": name,  # You may want to update this dynamically
            "email": email,
            "subject": subject,
            "message": message
        }
        data.append(new_item)
        return jsonify({"message": "Data added successfully."})
    else:
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
