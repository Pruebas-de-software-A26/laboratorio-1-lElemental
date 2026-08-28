import user_manager
import logging

logging.basicConfig(
    level = logging.DEBUG,
    filename =  'test.log',
    filemode = 'w'    
)

if __name__ == "__main__":
    Manager = user_manager.UserManager()

    logging.info('Test Case 1(RF1)')

    Manager.add_user(1,"Alice")
   

    logging.info('Pass using the debugger')
    
    logging.info('end Test CASE')

    logging.info('Test Case 2(RF2)')

    #Manager.add_user(1,"Alice")
    Manager.add_user(2,"Bob")
    Manager.add_user(3,"Charlie")

    user1 = Manager.find_user(2)

    logging.info('before if')
    if user1['name'] == 'Bob':
        logging.info('PASS')
    else:
        logging.info('FAIL')

    logging.info('end Test CASE3(RF3)')

    Manager.delete_user(3)
    logging.info('PASS using debugging')
    logging.info('end Test Case')

    logging.info('Test Case 4(RF4)')

    all_names = Manager.get_all_names()

    logging.info(f'The names are: {all_names}')
    if all_names == ['Alice', 'Bob']:
        logging.info('PASS')
    else:
        logging.info('FAIL')
        logging.warning('return the IDs')

    logging.info('Test case 5  (RNF1)')

    for i in range (1000):
        Manager.add_user(i, 'user'+str(i))
    logging.info('PASS using debugging')
    logging.info('end Test Case')