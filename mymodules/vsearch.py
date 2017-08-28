def search4letters(phase:str, letters:str = 'aeiou') -> set:
    '''Entering letters'''
    return set(letters).intersection(set(phase))
