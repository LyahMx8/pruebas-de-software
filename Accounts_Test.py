import unittest

from parcial2 import AccountManager 

class TestAccountManager(unittest.TestCase):

	def setUp(self):
		self.accManager = AccountManager()
		
		# Primer usuario con datos normales
		self.user1 = {'username': 'LyahMotta','password': '12345ABcYo.'}
		# Usuario con datos repetidos
		self.user2 = {'username': 'LyahMotta','password': '12345ABcYo.'}
		#Usuario con password de menos de 8 caracteres
		self.user3 = {'username': 'JoseCuervo','password': 'er23.@'}
		#Usuario con password completo
		self.user4 = {'username': 'Miguelon','password': 'PassKeySecret#H4CK3r'}


	#Verifica que un usuario puede ser registrado correctamente.
	def test_register_user_successfully():

	#Verifica que al intentar registrar un username que ya existe, se lance un ValueError.
	def test_register_duplicate_user_raises_error():

	# Verifica que al registrar un usuario con una contraseña de menos de 8 caracteres, se lance un ValueError.
	def test_register_user_with_short_password_raises_error():

	#Verifica que un usuario registrado con la contraseña correcta pueda iniciar sesión (login devuelve True).
	def test_login_successful():

	#Verifica que un login con la contraseña incorrecta falle (login devuelve False).
	def test_login_with_wrong_password():

	#Verifica que un usuario pueda cambiar su contraseña si proporciona las credenciales correctas.
	def test_change_password_successfully():

	# (El test crucial). Demuestra el bug. Esta prueba debe verificar que el método change_password debería lanzar un ValueError si se intenta establecer una nueva contraseña con menos de 8 caracteres.
	def test_bug_change_password_to_weak_password(self):
		self.accManager.register(self.user4['username'], self.user4['password'])
		self.accManager.login(self.user4['username'], self.user4['password'])
		with self.assertRaises(ValueError):
			self.accManager.change_password(self.user4['username'], self.user4['password'], '123Char')

if __name__ == '__main__':
    unittest.main()