from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)


@app.route("/kayit")
def kayit():
    return render_template("kayit.html")
@app.route("/verileriAl",methods=['POST','GET'])
def verileriAl():
    if request.method=="POST":
        urAd=request.form.get("urAd")
        urNum=request.form.get("urNum")
        tasUcr=request.form.get("tasUcr")
        varNok=request.form.get("varNok")
        arac=request.form.get("arac")
        dogumTarih=request.form.get("dogumTarih")
        baglanti=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='programlama')
        isaretci=baglanti.cursor()
        isaretci.execute("INSERT INTO ozankorkmaz(urAd,urNum,tasUcr,varNok,arac,tarih) VALUES ('%s','%s','%s','%s','%s','%s')"%(urAd,urNum,tasUcr,varNok,arac,dogumTarih))
        baglanti.commit()
        baglanti.close()
        return render_template("kayit.html",urAd=urAd,urNum=urNum,tasUcr=tasUcr,varNok=varNok,arac=arac,dogumTarih=dogumTarih)
    
    else:
        return "Kayıt Başarısız"
if __name__=="__main__":
    app.run()
