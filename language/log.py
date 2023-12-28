import logging

def helloWorld(name):
    logging.basicConfig(level=logging.DEBUG, filename="language/log.log", filemode="w")

    logging.debug("I am in hello world function.")
    logging.info("Hello world greeting for user " + name)
    logging.warning("hmm, something is not correct.")
    logging.error("Somthing is failing.")
    logging.critical("Somthing is broken.")
    return "Hello " + name

if __name__ == "__main__":
    helloWorld("Tan")