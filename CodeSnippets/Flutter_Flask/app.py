from flask import Flask, render_template,url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask.json import jsonify
from pandas_datareader import data, wb
import pandas_datareader.data as web
import pandas as pd

start = datetime(2006,1,6)
end = datetime(2016,1,6)

BAC = web.DataReader("BAC", "yahoo", start,end)

stock = pd.DataFrame(BAC)

stock.columns.names = ["BAC"]

print(stock.iloc[0,0])

app = Flask(__name__)

@app.route("/data")
def datafetch():
    return jsonify({"BAC" : str(round(stock.iloc[0,0],2))})


if __name__ == "__main__":
    app.run(debug = True)


