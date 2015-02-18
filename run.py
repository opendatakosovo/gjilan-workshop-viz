from flask import Flask
from flask import render_template, Response
import json
from urllib2 import urlopen

app = Flask(__name__)


@app.route('/')
def home():
    return 'Shiko kodin dhe ndjek instruksionet'


@app.route('/harta')
def harta():
    return render_template('map.html')


@app.route('/hartadata')
def merr_json():
    url = "http://0.0.0.0:5050/harta"

    result = urlopen(url).read()

    # Build response object.
    resp = Response(
        response=result, mimetype='application/json')

    # Return response.
    return resp


@app.route('/piechart')
def piechart():
    url = "http://0.0.0.0:5050/pie"
    read_url = urlopen(url).read()
    json_result = json.loads(read_url)
    return render_template('piechart.html', result=json_result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
