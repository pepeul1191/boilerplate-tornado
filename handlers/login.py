#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import requests
import datetime
from config.helper import *
from config.services import *

class LoginIndexHandler(tornado.web.RequestHandler):
	def prepare(self):
		#self.set_header('Server", "Python")
		if 2 == 3:
			self.redirect('/')

	def get(self):
		self.set_status(400)
		self.write("<h1>LOGIN</h1>")

	def post(self):
		services = Services()
		helper = Helper()
		
		usuario = self.get_argument('usuario')
		contrasenia =  requests.post(services.get('cipher') + 'encode?key=' + helper.get('cipher_key') + '&texto=' + str(self.get_argument('contrasenia'))).text
		
		url = services.get('accesos') + 'usuario/validar?usuario=' + str(usuario) + '&contrasenia=' + str(contrasenia)
		response = requests.post(url)
		
		if str(response.text) == '1':
			self.set_secure_cookie('usuario', usuario)
			self.set_secure_cookie('tiempo', str(datetime.datetime.now()))
			self.redirect('/')
			return
		else:
			self.redirect('/login/error')
			return