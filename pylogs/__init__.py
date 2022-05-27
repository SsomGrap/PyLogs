"""
PyLogs :
A logging package for your python project

developed by SsomGrap
"""

from datetime import datetime

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
        self.time = str(str(datetime.now()).replace(" ", "_").split(".").pop(0))
        self.logFile = f"{directory}/{self.name}_{self.time}.log"

    def getFormat(self, logType=""):
        """
        :param logType: TYPE_INFO, TYPE_WARN, TYPE_ERROR, TYPE_CRITICAL. If the logType is not specify, return all logs types formats.
        :return: Logs format
        """
        if logType == "":
            result = []
            for logTyp in self.logsDict.items():
                result.append(self.logsDict[logTyp]["format"])
        else:
            result = self.logsDict[logType]["format"]
        return result

    def setFormat(self, logFormat, logType=""):
        """
        :param logType: TYPE_INFO, TYPE_WARN, TYPE_ERROR, TYPE_CRITICAL. If the logType is not specify, define the format for all logs types.
        :param logFormat: Write here the new format you need
        """
        if logType == "":
            for logTyp in self.logsDict.items():
                self.logsDict[logTyp]["format"] = str(logFormat)
        else:
            self.logsDict[logType]["format"] = str(logFormat)

    def colorization(self, boolean, logType=""):
        """
        The logs colorization is only applied to the terminal logs.
        :param logType: TYPE_INFO, TYPE_WARN, TYPE_ERROR, TYPE_CRITICAL. If the logType is not specify, define the colorization for all logs types.
        :param boolean: True or False for the colorization of your logs
        """
        if logType == "":
            for logTyp in self.logsDict.items():
                self.logsDict[logTyp]["colorization"] = bool(boolean)
        else:
            self.logsDict[logType]["colorization"] = bool(boolean)

    def terminalOutput(self, boolean, logType=""):
        """
        It's true for all logs by default
        :param logType: TYPE_INFO, TYPE_WARN, TYPE_ERROR, TYPE_CRITICAL. If the logType is not specify, define the terminalOutput for all logs types.
        :param boolean: True or False
        """
        if logType == "":
            for logTyp in self.logsDict.items():
                self.logsDict[logTyp]["doTerminalOutput"] = bool(boolean)
        else:
            self.logsDict[logType]["doTerminalOutput"] = bool(boolean)

    def fileOutput(self, logType, boolean):
        """
        It's true for all logs by default
        :param logType: TYPE_INFO, TYPE_WARN, TYPE_ERROR, TYPE_CRITICAL. If the logType is not specify, define the fileOutput for all logs types.
        :param boolean: True or False
        """
        if logType == "":
            for logTyp in self.logsDict.items():
                self.logsDict[logTyp]["doFileOutput"] = bool(boolean)
        else:
            self.logsDict[logType]["doFileOutput"] = bool(boolean)

    def neutral(self, text):
        """
        This log has no format
        :param text:
        """
        if self.logsDict["neutral"]["doTerminalOutput"]:
            print(text)
        if self.logsDict["neutral"]["doFileOutput"]:
            with open(self.logFile, "a") as logFile:
                logFile.write(text)

    def loggerPrint(self, logType, text):
        """
        :param logType:
        :param text:
        """
        if self.logsDict[logType]["doTerminalOutput"]:
            print(self.logsDict[logType]["format"], text)
        if self.logsDict[logType]["doFileOutput"]:
            with open(self.logFile, "a") as logFile:
                logFile.write(f"{self.logsDict[logType]['format']} {text}")

    def info(self, text):
        """
        :param text:
        :return:
        """
        self.loggerPrint(TYPE_INFO, text)

    def warn(self, text):
        """
        :param text:
        :return:
        """
        self.loggerPrint(TYPE_WARN, text)

    def error(self, text):
        """
        :param text:
        :return:
        """
        self.loggerPrint(TYPE_ERROR, text)

    def critical(self, text):
        """
        :param text:
        :return:
        """
        self.loggerPrint(TYPE_CRITICAL, text)
