Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@fh3idgg3r 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


antoniodiasabc
/
defciberac3
1
02
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
defciberac3/app.py /
@antoniodiasabc
antoniodiasabc ac4
Latest commit b3f82d1 15 days ago
 History
 1 contributor
36 lines (27 sloc)  683 Bytes
  
import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    limite = 100

    c = 1
    p = 1
    numero = 3

    primos = "2,"

    while p < limite:
        ehprimo = 1
        for i in range(2, numero):
            if numero % i == 0:
                ehprimo = 0
                break
        if (ehprimo):
            primos = primos + str(numero) + ","
            p += 1
            if(p % 10 == 0):
                primos = primos + "<br>"
        numero+=1

    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
