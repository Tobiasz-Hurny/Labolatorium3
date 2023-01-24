import logging


class lab:
    i = input("""
     Wcisnij:
     1. aby wyświetlić Debug
     2. aby wyświetlić Info
     3. aby wyświetlić Warning
     4. aby wyświetlić Error
     5. aby wyświetlić Critical 
    """)
    if i == '1':
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
        logging.debug('Tak to wygląda')
    elif i == '2':
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
        logging.info('A to tak')
    elif i == '3':
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.WARNING)
        logging.warning('To jest Ostrzeżenie!')
    elif i == '4':
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.ERROR)
        logging.error('Błąd w systemie!!')
    elif i == '5':
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.CRITICAL)
        logging.critical('Krytyczne uszkodzenia')
    else:
        print('nie było takiej opcji!')
