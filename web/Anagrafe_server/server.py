from flask import Flask, render_template, request, json
import base64

cittadini = [["Leonardo", "Rossi", "12/08/2000", "dsrfed12e28h501r"],["Francesco", "Russo", "09/11/2001", "abcdef12th501m"],["Alfred", "Wilson", "23/08/2024", "bgfmjh90e26h501i"]]

api = Flask("__name__")

@api.route('/post_create', methods=['POST'])
def process_json():
    print("Ricevuta chiamata")
    auth = request.headers.get('Authorization')
    auth = auth[6:]
    security_data = base64.b64decode(auth)
    print(security_data)
    content_type = request.headers.get('Content-Type')
    print("Ricevuta Chiamata " + content_type)
    if (content_type == "application/json"):
        json1 = request.json
        print(json1)
        cittadini.append(json1)
        response = {"esito":"ok","Msg":"Dato inserito"}
        return json.dumps(response)
    else:
        return 'content_type not supported!'

@api.route('/post_delete', methods=['DELETE'])
def process_json():
    print("Ricevuta chiamata")
    content_type = request.headers.get('Content-Type')
    print("Ricevuta Chiamata " + content_type)
    if (content_type == "application/json"):
        json1 = request.json
        print(json1)
        cittadini.append(json1)
        response = {"esito":"ok","Msg":"Dato inserito"}
        return json.dumps(response)
    else:
        return 'content_type not supported!'

api.run(host="0.0.0.0", port=8085)