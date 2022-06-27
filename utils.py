def log_init(name=None, level='logging.DEBUG', filepath='logs'):
    """
    Initializes logger and names file using today's date.
    :param name: Name of logger
    :param level: Logging level
    :param filepath: Filepath to logs
    :return: logger object to use in functions
    """
    import logging
    import datetime as dt

    # collect date
    today = dt.datetime.today()
    log_filename = f'{today.month:02d}-{today.day:02d}-{today.year}.log'

    # formatted logger
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %H:%M:%S'
    )
    # create file handler
    fh = logging.FileHandler(f'{filepath}/{log_filename}')
    fh.setFormatter(formatter)

    # create stream handler
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)

    # create logger object and set the level
    logger = logging.getLogger(name)
    logger.setLevel(eval(level))

    # add handlers to logger object
    logger.addHandler(fh)
    logger.addHandler(sh)

    return logger
