from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        num = request.form.get("number")
        if not num.isdecimal() or (not 0 < int(num) < 4000):
            return render_template("index.html", not_valid=True, developer_name="codebenders")
        else:
            num = int(num)
            num1 = num
            mappings = {1000: "M", 900: 'CM', 500: "D", 400: 'CD', 100: "C",
                        90: 'XC', 50: "L", 40: 'XL', 10: "X", 9: 'IX', 5: "V", 4: 'IV', 1: "I"}
            res = ""
            for k, v in mappings.items():  # k =1000
                value = num // k  # 1
                res += v * value  # M *1
                num %= k  # 994        return render_template("result.html", number_decimal=num1, developer_name="codebenders", number_roman=res)
    else:
        return render_template("index.html", not_valid=False, developer_name="codebenders")
if __name__ == "__main__":
    #app.run("localhost", port=5000, debug=True)
    #app.run(debug=True, port=8000)
    app.run('0.0.0.0', port=80)