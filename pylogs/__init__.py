"""
PyLogs :
A logging package for your python project

developed by SsomGrap
"""

TYPE_INFO = "info"
TYPE_WARN = "warn"
TYPE_ERROR = "error"
TYPE_CRITICAL = "critical"

COLORS = {
    "white": "",
    "red": "",
    "green": "",
    "blue": "",
    "orange": "",
    "yellow": ""
}


class Logger:

    def __int__(self, name, directory):
        """
        :param name: The name of your Logger (will be present in all messages formats).
        :param directory: The directory where the files logs will be created.
        :return: A Logger object and create a logs file when initialized.
        """
        self.name = name
        self.directory = directory
        self.logsDict = {
            "info": {"format": "", "colorization": False, "doTerminalOutput": True, "doFileOutput": True},
            "warn": {"format": "", "colorization": False, "doTerminalOutput": True, "doFileOutput": True},
            "error": {"format": "", "colorization": False, "doTerminalOutput": True, "doFileOutput": True},
            "critical": {"format": "", "colorization": False, "doTerminalOutput": True, "doFileOutput": True}
        }

    def getFormat(self, logType=""):
        """
        :param logType: If the logType is not specify, return all formats.
        :return: Logs format
        """
        if logType == "":
            result = []
            for logTyp in self.logsDict.items():
                result.append(self.logsDict[logTyp]["format"])
        else:
            result = self.logsDict[logType]["format"]
        return result

    def setFormat(self, logType, logFormat):
        self.logsDict[logType]["format"] = str(logFormat)

    def colorization(self, logType, boolean):
        self.logsDict[logType]["colorization"] = bool(boolean)

    def terminalOutput(self, logType, boolean):
        self.logsDict[logType]["doTerminalOutput"] = bool(boolean)

    def fileOutput(self, logType, boolean):
        self.logsDict[logType]["doFileOutput"] = bool(boolean)

    def neutral(self, text):
        if self.logsDict["neutral"]["doTerminalOutput"]:
            print(text)
        if self.logsDict["neutral"]["doFileOutput"]:
            print(text)

    def loggerPrint(self, logType, text):
        if self.logsDict[logType]["doTerminalOutput"]:
            print(self.logsDict[logType]["format"], text)
        if self.logsDict[logType]["doFileOutput"]:
            print(text)

    def info(self, text):
        self.loggerPrint(TYPE_INFO, text)

    def warn(self, text):
        self.loggerPrint(TYPE_WARN, text)

    def error(self, text):
        self.loggerPrint(TYPE_ERROR, text)

    def critical(self, text):
        self.loggerPrint(TYPE_CRITICAL, text)
