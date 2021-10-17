import json
import random
import string


en_relation = []
de_relation = []


def en_code(en_string):
    """
    A Function used to generate a secret code which includes all the letters, digits and special characters
    
    function format : en_code(<-String_to_be_Encoded->)
    
    Usage:
    >>>en_code("Adithiyaa")
    >>>!5qhw2}P( #Generates a en-coded string)
    """


    relation_tree = json.load(open('RelationTree.json'))
    encoded = ""
    

    if en_string in relation_tree["encoding"].keys():
        # encoded = "".join(lst[1] for lst in relation_tree[en_string])
        encoded = "".join(lst[1] for lst in relation_tree["encoding"][en_string])

    else:
        characters = string.ascii_letters + string.digits + string.punctuation

        for i in range(len(en_string)):
            code = random.choice(characters)
            en_relation.extend([[en_string[i], code]])
            de_relation.extend([[code, en_string[i]]])
            encoded = encoded + code

        en_main = relation_tree["encoding"]
        en_main[en_string] = en_relation
        de_main = relation_tree["decoding"]
        de_main[encoded] = de_relation

        j = json.dumps(relation_tree)
        with open('RelationTree.json', 'w') as f:
            f.write(j)
            f.close()

    print("The secret code which only this computer can decode is as below")
    print(encoded)


def de_code(de_string):
    """
    A Function used to de-code a string which has been encoded using the encode function
    
    function format : de_code(<-String_to_be_Decoded->)
    
    Usage:
    >>>de_code("!5qhw2}P")
    >>>Adithiyaa(# Generates the de-coded string)
    """


    relation_tree = json.load(open('RelationTree.json'))

    if de_string in relation_tree["decoding"].keys():
        decoded = "".join(lst[1] for lst in relation_tree["decoding"][de_string])
        print("\nVoila! you have decoded it...")
        print(de_string + " --> " + decoded)

    else:
        print("\nSorry!, there was no such secret code created in this computer. \nTry creating one using the 'endode(<-string->) function.")


en_code("Adithiyaa")
de_code("fwEb;]k!$")