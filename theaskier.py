import requests, bs4

#program initiate
print('=================================')
print('Welcome to THE ASKIER - NETSHOES')
print('#goNets')
print('=================================')

#Seleting the SKU
print('Insert the SKU that you want:')
product_sku = input('>>> ')

#confirming the SKU
print('You selected the product with SKU',product_sku, '. Confirm: Y/n')
confirmation_sku = input('>>> ')
confirmated_sku = False
while(confirmated_sku == False):
	if confirmation_sku == 'Y' or confirmation_sku == 'y':
		print('lalalal')
		confirmated_sku = True
	else:
		print('Ok. You wan\'t another SKU, right? Type the sku again:')
		product_sku = input('>>> ')

#Checking on Netshoes Website
print('Let me check the price of this product on Netshoes Website - Direct Access - No cookie')
url_netshoes = 'http://www.netshoes.com.br/produto/' + product_sku
print('The URL of the product',product_sku,'is', url_netshoes)
response_netshoes = requests.get(url_netshoes)
print(response_netshoes)

#Getting the HTML of Netshoes webpage
parsing_response_netshoes = bs4.BeautifulSoup(response_netshoes.text,'html.parser')

#Getting the NAME of the product
name_product_netshoes = parsing_response_netshoes.select('.base-title')
print('The name of the product is: ', name_product_netshoes[0].getText())

#Getting the PRICE of the product
price_product_netshoes = parsing_response_netshoes.select('.new-price')
print('The price of the product is: ', price_product_netshoes[0].getText())

#Getting the HTML of Centauro webpage
url_centauro = 'http://esportes.centauro.com.br/search?w=' + name_product_netshoes[0].getText()
response_centauro = requests.get(url_centauro)
print(response_centauro) #print in the response of the website --> Status 200, 300, 400

#Parsing the HTML of Centauro webpage
parsing_response_centauro = bs4.BeautifulSoup(response_centauro.text,'html.parser')

#Getting the NAME of the product on centauro
name_product_centauro = parsing_response_centauro.select('#zone1_product1 .product-name .goto-pdp')
print('The name of the product in Centauro is: ',name_product_centauro[0].getText())
print(len(name_product_centauro[0].getText()))

#Getting the PRICE of the produc
price_product_centauro = parsing_response_centauro.select('#zone1_product1 .product-name .goto-pdp')
print(len(price_product_centauro[0]))

name_product_centauro_1 = parsing_response_centauro.find_all(attrs={"data-product-skuid": "849291Q4"})
print(name_product_centauro_1)

#Getting the NAME of the product of CENTAURO
#name_product_centauro = parsing_response_centauro.select('.base-title')
#print('The name of the product is: ', name_product_centauro[0].getText())


#Getting the PRICE of the product of CENTAURO
#price_product_centuaro = parsing_response_centauro.select('.price')
#print(price_product_centuaro)
#print('The price of the product is: ', parsing_response_centauro[0].getText())


	#If you don't have the sku, insert the product or the url
		#if it's a product
			#go to netshoes website
				#search the product
					#came back with the product title, SKU, price.





#Making the request to the competitor
	#loop competitors
		#while find product
			#From title (hole string):
				#came back with the product title, sku and price




