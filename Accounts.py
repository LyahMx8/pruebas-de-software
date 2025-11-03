# AccountManager.py

class AccountManager:
    def __init__(self):
        """Inicializa un gestor de cuentas sin usuarios."""
        self._users = {}

    def register(self, username: str, password: str):
        """Registra un nuevo usuario."""
        if username in self._users:
            raise ValueError("El nombre de usuario ya existe.")
        if len(password) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")
        
        self._users[username] = password
        return True

    def login(self, username: str, password: str) -> bool:
        """Autentica a un usuario."""
        stored_password = self._users.get(username)
        return stored_password == password

    def change_password(self, username: str, old_password: str, new_password: str) -> bool:
        """Cambia la contraseña de un usuario."""
        if not self.login(username, old_password):
            return False
        
        self._users[username] = new_password
        return True