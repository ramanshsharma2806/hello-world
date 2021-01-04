from flask import Flask, request, Response
import json, os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    if you're coming to not where you want to be, you probably don't know how to send an API request
    """
    input_json = None

    if request.get_json(silent=True):
        input_json = request.get_json(silent=True)
    
    if input_json:
        if 'help' in input_json.values():
            output_text = f"umm please inspect the code I don't have time to help you out"
        else:
            output_text = f"why are you sending this stuff to not where you want to be you noob: {input_json}\nyou need to send it to the correct endpoint"
    
    else:
        output_text = "This is not where you want to be. Um, you're not supposed to be here, please leave"
    
    output_text = "This is not where you want to be. Um, you're not supposed to be here, please leave."

    return "<h1 style='position: absolute; top: 42%; right: 10%;'>" + output_text + "</h1>"

@app.route('/hello_world', methods=['GET', 'POST'])
def helloworld():
    """
    yeah sure, you will get you hello world now
    """
    input_json = None

    if request.get_json(silent=True):
        input_json = request.get_json(silent=True)
    
    if input_json:     
        input_json = request.get_json(silent=True)
        if 'please' not in input_json.values() and 'please' not in input_json.keys():
            output_text = f"You need to ask nicely first, please include the magic word in either the key or value of the json."
        else:
            output_text = f"Hello world"
    else:
        output_text = f"Hello world"

    return Response(json.dumps({"response": output_text}), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT'))