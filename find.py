import os
from cshop import create_app # type: ignore

app = create_app()
db_path = os.path.join(app.instance_path, 'new_db.sqlite')
print("Database Path:", db_path)
