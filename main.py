from flask import Flask, render_template
import random
app = Flask(__name__)
gercekler = ["Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir." , "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor." , "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."
]
@app.route("/")
def hello_world():
    return f'<h1>{random.choice(gercekler)}</h1>'
@app.route("/ana")
def ana():
    return render_template("index.html")
@app.route("/insan")
def das():
    return '''<h1>Ne güzel bir gün ya!</h1>
<h2>b-bir dakika SENDE KIMSIN</h2>
<h2> her neyse hiç bir şeye zarar verme sana işine yarayacak bir araç vercem</h2>
<h2> buraya her nasıl geldiysen geldiğin yere "au" yaz (şifre vercek sana)'''
@app.route("/au")
def au():
    karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:,.<>/?|~`"

    sifre = ''.join(random.choice(karakterler) for _ in range(17))
    return f"<h1> {sifre}</h1>"

app.run(debug=True)


