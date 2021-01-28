filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except:
    msg = 'Sorry, the file ' + filename + ' does not exist.'
    print(msg)