import DataBaseServices

def create_user(nombre, usuario, contrasena):
    db_service = DataBaseServices.DataBaseServices()
    query = "INSERT INTO users (nombre, usuario, contrasena) VALUES (?, ?, ?)"
    params = (nombre, usuario, contrasena)
    db_service.execute_query(query, params)

def get_user_by_id(user_id):
    db_service = DataBaseServices.DataBaseServices()
    query = "SELECT * FROM users WHERE id = ?"
    params = (user_id,)
    return db_service.fetch_one(query, params)

def get_all_users():
    db_service = DataBaseServices.DataBaseServices()
    query = "SELECT * FROM users"
    return db_service.fetch_query(query)

def update_user(user_id, nombre=None, usuario=None, contrasena=None):
    db_service = DataBaseServices.DataBaseServices()
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
    db_service = DataBaseServices.DataBaseServices()
    query = "DELETE FROM users WHERE id = ?"
    params = (user_id,)
    db_service.execute_query(query, params)


