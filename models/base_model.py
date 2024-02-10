#!/usr/bin/python3
"""defines the base class
It is the parent class"""

import uuid
from datetime import datetime

class BaseModel:
    """Represents the Base model of whole AirBnB project"""

    def __init__(self):
        """Initialises the basic attributes of the class"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """provides the string representation"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Saves the status in a file
        it helps in future retrieval"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """It returns dictionary representation"""

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
