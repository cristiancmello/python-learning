# Data Compression
# Alguns dados e arquivos podem ser comprimidos diretamente com módulos, incluindo:
# zlib, gzip, bz2, lzma, zipfile e tarfile
import zlib
string = b'witch which has which witches wrist watch'   # b sinaliza strings ASCII (1 char = 1 byte)

print('{0} bytes'.format(len(string)))          # 41 bytes

# Comprimir...
str_compressed = zlib.compress(string)
print('{0} bytes'.format(len(str_compressed)))  # 37 bytes
