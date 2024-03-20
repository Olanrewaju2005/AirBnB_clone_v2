#!/usr/bin/python3

from sqlalchemy import create_engine


class DBStorage:
    """

    """
    __engine = None
    __session = None

    def __init__(self) -> None:

        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        db_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(username, password, host, db_name)

        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(db_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") = test:
            Base.metadata.drop_all(self.__engine)
