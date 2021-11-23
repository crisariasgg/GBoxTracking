from xml.dom.minidom import *
from zeep import Client




class MagayaConnection():

	def __init__(self,url,alias,user,password):
		self.url = url
		self.alias = alias
		self.service = self.connect_to_server(self.url,self.alias)
		self.acces_key=self.get_acces_key(self.service,user,password)


	def connect_to_server(url,alias):
		client = Client(url)
		service = client.create_service( 
		"{urn:CSSoapService}CSSoapServiceSoap",
		alias
		)
		return service
	
	
	def get_acces_key(service,user,password):
		session = service.StartSession(user, password)
		acces_key=int(session['access_key'])
		return acces_key

