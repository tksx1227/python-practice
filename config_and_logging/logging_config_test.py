import logging.config


# fileConfig or dictConfig でロギングの設定を行う
logging.config.fileConfig("logging.ini")
# logging.config.dictConfig({
#     "version": 1,
#     "formatters": {
#         "sampleFormatter": {
#             "format": "%(asctime)s %(name)-13s %(levelname)-8s %(message)s"
#         }
#     },
#     "handlers": {
#         "sampleHandlers": {
#             "class": "logging.StreamHandler",
#             "formatter": "sampleFormatter",
#             "level": logging.DEBUG
#         }
#     },
#     "root": {
#         "handlers": ["sampleHandlers"],
#         "level": logging.WARNING
#     },
#     "loggers": {
#         "simpleExample": {
#             "handlers": ["sampleHandlers"],
#             "level": logging.DEBUG,
#             "propagate": 0
#         }
#     }
# })

logger_root = logging.getLogger(__name__)
logger_simpleExample = logging.getLogger("simpleExample")

# root の設定が反映されるため、レベルが WARNING になっている
logger_root.critical("critical message")
logger_root.error("error message")
logger_root.warning("warn message")
logger_root.info("info message")
logger_root.debug("debug message")

# simpleExample の設定が反映されるため、レベルが DEBUG になっている
logger_simpleExample.critical("critical message")
logger_simpleExample.error("error message")
logger_simpleExample.warning("warn message")
logger_simpleExample.info("info message")
logger_simpleExample.debug("debug message")
