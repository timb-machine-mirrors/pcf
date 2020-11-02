from system.db_initiation import create_db
from system.config_load import change_secret_key
from system.cert_initiation import create_self_signed_cert
from os import mkdir, path

print('''
##################################################################
#                                                                #
#   .----------------.  .----------------.  .----------------.   #
#  | .--------------. || .--------------. || .--------------. |  #
#  | |   ______     | || |     ______   | || |  _________   | |  #
#  | |  |_   __ \   | || |   .' ___  |  | || | |_   ___  |  | |  #
#  | |    | |__) |  | || |  / .'   \_|  | || |   | |_  \_|  | |  #
#  | |    |  ___/   | || |  | |         | || |   |  _|      | |  #
#  | |   _| |_      | || |  \ `.___.'\  | || |  _| |_       | |  #
#  | |  |_____|     | || |   `._____.'  | || | |_____|      | |  #
#  | |              | || |              | || |              | |  #
#  | '--------------' || '--------------' || '--------------' |  #
#   '----------------'  '----------------'  '----------------'   #
#                                                                #
#  https://gitlab.com/invuls/pentest-projects/web-hack-toolkits  #
#                                                                #
##################################################################

This script will do following:
1. Renames database /configuration/database.sqlite3
2. Regenerates SSL certificates
3. Regenerates session key.
4. Creates new empty /configuration/database.sqlite3 database
5. Creates /tmp_storage/ folder 
''')

print('Are you sure running it? Write: DELETE_ALL')
init_proof = input('Your input: ')
if init_proof != 'DELETE_ALL':
    exit(0)

create_db()

change_secret_key()

create_self_signed_cert()

if not path.exists('tmp_storage'):
    mkdir('tmp_storage')

print('Success!')
