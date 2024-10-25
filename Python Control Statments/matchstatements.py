character = input("Enter any single alphabatic character : ")
def check_vowel(character):    
    match character:
        case 'a': return "Vowel alphabet"
        case 'e': return "Vowel alphabet"
        case 'i': return "Vowel alphabet"
        case 'o': return "Vowel alphabet"
        case 'u': return "Vowel alphabet"
        case _: return "Simple alphabet"

print (check_vowel(character))
    
    