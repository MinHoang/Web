from flask import *
import mlab
from mongoengine import *
mlab.connect()

class GirlType(Document): #COLLECTION
    name = StringField()
    image = StringField()
    description = StringField()

# girl_type = GirlType(name = "Gái Tiểu Thư",
#                     image ="https://scontent.fhan4-1.fna.fbcdn.net/v/t1.0-9/21032766_687949738069098_2695562382087912876_n.jpg?oh=c4272a4774fbdc01f0baca18b488060f&oe=5A4E0DA7",
#                     description = "DESCRIPT: Hơi chảnh, Ít nói,Khó tiếp cận, Thích sạch sẽ, Thích Trai nhà giàu và nhiều tiền, hay mặc quần áo kín, gọn, đắt tiền")
# #girl_type.save()
# 1. connect to mlab
# 2.Add data
# 3.Get data for render_template

#create server
app = Flask(__name__)

#Configure
@app.route("/")
def index():
    return render_template("index.html", girl_type = GirlType.objects())

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/school")
def schoolwebsite():
    return redirect ("http://techkids.vn/")
@app.route("/bmi")
def bmi():
    args = request.args
    weight = int(args["weight"])
    height = int(args["height"]) / 100
    bmi  = weight / (height **2)
    return "Your bmi is " + str(bmi)

@app.route('/bmi-calc')
def bmi_calc():
    return render_template("bmi_calc.html")
@app.route('/tutorial')
def tutorial():
    return render_template("tutorial.html")
#apprun
if __name__ == "__main__":
	app.run(debug=True)
