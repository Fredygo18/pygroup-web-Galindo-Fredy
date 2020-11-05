from flask import Blueprint, Response


prod = Blueprint('prod', __name__, url_prefix='/prod')


@prod.route('/<string:name>', methods=['GET'])
def index(name):
    if name != 'pygroup':
        return Response("<h1>Felicitaciones! Trabajo exitoso {}</h1>".format(name), status=200)

    if name == 'pygroup':
        return Response("<h2>ERROR! No se puede usar el nombre pygroup</h2>", status=400)


'''
Método Render_Template

Flask proporciona el método render_template() que permite 
el uso del motor de plantillas Jinja. Esto permite que la gestión HTML sea 
mucho más fácil escribiendo código HTML en archivos .html, además de 
utilizar la lógica del código HTML. Se Usarán estos archivos HTML, 
(plantillas), para crear todas las páginas de la aplicación, de igual 
forma que la página principal donde mostrará las entradas actuales del blog, 
la página de la entrada del blog, la página donde el usuario puede añadir una 
nueva entrada, etcétera.

Fuente: DigitalOcean

'''