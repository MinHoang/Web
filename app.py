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

g = [
{
'name' : 'Atari',
'image' : "https://dvsgaming.org/wp-content/uploads/2017/06/do-atari-atari-na-mdia-downloads-poltica-de-privacidade-contato.jpg",
'description' : 'Là công ty làm máy chơi game và xuất bản game lớn nhất trong những năm 80 và cũng là công ty quan trọng nhất trong lịch sử game, Atari là ông anh lớn của game trong cuối thập kỷ 70 đến thập kỷ 80.'
},
{
'name' : "Nintendo" ,
'image' : "https://www.nintendo.com/images/social/fb-400x400.jpg",
'description' : "Nintendo được thành lập vào năm 1889 nhưng đến năm 1985 mới tham gia vào ngành máy chơi game khi tạo ra máy NES lừng danh, Ninendo luôn sáng tạo thậm chí đến ngày nay. "
},
{
'name' : "Sega" ,
'image' : "https://pbs.twimg.com/profile_images/834363762912219136/shGE2Cho.jpg",
'description' : "Thành lập năm 1960, Sega bắt đầu làm máy arcade đến năm 1983 khi ra máy SG-1000, nhập vào ngành máy chơi game nhưng đến năm 1988 ra máy Sega Genesis để tranh giành với SNES của Nintendo."
}

]
#Configure
@app.route("/")
def index():
    return render_template("index.html", girl_type = g)

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
