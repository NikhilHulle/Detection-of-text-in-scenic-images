from flask import Flask, render_template, request, redirect

from werkzeug.utils import secure_filename

from fuzzywuzzy import fuzz

from fuzzywuzzy import process

from c9 import OCR

from lib.trial import cool

from lib.utils import get_med_name

import cv2

import os 


app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = 'D:/images/'

@app.route('/')
def home_page():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      print(f.filename)
      pre_img = cv2.imread(f.filename)
      #img = cv2.resize(pre_img, (800, 600))
      cv2.imwrite("resized.jpeg",pre_img)
      ocr=OCR()
      query_string = ocr.start_OCR("resized.jpeg")
      print(query_string)
      req_med = get_med_name(query_string)
      return redirect('https://www.1mg.com/search/all?name='+ req_med)
        
if __name__=='__main__':
    app.run()#(host='0.0.0.0')#, port=5000)
    

