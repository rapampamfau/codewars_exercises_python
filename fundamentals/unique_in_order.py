def unique_in_order(sequence):
    unique = []
    current = "" 
    for element in sequence:
        if element != current:
            current = element
            unique.append(element)
    return unique
        
