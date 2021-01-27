import socket
from flask import Flask, request, render_template, send_file
from time import strftime, gmtime
from flask import Response

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
app.config.from_object(__name__)
#globale Varibale
ESP_temperatur = "0"


def get_the_time():
    dt_gmt = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    return dt_gmt


def who_am_i():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()

    return ip




@app.route("/static/img/food1.png", methods=['GET'])
def food1():
    if request.method == 'GET':
        return send_file("static/img/food1.png", mimetype='image/gif')


@app.route("/static/img/food2.png", methods=['GET'])
def food2():
    if request.method == 'GET':
        return send_file("static/img/food2.png", mimetype='image/gif')


@app.route("/static/img/food3.png", methods=['GET'])
def food3():
    if request.method == 'GET':
        return send_file("static/img/food3.png", mimetype='image/gif')


@app.route("/static/img/food4.png", methods=['GET'])
def food4():
    if request.method == 'GET':
        return send_file("static/img/food4.png", mimetype='image/gif')


@app.route("/login", methods=['POST', 'GET'])  # mit Parameter
def login():
    name = ""
    if request.method == 'POST':
        name = str(request.args.get('name'))
        # name = request.form['name']
        print(name)
    else:
        name = request.args.get('name')
        print(name)
        try:
            fobj_write = open("Kunden/Kunde_1/Teller/Temperaturen.txt", "a")
            fobj_write.write("\n")
            fobj_write.write(str(name) + "             ," + str(get_the_time()))
            fobj_write.close()
            global ESP_temperatur
            ESP_temperatur = name
        except FileNotFoundError:
            print("The file doesn't exist")

    return "Server sagt Danke " + name + "!"


@app.route("/essen", methods=['POST', 'GET'])
def essen():
    temperature = ""
    if request.method == 'POST':
        temperature = request.form('temperature')
    else:
        temperature = request.args.get('temperature')
        print(temperature)

    return "Temperature in C° = (" + temperature + ")"

@app.route("/gett", methods = ['POST', 'GET'])
def gett():
    return ESP_temperatur.split(".")[0]

@app.route("/getbl", methods=['POST', 'GET'])
def getbl():
    return 'true'

@app.route("/")
def index():
    los = False
    if (float(ESP_temperatur) > 0):
        los = 'true'
    else:
        los = 'false'
    return render_template('index.html', temperatur = ESP_temperatur, los = los ) #hier könnte man mit einem , eine Varible einfügen





if __name__ == '__main__':
    host_IP_Adresse = str(who_am_i())
    print(host_IP_Adresse)
    app.run(host=host_IP_Adresse, port=1337, debug=True)
    print(type(ESP_temperatur))