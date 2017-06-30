#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.login import *
from handlers.accesos.usuario import *
from handlers.accesos.session import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, world')

routes = [
	(r'/', MainHandler),
	# login
	(r'/login', AccesosLoginIndexHandler),
	(r'/login/acceder', AccesosLoginAccederHandler),
	# usuario
	(r'/usuario/validar_correo_repetido', AccesosUsuarioValidarCorreoRepetidoHandler),
	(r'/usuario/validar_usuario_repetido', AccesosUsuarioValidarUsuarioRepetidoHandler),
	(r'/session/logueado', AccesosSessionLogueadoHandler),
]