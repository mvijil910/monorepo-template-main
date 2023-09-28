class Logger:
    _instance = None  # Private class variable to hold the single instance
    _addMessage = []
    
    def __init__(self):
        raise RuntimeError('Call get_instance() instead')
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            print("Logger created exactly once") 
            cls._instance = super(Logger, cls).__new__(cls)
        if cls._instance is not None: 
            print("logger already created")    
        return cls._instance
        

    def add_message(self, message):
        self._addMessage.append(message)
        
    def get_message(self): 
        print(self._addMessage)


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
       
    for i in range(3):
        logger = Logger.get_instance()
        logger.add_message(f"Adding message number: {i}")
        logger.get_message()
        
        
if __name__ == "__main__":
    main()
