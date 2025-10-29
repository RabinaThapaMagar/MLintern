#logging means program run huda kheri every message or event track or record garnu ho. if program run garda kunai error
#ayo bhaney code ko kun part ma error ayo vanera thaha hudaina so teslai debug ie error find garne ra fic garne kaam logging ko ho
#logging is important kina vane kun line of code ma k kaam vairaxa vanera yesle vanxa so that hamlai tahha hos error ka nira xa vanera
#log file haru banayera rakhyo bhaney code afai lai sajilo hunxa 
#there are levels of logging:DEBUG – Detailed info (for developers).
# kunai debug garnu parne huna sakxa, or info, error , warning ra critical message hunxa testo lai log garera rakhney

#level of logging
#DEBUG – Detailed info (for developers).
#INFO – Confirmation that things are working.

#WARNING – Something unexpected, but program still runs.

#ERROR – A serious issue, program may not work correctly.

#CRITICAL – Program is unable to continue.

# yesko op chai log.log vane file ma auxa


import logging


#configure the log
#w means file xaina vane create garne if xa vane tei file ma overwrite gardine
# jastai apxi hamlai error ra critical or kunai ko matra log file rakhna paryo vane we can change logging ko level like logging.error rakhne or logging.critical 
logging.basicConfig(level=logging.INFO, filename = "log.log",filemode = "w",format="%(asctime)s - %(levelname)s - %(message)s")#logging.DEBUG matlab yesma chai level rakheko ho debug rakhim vane debug dekhi critical samma ko lg rakhxa raaru rakhna ni milxa, as your requirements paxi custom log banauneybela pani


# logging the variable value
# x = 2
# logging.info(f"the value of x is {x}")

# logging.debug("debug")  # as deubg ra info chai least important ho kinaki debug vaneko ka error auxa ra fic garne kaam ho
# logging.info("info")# ra info vaneko just msg ho so yo op ma auna imp xaina
# logging.warning("warning")# op ma warning, error, ra critical which are very imp show hunxa
# logging.error("error")
# logging.critical("critical")


#log a stack trace ie meaning if an exception occur and we want to log that 
# try:
#     1 / 0
# except ZeroDivisionError as e:
#     logging.exception("test")



##custom log ie different log files which contain different information
logger = logging.getLogger(__name__) # yo bhitra afulai chaheko log ko naam rakne if yo name vaneko log xa vane dinxa if xaina vane it will create the name vane log



#handler: handler vaneko hamlai custom log haru lai seperate file format ie mathi ko basic config ma rakna xaina vane we cam use handler
handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
handler.setFormatter(formatter) #setting the handler

# add handler to the log
# test.log is just a file on your computer.
# It will be created automatically (if it doesn’t exist).
# All logs handled by this FileHandler will be written (saved) into this file instead of (or in addition to) the console.
logger.addHandler(handler)
logger.info("test the custom logger")