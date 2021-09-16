# notes_de_la_classe = [('Enzo', 3), ('Emma', 16), ('Lucas', 14), ('Manon', 13)]
# notes_de_la_classe.append(('Farid',13))
# 
# def nom_du_genie(les_notes): 
#     genie = None 
#     note_max = None
#     for (nom, note) in les_notes:
#         if note_max == None or note > note_max: 
#             note_max = note 
#             genie = nom 
#     return genie 
# 
# print(nom_du_genie([ ]))

notes = {'Enzo': ('Math', 3), 'Emma': ('Math', 16), 'Lucas': ('NSI', 14), 'Manon': ('NSI', 13)}
notes['Farid']=("NSI",15)
print(notes)
def tri_par_matières(les_notes): 
    matiere1 = None 
    matiere2 = None
    note_mat1=[]
    note_mat2=[]
    for (nom, (matiere, note)) in les_notes.items():
        if matiere1 == None or matiere==matiere1: 
            matiere1=matiere
            note_mat1.append(note)
        elif matiere2 == None or matiere==matiere2:
            matiere2=matiere
            note_mat2.append(note)
    return {matiere1:note_mat1, matiere2:note_mat2}


print(tri_par_matières(notes))