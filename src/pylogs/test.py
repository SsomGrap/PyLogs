import __init__ as pylogs

logger = pylogs.Logger("Test", r"C:\Users\sacha\Documents\Developpement\Projets\PyLogs\src\pylogs")

logger.colorization(True)
logger.terminalOutput(True)
logger.fileOutput(True)

logger.info("hello")
