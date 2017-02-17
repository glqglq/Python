CODEC = 'utf-8'
FILE = 'c:\Python27\io.txt'
hello_out = u'Hello World\n'
bytes_out = hello_out.encode(CODEC)
f = open('c:\Python27\io.txt','w')
f.write(bytes_out)
f.close()
f = open(FILE,'r')
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)
print hello_in,
raw_input()
