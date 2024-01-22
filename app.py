from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/stock', methods=['GET'])
def get_fruits():
    url = "https://blox-fruits.fandom.com/api.php?action=query&prop=revisions&titles=Blox_Fruits_%22Stock%22&rvprop=content&format=json"

    try:
        response = requests.get(url)
        data = response.json()
        content = data['query']['pages']['17665']['revisions'][0]['*']

        start_index = content.find('{{CurrentStock')
        end_index = content.find('}}', start_index) + 2  # Include the closing braces
        selected_data = content[start_index:end_index]

        # Extracting all fruits
        lines = selected_data.split('\n')
        fruits_json = {}
        for line in lines:
            if '=' in line:
                key, value = map(str.strip, line.split('='))
                fruits_json[key] = value

        return jsonify(fruits_json)
    except KeyError:
        return jsonify({"error": "ÙØ´Ù ÙÙ Ø§Ø³ØªØ®Ø±Ø§Ø¬ Ø§ÙØ¨ÙØ§ÙØ§Øª ÙÙ Ø§ÙÙØ§Ø¬ÙØ© Ø§ÙØ¨Ø±ÙØ¬ÙØ©."}), 500
    except Exception as e:
        return jsonify({"error": f"Ø­Ø¯Ø« Ø®Ø·Ø£: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
