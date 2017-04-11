import logging

logging.basicConfig(
    filename = 'hi.log',
    level = 10,
    format = "%(levelname)-10s %(asctime)s %(message)s"
)

logging.error('hi')
