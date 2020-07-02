from flask import Flask, render_template, requestapp = Flask(__name__)def convert(num):
    num = int(num)    mappings = {1000: "M", 900: 'CM', 500: "D", 400: 'CD', 100: "C",
                90: 'XC', 50: "L", 40: 'XL', 10: "X", 9: 'IX', 5: "V", 4: 'IV', 1: "I"}    result = ""    for k,v in mappings.items() : # k =1000
        value = num // k # 1
        result += v * value # M *1
        num%=k # 994    return result@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", not_valid=False, developer_name="codebenders")@app.route("/", methods=["POST"])
def result():
    decimal = request.form.get("number")
    if not decimal.isdecimal() or (not 0< int(decimal)<4000):
        return render_template("index.html", not_valid = True, developer_name = "codebenders")
    else:
        return render_template("result.html", number_decimal= decimal, developer_name= "codebenders", number_roman= convert(decimal))if __name__ == "__main__":
    #app.run("localhost", port=5000, debug=True)
    app.run(debug=True)