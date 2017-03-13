# Scopes and Namespaces Example
# Exemplo de como se referencia escopos diferentes e namespaces, e como
# variáveis globais e não-locais (nonlocal) afetam o código.

def scope_test():
    def do_local():
        spam = 'local spam'
    
    def do_nonlocal():
        nonlocal spam           # spam será atribuído dentro do escopo de scope_test()
        spam = 'nonlocal spam'
    
    def do_global():
        global spam             # spam será atribuído globalmente em todo código
        spam = 'global spam'
    
    spam = 'test spam'
    do_local()
    print('Depois da atribuição local:', spam)
    
    do_nonlocal()
    print('Depois da atribuição não-local:', spam)
    
    do_global()
    print('Depois da atribuição global:', spam)
    
scope_test()
print('No escopo global:', spam)