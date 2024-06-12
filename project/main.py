from blueprints.principal import principal
from flask import Flask, redirect, url_for, request, jsonify, render_template
from flask_login import LoginManager
from blueprints.principal.principalRepo import get_user
from blueprints.principal.principalService import User
from blueprints.curso import curso

app = Flask(__name__, static_folder="static", static_url_path="/static")
app.register_blueprint(principal)
app.secret_key = "senhaSecreta"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'principal.user_login'

@app.route("/")
def access():
    return redirect(url_for('principal.pagina_principal'))

@login_manager.user_loader
def load_user(user_id):
    user_data = get_user(user_id)
    return User(user_data["username"], user_data["permission"])

@app.route('/exclui_curso', methods=['POST'])
def exclui_curso():
    codigoCurso = request.form['codigoCurso']
    if not curso.valida_codigo_curso(codigoCurso):
        return jsonify({"error": "Código de curso inválido"}), 400
    if curso.exclui_curso(codigoCurso):
        return jsonify({"success": "Curso excluído com sucesso"})
    return jsonify({"error": "Curso não encontrado"}), 404

@app.route('/consulta_curso', methods=['GET'])
def consulta_curso():
    codigoCurso = request.args.get('codigoCurso')
    if not curso.valida_codigo_curso(codigoCurso):
        return jsonify({"error": "Código de curso inválido"}), 400
    dadosCurso = curso.consulta_curso(codigoCurso)
    if dadosCurso:
        return jsonify(dadosCurso)
    return jsonify({"error": "Curso não encontrado"}), 404

@app.route('/atualiza_curso', methods=['POST'])
def atualiza_curso():
    codigoCurso = request.form['codigoCurso']
    dadosCurso = request.form['dadosCurso']
    if not curso.valida_codigo_curso(codigoCurso):
        return jsonify({"error": "Código de curso inválido"}), 400
    if not curso.valida_dados_curso(dadosCurso):
        return jsonify({"error": "Dados do curso inválidos"}), 400
    if curso.atualiza_curso(codigoCurso, dadosCurso):
        return jsonify({"success": "Curso atualizado com sucesso"})
    return jsonify({"error": "Curso não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)

