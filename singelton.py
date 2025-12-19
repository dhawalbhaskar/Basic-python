class singelton:
    _instance = None
    def __init__(self ):
        raise RuntimeError("This class is a singleton!")


    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

 
