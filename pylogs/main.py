"""
PyLogs :
A logging package for your python project

developed by SsomGrap
"""

TYPE_INFO = "info"
TYPE_WARN = "warn"
TYPE_ERROR = "warn"
TYPE_CRITICAL = "warn"

colors = {
    "white"
    "red"
    "green"
    "blue"
    "orange"
    "yellow"
}

class Logger:

    def __int__(self, name, directory):
        self.name = name
        self.directory = directory
        self.logDict = {
            "info": {"format": "","colorization" : False, "doTerminalOutput": True, "doFileOutput": True},
            "warn": {"format": "","colorization": False, "doTerminalOutput": True, "doFileOutput": True},
            "error": {"format": "", "colorization": False, "doTerminalOutput": True, "doFileOutput": True},
            "critical": {"format": "", "colorization": False, "doTerminalOutput": True, "doFileOutput": True}
        }

    def getFormat(self, logType):
        return self.logDict[logType]["format"]

    def setFormat(self, logType, logFormat):
        self.logDict[logType]["format"] = str(logFormat)

    def colorization(self, logType, boolean):
        self.logDict[logType]["colorization"] = bool(boolean)

    def terminalOutput(self, logType, boolean):
        self.logDict[logType]["doTerminalOutput"] = bool(boolean)

    def fileOutput(self, logType, boolean):
        self.logDict[logType]["doFileOutput"] = bool(boolean)

    def neutral(self, text):
        if

    def info(self, text):

    def warn(self, text):

    def error(self, text):

    def critical(self, text):
