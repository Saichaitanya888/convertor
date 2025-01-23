from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        conversion_type = request.form['conversion_type']
        
        if conversion_type == 'cm_to_in':
            result = value * 0.393701
        elif conversion_type == 'in_to_cm':
            result = value / 0.393701
        elif conversion_type == 'kg_to_lb':
            result = value * 2.20462
        elif conversion_type == 'lb_to_kg':
            result = value / 2.20462
        elif conversion_type == 'c_to_f':
            result = (value * 9/5) + 32
        elif conversion_type == 'f_to_c':
            result = (value - 32) * 5/9
        
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
