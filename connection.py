

# TRACKINGS TEST 
#tracking='8515-752693-1z';
#tracking='4203319892612927005143010007020317';
#tracking='1z2y842v0301429552';
#tracking='1ZW709680337131270';
#tracking='420331989374869903503391326026';
#tracking='8515-752693-1z';
#tracking='61290983461420188456’;
#TBA165795238301
#TBA165757372301
#1Z6A3E340316394662
#TBA165746066201
#1Z6A3E340316408941
#42033198]9400111108435512641923
#42033198]9400111699000626403728
#1Z6A3E340316352895
#1001901781970003319800501585236374 fedex
#1LS731607009591
#4795851152 DHL

# OTRO
# tracking="6349564863"
# tracking="TBA155438582801"
# tracking="TBA165795238301"
# tracking= "rbueso@ss-honduras.com"
# tracking= "jcrreichmann@gmail.com"
# tracking= "8429-7700-1"
# entity='SPSLC35013'


# # Minidom
# from xml.dom.minidom import *
# from django.db import connection

# # Zeep
# from zeep import Client
# from zeep.cache import SqliteCache
# from zeep.transports import Transport




# HONDURAS
# url = 'http://181.115.48.20:3691/CSSoapService?wsdl'
# alias = 'http://181.115.48.20:3691/Invoke?Handler=CSSoapService'
# user = "walteraraujo"
# password = "Junio21@"
# tracking="8515-752693-1z"

# client = Client(url)

# try:
# 	service = client.create_service( 
# 	"{urn:CSSoapService}CSSoapServiceSoap",
# 	alias
# 	)
# 	key = service.StartSession(user, password)
# 	acces_key=int(key['access_key'])


# 	type="WH"
# 	start_date = "2018-10-30"
# 	end_date = "2021-10-14"
# 	flags = 0x08000000
# 	# flags = 0x00001000
# 	record_quantity = 1
# 	backwards_order = 1
# 	jsFunction = "FindTracking"
# 	# jsFunction = "FindClientUsingPurchaseOrder"
# 	# jsFunction = "FindClientUsingEmail"
# 	xml_params = "<Parameters><Parameter>"+tracking+"</Parameter></Parameters>"
	
	

# 	result = service.GetFirstTransbyDateJS(acces_key,
# 		type,start_date,end_date,flags,
# 		record_quantity,backwards_order,
# 		jsFunction,xml_params)
# 	print('resultado',result)
# 	# accounting_transactions = service.GetAccountingTransactions(acces_key,type,flags,'SPSLC35013')
# 	# print('accounting',accounting_transactions)

# 	# print('VERIFICAR ACCOUNT')
# 	# entity_transactions = service.GetEntityTransactions(acces_key,'SPSLC35013',flags,start_date,end_date)
# 	# print('accounting',accounting_transactions)
# 	more_result=result['more_results']
	
	
# 	if(more_result > 0 and result['cookie'] is not None):
# 		cookie=result['cookie']; 
# 		trackinginfo=service.GetNextTransbyDate(result['cookie']);
# 		trackdetails=trackinginfo['trans_list_xml']
# 		print('tracking info',trackinginfo)
# 		print(trackdetails)
# 		xml = parseString(trackdetails)
# 		status = xml.getElementsByTagName('Status')
# 		print(status[0].firstChild.data)		
# except Exception as e:
# 	print(str(e))



# Third party
from xml.dom.minidom import *
from zeep import Client


def connect_to_server(url,alias):
	client = Client(url)
	service = client.create_service( 
	"{urn:CSSoapService}CSSoapServiceSoap",
	alias
	)
	return service

def search_by_tracking_id(service,acces_key,type,start_date,end_date,flags,record_quantity,backwards_order,js_function,xml_params):
	result = service.GetFirstTransbyDateJS(
		acces_key,
		type,start_date,end_date,flags,
		record_quantity,backwards_order,
		js_function,xml_params
	)
	return result

def get_acces_key(service,user,password):
	session = service.StartSession(user, password)
	acces_key=int(session['access_key'])
	return acces_key

def get_transaction_status(parsed_trackdetails):
	result = parsed_trackdetails.getElementsByTagName('Status')
	return result[0].firstChild.data

def get_cookie(result):
    cookie = result['cookie']
    return cookie

def get_trans_by_date(service,cookie):
	trackinginfo=service.GetNextTransbyDate(cookie);
	return trackinginfo

def parse_xml(xml):
	parsed_trackdetails = parseString(xml['trans_list_xml'])
	return parsed_trackdetails

def main():

	# Magaya's El Salvador server credentials
	url = 'http://181.115.68.74:3691/CSSoapService?wsdl'
	alias = 'http://181.115.68.74:3691/Invoke?Handler=CSSoapService'
	user = "crisarias"
	password = "Api@123456"
	tracking="528674226949"
	# tracking="284502343716"
	
	# Magaya's Honduran server credentials
	# url = 'http://181.115.48.20:3691/CSSoapService?wsdl'
	# alias = 'http://181.115.48.20:3691/Invoke?Handler=CSSoapService'
	# user = "walteraraujo"
	# password = "Junio21@"


	# Tracking example
	# tracking="8515-752693-1z"


	type="WH"
	start_date = "2018-10-30"
	end_date = "2021-10-26"
	flags = 0x08000000
	record_quantity = 1
	backwards_order = 1
	js_function = "FindTracking"
	xml_params = "<Parameters><Parameter>"+tracking+"</Parameter></Parameters>"
	

	# Service creation
	service = connect_to_server(url,alias)
	acces_key=get_acces_key(service,user,password)
	result = search_by_tracking_id(service,acces_key,type,start_date,end_date,flags,record_quantity,backwards_order,js_function,xml_params)
	
	more_result=result['more_results']
	if(more_result > 0 and get_cookie is not None):
		trackdetails=get_trans_by_date(service,get_cookie(result))
		parsed_trackdetails = parse_xml(trackdetails)
		status = get_transaction_status(parsed_trackdetails)
		print(status)

if __name__ == '__main__':
	main()
