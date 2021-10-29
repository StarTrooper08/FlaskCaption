from flask import Flask, render_template , request , redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    transcript = ''
    if request.method == "POST":
         print("FORM DATA RECEIVED") 

         if "file" not in request.files:
              return redirect(request.url) #check whether wav file is added or not
        
         file = request.files["file"]
         if file.filename == "":
             return redirect(request.url)  #checking whether proper file is added
        
         if file:
             recognizer = sr.Recognizer()  #calling recognizer method
             wavfile = sr.AudioFile(file)
             with wavfile as source:
                 data = recognizer.record(source)
             transcript = recognizer.recognize_google(data, key=None) #processing wavfile here
             
# render data 
    return render_template('index.html' , transcript = transcript)

if __name__ == " main ":
    app.run(debug=True, threaded=True)
