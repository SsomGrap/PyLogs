# PyLogs
### A logging package for your python project
***

## Description
PyLogs allow you to add a logger to your python project. This logger can send the logs directly to the terminal and/or save them to an external file. Several options are available, such as :
- format of the logs
- the colorization of the text
- etc...

Work on python 3 and 2. For Windows, macOS and Linux.
***

## Installation
You just need to run this command in your **terminal** : 
```
pip install PyLogs
```
***

## Functions and Constant
A list of all functions and constant in this package.
```
pylogs.TYPE_NEUTRAL
pylogs.TYPE_INFO
pylogs.TYPE_WARN
pylogs.TYPE_ERROR
pylogs.TYPE_CRITICAL
```
```
pylogs.Logger()

pylogs.Logger.getFormat()
pylogs.Logger.setFormat()

pylogs.Logger.colorization()
pylogs.Logger.terminalOutput()
pylogs.Logger.fileOutput()

pylogs.Logger.neutral()
pylogs.Logger.info()
pylogs.Logger.warn()
pylogs.Logger.error()
pylogs.Logger.critical()
```
***

## Exemple
An example of how to implement PyLogs to your projects
```
>>> import pylogs
>>> logger = pylogs.Logger(name="MyLogger", directory="./logs")
>>> logger.setFormat(pylogs.TYPE_INFO, "[Un truc] [Un second] "
>>> logger.info("Connected")

# Create a log file named with the datetime of your computer
# It contain the output
[Un truc] [Un second] Connected

>>> logger.fileOutput(False) # Turn off the file ouput for all logs
>>> logger.neutral("A random message")
A random message

>>> logger.fileOutput(TYPE_CRITICAL, True) # Turn on the file output for the critical messages
>>> logger.terminalOutput(TYPE_CRITICAL, False)
>>> logger.critical("critical error")

# The output will be in the logs file but not in the terminal (Only for the critical messages)
```
***

## Credits
developed by *SsomGrap*