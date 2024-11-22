from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1',methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':

        nuevoValorTarro = None

        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        valorTarro = tarros * 9000

        if edad >= 18 and edad <= 30:
            nuevoValorTarro = valorTarro - ( 0.15 * valorTarro )


        elif edad > 30:
            nuevoValorTarro = valorTarro - ( 0.25 * valorTarro )

        else:
            nuevoValorTarro = valorTarro

        descuento = valorTarro - nuevoValorTarro

        return render_template('ejercicio1.html', nombre=nombre, valorTarro=valorTarro, nuevoValorTarro= nuevoValorTarro, descuento=descuento )
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        verificar = None

        nombre = str(request.form['nombre'])
        contrasenha = str(request.form['contrasenha'])

        if nombre == "juan" and contrasenha == "admin":
            verificar = f"Bienvenido administrador {nombre}"

        elif nombre == "pepe" and contrasenha == "user":
            verificar = f"Bienvenido usuario {nombre}"

        else:
            verificar = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', nombre=nombre, verificar=verificar)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)