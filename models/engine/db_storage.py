#!/usr/bin/python3
"""
Important modules and objects are imported from
respective modules
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy.exc import InvalidRequestError
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage:
    """

    """
    __engine = None
    __session = None

    def __init__(self) -> None:
        """
        iniitializatin of attributes and definition of db connection
        """
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        db_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(username, password, host, db_name)

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session) all objects
        depending of the class name (argument cls)

        if cls=None, query all types of objects

	Returns a dictionary
        """
        obj_list = []

        if cls:
            if isinstance(cls, str):
                try:
                    globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                obj_list = self.__session.query(cls).all()
            else:
                for subclass in Base.__subclasses__():
                    obj_list.extend(self.__session.query(subclass).all())
            obj_dict = {}
            for obj in obj_list:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj
            return obj_dict

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database

        create the current database session from the engine by using a sessionmaker
        """
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self)
        """ Calls remove() """
        self.__session.close()
