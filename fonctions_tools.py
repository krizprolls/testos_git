'''
Ensemble de fonctions
'''


def input_int(message:str)->int:
    '''
    fonction qui verifie qu'il s'agit bien d'un int
    '''
    reponse = input(message)
    try:
        nombre = int(reponse)
    except ValueError as v_e:
        print("entrer un ENTIER !")
        print(v_e)
        nombre = input_int(message)
    return nombre


def input_int_positif(message:str)->int:
    '''
    fonction qui verifie qu'il s'agit bien d'un int positif
    '''
    reponse_pos= input_int(message)
    if reponse_pos<0:
        print("entrer un POSITIF ! !")
        reponse_pos = input_int_positif(message)
    return reponse_pos
