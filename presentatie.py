def presenteer(mijn_dict,totaal):
    print()
    for i,j in mijn_dict.items():
        print(f"{i} : {j}")
    print(26*"=")
    print(f"totaal : {totaal} euro")

mijn_dict={'vis' : 10,'vlees': 25,'overig' : 15}
totaal=50   
print(presenteer(mijn_dict,totaal))
