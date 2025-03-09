from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    message = f'Hello, {name}!'
    return render_template('greet.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# check jenkins commit pipeline