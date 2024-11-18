from flask import Flask, request
import requests

app = Flask(__name__)

# IP adreslerini içeren JSON verisi
data = {
    "data": [
        {"ipv4": "77.92.138.121"}, {"ipv4": "212.102.38.46"}, {"ipv4": "212.102.38.47"},
        {"ipv4": "77.92.138.126"}, {"ipv4": "77.92.138.120"}, {"ipv4": "89.187.169.43"},
        {"ipv4": "77.92.138.197"}, {"ipv4": "185.107.83.119"}, {"ipv4": "77.92.138.119"}
    ]
}

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    if request.method == "POST":
        url = request.form.get("url")
        for item in data["data"]:
            ip = item["ipv4"]
            try:
                response = requests.get(url, timeout=5)
                results.append({"ip": ip, "status_code": response.status_code})
            except requests.RequestException as e:
                results.append({"ip": ip, "status_code": "Error", "error": str(e)})

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                margin: 0;
                padding: 0;
            }}
            .container {{
                width: 80%;
                margin: auto;
                overflow: hidden;
                padding: 20px;
            }}
            h1, h2 {{
                color: #444;
            }}
            form {{
                margin-bottom: 20px;
            }}
            input[type="text"] {{
                width: 70%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }}
            button {{
                background-color: #5cb85c;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            table, th, td {{
                border: 1px solid #ddd;
            }}
            th, td {{
                padding: 8px;
                text-align: left;
            }}
        </style>
        <title>IP Test Aracı</title>
    </head>
    <body>
        <div class="container">
            <h1>IP Test Aracı</h1>
            <form method="POST">
                <label for="url">Test Edilecek URL:</label>
                <input type="text" id="url" name="url" placeholder="https://example.com" required>
                <button type="submit">Test Et</button>
            </form>
            {"<h2>Sonuçlar</h2><table><tr><th>IP Address</th><th>Status Code</th></tr>" + "".join(f"<tr><td>{result['ip']}</td><td>{result['status_code']}</td></tr>" for result in results) + "</table>" if results else ""}
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
