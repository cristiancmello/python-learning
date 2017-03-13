# Looping Techniques
point = {'x': 100, 'y': 200}
for k, v in point.items():
    print(k, v, sep='=')
    
# OUTPUT
# x=100
# y=200

# Responder com índice e valor ao mesmo tempo
for i, v in enumerate(['orange', 'apple', 'strawberry']):
    print(i,v,sep='=>')
    
# OUTPUT
# 0=>orange
# 1=>apple
# 2=>strawberry

# Parear entradas com a função 'zip()'
keys = ['name', 'email', 'tel']
values = ['John Doe', 'john@doe.com', '(122) 1223456']

for k, v in zip(keys, values):
    print('{0}: {1}'.format(k, v))
    
# OUTPUT
# name: John Doe
# email: john@doe.com
# tel: (122) 1223456

