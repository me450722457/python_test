import re
a = 'C2CQW++3WasdfJava4Pythonnnnnnnty_n& 6JQavwQTWDaScrQEWWQSipt8Python4pythwqewaregon5'
b = '''
192.168.6.8
asdad.asdf.asd.asd
19236456.156.15.556
10.1.1.1
'''
c = re.findall('\d[0-192]{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', b)
print(c)
