from app import app
from flask import Flask, request
from flask.templating import render_template
from test.test_iterlen import TestListReversed

@app.route('/')
@app.route('/index')
def pageWeb():
    return render_template('pageWeb.html')

@app.route('/resultPage', methods=['POST'])
def resultPage():
    import Main
    productN = request.form.get('productName','None')
    #listR = Main.getPrice(Main.openFile("./app/templates/sourceCode.html"))
    #listRM = Main.getPriceM(Main.openFile("./app/templates/sourceCodeM.html"))
    #listRN = Main.getPriceN(Main.openFile("./app/templates/sourceCodeN.html"))
    listR = Main.getPrice(Main.getWebPage(productN))
    listRM = Main.getPriceM(Main.getWebPageM(productN))
    listRN = Main.getPriceN(Main.getWebPageN(productN))
    return render_template('resultPage.html', THISproductN=productN, i=len(listR), listR = listR, j=len(listRM), listRM = listRM, k=len(listRN), listRN = listRN)
