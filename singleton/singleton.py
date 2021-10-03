import time

instance = None


class Singleton:
    def __init__(self):
        print("Initializing a new instance....")
        time.sleep(3)
        print("Done.")


def get_instance() -> Singleton:
    """Returns a singleton instance of the Singleton class. If no instance exists, we create one.

    Returns:
        Singleton: singleton class instance
    """
    global instance
    if not instance:
        instance = Singleton()
    return instance
