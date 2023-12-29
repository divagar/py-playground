import logging

logLevel = logging.DEBUG
logFilename = "language/log.log"
logFileMode = "w"
logFormat = "%(asctime)s | %(levelname)s | %(funcName)s: Line#%(lineno)d | %(message)s"
logDateFormat = "%Y-%m-%d %I:%M:%S %p"

logging.basicConfig(level=logLevel, filename=logFilename, filemode=logFileMode, format=logFormat, datefmt=logDateFormat)

def helloWorld(name):

    logging.debug("I am in hello world function.")
    logging.info("Hello world greeting for user " + name)
    logging.warning("hmm, something is not correct.")
    logging.error("Somthing is failing.")
    logging.critical("Somthing is broken.")
    return "Hello " + name

if __name__ == "__main__":
    helloWorld("Tan")