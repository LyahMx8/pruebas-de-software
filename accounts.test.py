import unittest

from accounts import AccountManager 

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
	def test_register__login_user_successfully():
		register = self.accManager.register(self.user1['username'], self.user1['password'])
		
		self.assertTrue(register, "El registro ha sido exitoso.")

		# Subtest inicio de sesión con el nuevo registro
		self.assertTrue(self.accManager.login(self.user1['username'], self.user1['password']),
					"Sesión iniciada correctamente.")


	#Verifica que al intentar registrar un username que ya existe, se lance un ValueError.
	def test_register_duplicate_user_raises_error():
		self.accManager.register(self.user1['username'], self.user1['password'])

		with self.assertRaises(ValueError):
      self.accManager.register(self.user2['username'], self.user2['password'])


	# Verifica que al registrar un usuario con una contraseña de menos de 8 caracteres, se lance un ValueError.
	def test_register_user_with_short_password_raises_error():
		with self.assertRaises(ValueError):
			self.accManager.register(self.user3['username'], self.user3['password'])


	#Verifica que un usuario registrado con la contraseña correcta pueda iniciar sesión (login devuelve True).
	def test_login_successful():
		self.accManager.register(self.user1['username'], self.user1['password'])
		
		self.assertTrue(self.accManager.login(self.user1['username'], self.user1['password']),
					"Sesión iniciada correctamente.")


	#Verifica que un login con la contraseña incorrecta falle (login devuelve False).
	def test_login_with_wrong_password():
		self.accManager.register(self.user1['username'], self.user1['password'])

		self.assertFalse(self.accManager.login(self.user1['username'], self.user4['password']),
					"El login no ha sido exitoso.")
		# Subtest Verifica que el login falle para un usuario inexistente
		self.assertFalse(self.accManager.login(self.user3['username'], self.user3['password']),
					"El usuario no ha sido registrado.")
	
	
	#Verifica que un usuario pueda cambiar su contraseña si proporciona las credenciales correctas.
	def test_change_password_successfully():
		self.accManager.register(self.user4['username'], self.user4['password'])
        
		new_password = 'P4$$2025²55'
		result = self.accManager.change_password(self.user4['username'], self.user4['password'], new_password)
		
		self.assertTrue(result, "El cambio de contraseña ha sido exitoso.")

		# Subtest Verifica que la contraseña antigua ya no funcione
		self.assertFalse(self.accManager.login(self.user4['username'], self.user4['password']),
					"El login no ha sido exitoso.")

		# Subtest Verifica que la nueva contraseña funcione
		self.assertTrue(self.accManager.login(self.user4['username'], new_password),
					"Sesión iniciada correctamente.")


	# (El test crucial). Demuestra el bug. Esta prueba debe verificar que el método change_password debería lanzar un ValueError si se intenta establecer una nueva contraseña con menos de 8 caracteres.
	def test_bug_change_password_to_weak_password(self):
		self.accManager.register(self.user4['username'], self.user4['password'])
		self.accManager.login(self.user4['username'], self.user4['password'])
		with self.assertRaises(ValueError):
			self.accManager.change_password(self.user4['username'], self.user4['password'], '123Char')

if __name__ == '__main__':
    unittest.main()