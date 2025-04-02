from flask import Flask, request

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def upload_file():
    print('INIT upload_file')
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']

    print('REQUEST ', request)
    print('request.files ', request.files)
    print('file', file)

    if file.filename == '':
        return "No selected file", 400
    if file:
        content = file.read().decode('utf-8')
        return content, 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
