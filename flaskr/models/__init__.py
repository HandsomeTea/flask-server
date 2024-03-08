# mongodb的所有数据库表model
from flaskr.models.mongodb.user import Users  # noqa: F401

# # mysql的所有数据库表model
# from flaskr.models.mysql.base import Migrate
# from flaskr.db.mysql import sql_engine
# from flaskr.models.mysql.user import Users  # noqa: F401

# # mysql初始化数据库表(创建表)
# Migrate.metadata.create_all(sql_engine)
