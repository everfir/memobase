import dotenv

dotenv.load_dotenv()
from datetime import datetime
from sqlalchemy.schema import CreateTable
from memobase_server.connectors import DB_ENGINE
from memobase_server.models.database import User, GeneralBlob


print("--", f"Generated by memobase_server/build_init_sql.py on {datetime.now()}")
for db in [User, GeneralBlob]:
    print(str(CreateTable(db.__table__).compile(DB_ENGINE)).strip() + ";")
