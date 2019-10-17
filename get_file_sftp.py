import pysftp

myHostname = '192.168.69.9'
myUsername = 'gmann'
myPassword = '2005Ford'

# print('Accessing sftp for ' + myHostname + " using user " + myUsername + ' with password ' + myPassword)

with pysftp.Connection(myHostname, username=myUsername, password=myPassword)
    print('Connection successfully established...')


    # switch to remote directory
    sftp.cwd('/tmp/')

    # obtain structure of the remote directory 
    directory_strucutre = sftp.listdir_attr()


    for attr in directory_strucutre:
        print attr.filename, attr