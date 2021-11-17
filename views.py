from flask import Blueprint, render_template, request


views = Blueprint('views',__name__)


@views.route('/',methods=['GET','POST'])
def home():
    data = request.form
    print(data)
    return render_template("home.html", boolean = True)

@views.route('/admin',methods=['GET','POST'])
def admin():
    if request.method =='POST':
        print(request.form.getlist('campos'))
        print(request.form.get('ano'))
    return render_template("admin.html", boolean = True)



