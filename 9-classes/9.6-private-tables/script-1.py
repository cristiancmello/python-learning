# Private Variables
# Em Python, não existe proteção de acesso 'private' aos membros das classes
# Usa-se, entretanto, convenções de nomes para nomear membros privados.

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
        
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
            
    __update = update   # cópia privada do método update() original

class MappingSubClass(Mapping):
    
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)
