import json
import time

from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/api/comments', methods=['GET', 'POST'])
def comments_handler():
    with open('comments.json', 'r') as file:
        comments = json.loads(file.read())

    if request.method == 'POST':
        new_comment = request.form.to_dict()
        new_comment['id'] = int(time.time() * 1000)
        comments.append(new_comment)

        with open('comments.json', 'w') as file:
            file.write(json.dumps(comments, indent=4, separators=(',', ': ')))

    return Response(json.dumps(comments), mimetype='application/json', headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
