# pass Statements
# A princípio, 'pass' não faz nada. No entanto, pode ser útil para forjar um statement
# sintaticamente válido mas que não irá fazer nada.

# Uma classe sintaticamente válida mas vazia
class MyEmptyClass:
    pass

# 'pass' também pode ajudar a criar estruturas abstratas, num "faz de conta"
def initlog(*args):
    pass                # Não esqueça de implementar algo...
