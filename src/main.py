import csv
import requests
import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen

# url of rss feed
xml = 'https://www.w3schools.com/xml/cd_catalog.xml'
jsons = 'https://jsonplaceholder.typicode.com/todos?page=2'

FILENAME = '..\\files\json.csv'

# creating HTTP response object from given url
respXML = requests.get(xml)
xmlf = urlopen(xml)


respJSON = requests.get(jsons)
print('\nContent Json\n')
print(respJSON.content)
html = urlopen(jsons)
j_obj = json.load(html)
print("\n\n")
print(j_obj)




def salvarCSV(vet):
	try:
		type = input("\nDigite 'w' para Substituir ou 'a' para Acrescentar\n ")
		with open(FILENAME, type, newline='') as csvfile:
			file = csv.writer(csvfile, delimiter=";")
			header = ['dados']
			file.writerow(header)
			string = []
			for page in vet:
				string.append([page])
				string.append({"___________________________________________________________________________________"})
			else:
				file.writerows(string)
	except ValueError:
		opcErro(0)
	except PermissionError:
		 opcErro(1)


def opcErro(erro):
	if erro == 1:
		print ("Oops!  Não foi possível salvar, pois o arquivo está aberto.  Tente novamente...\n")
	elif erro == 2:
		print("Error de caracter")
	else:
		print("Erro invalido")

	opc = input("\nDigite 1 para tentar novamente ou 0 para sair\n")
	if opc == "1":
	   salvarCSV()
	elif opc == "0":
	   print("Os dados não foram salvos")
	else:
	   print("Digito inválido")

#Chamar Metodo SalvaCSV
salvarCSV(j_obj)
salvarCSV(xmlf)
