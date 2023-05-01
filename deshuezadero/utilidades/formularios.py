from home.models import *
from django.utils.html import format_html
from utilidades import dreamhost


#####formulario
def get_categorias_choices():
	return [
	(value.pk, value.nombre) for value in Categoria.objects.all()
	]

#####admin
def set_user(obj):
	return f"{obj.user.first_name} {obj.user.last_name}"
set_user.short_description="Usuario"


def set_categoria_con_link(obj):
	return format_html(f"""<a href="/core/backend/home/categoria/{obj.categoria_id}/change/" target="_blank">{obj.categoria}</a>""")
set_categoria_con_link.short_description="Categoría"


def foto_producto(obj):
	if dreamhost.existeArchivo('producto', obj.foto)==False:
		dreamhost.moverArchivoProducto(obj.foto, obj.id)
	return format_html(f""" <a href="/assets/upload/producto/{obj.foto}" target="_blank">
		<img src="/assets/upload/producto/{obj.foto}" width="100" height="100" />
		</a> """)
foto_producto.short_description="Foto"