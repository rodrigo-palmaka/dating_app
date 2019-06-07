import json
import requests
from find_restaurant import find_restaurant

def main():
    j = open("cusTable.txt","w+")
    f = find_restaurant()
    # f.city_ID = 306
    n = f.allCuisines()
    for k,v in n.items():
        # num = f.get_cuisine(i)
        # html = "<input type='checkbox' name='cuis' value="+str(v)+">"+k+"<br>"
        j.write(k + ' TINYINT(1), ')

        # j.write(html + "\n")
    # j.write(n[-1] + ' TINYINT(1)')
main()
