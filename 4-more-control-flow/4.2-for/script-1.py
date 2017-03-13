# for Statements
# A instrução 'for' em Python é semelhante ao 'foreach' em outras linguagens
words = ['cat', 'dog', 'fish']

# for para percorrer por cada elemento da lista
for word in words:
    print(word, len(word))
    
for word in words[:]: # percorrer ao longo de uma cópia de slice da lista
    if len(word) > 3:
        words.insert(0, word)
        
