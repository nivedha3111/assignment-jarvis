from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint
import pdfkit as pdf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/add', methods=['POST'])
def result():
    
    url  = str(request.form.get('value1'))
    pdf.from_url(url, 'finally2.pdf')
    
    # You can validate the car brands. If someone is telling the wrong brand name, reply them with the wrong answer
    

    
    result = {
        'value1' : url,
        
    }
    
    
    #return content
    return render_template('index1.html', result=result)


    
if __name__ == "__main__":
    app.run(debug=True)
