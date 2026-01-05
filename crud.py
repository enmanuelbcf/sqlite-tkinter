from DataBaseServices import DataBaseServices

db_service = DataBaseServices()
print("Creating users table if not exists...")


def create_user(nombre, usuario, contrasena):
    query = "INSERT INTO users (nombre, usuario, contrasena) VALUES (?, ?, ?)"
    params = (nombre, usuario, contrasena)
    db_service.execute_query(query, params)

def get_user_by_id(user_id):
    query = "SELECT * FROM users WHERE id = ?"
    params = (user_id,)
    return db_service.fetch_one(query, params)

def get_all_users():
    query = "SELECT * FROM users"
    return db_service.fetch_query(query)

def update_user(user_id, nombre=None, usuario=None, contrasena=None):
    fields = []
    params = []
    if nombre:
        fields.append("nombre = ?")
        params.append(nombre)
    if usuario:
        fields.append("usuario = ?")
        params.append(usuario)
    if contrasena:
        fields.append("contrasena = ?")
        params.append(contrasena)
    params.append(user_id)
    query = f"UPDATE users SET {', '.join(fields)} WHERE id = ?"
    db_service.execute_query(query, tuple(params))

def delete_user(user_id):
    query = "DELETE FROM users WHERE id = ?"
    params = (user_id,)
    db_service.execute_query(query, params)

def login(usuario, contrasena):
    try:
        query = "SELECT * FROM users WHERE usuario = ? AND contrasena = ?"
        params = (usuario, contrasena)
        user = db_service.fetch_one(query, params)
        return True
    except Exception as e:
        print(f"Login error: {e}")
        return False