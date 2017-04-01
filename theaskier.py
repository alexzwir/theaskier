import requests, bs4

response_netshoes = requests.get('http://www.netshoes.com.br/produto/100-whey-gold-standard-2-lbs--optimum-nutrition-165-7007-975?&lkey=a6')
response_madrugadao = requests.get('http://www.madrugaosuplementos.com.br/100-whey-protein-900g-optimum-nutrition/')
response_submarino = requests.get('https://www.submarino.com.br/produto/14112555/whey-protein-gold-100-909g-optimum-nutrition-banana?DCSext.recom=RR_category_page.rr1-CategoryTopProducts&chave=b2wads_582495e617e124414afe6273_18274474000197&condition=NEW&nm_origem=rec_category_page.rr1-CategoryTopProducts&nm_ranking_rec=2&sellerId=18274474000197')
response_decathlon = requests.get('http://www.decathlon.com.br/suplementos-e-saude/suplementacao/proteinas/gold-standard-whey-on-baunilha?skuId=984842')

parsing_response_netshoes = bs4.BeautifulSoup(response_netshoes.text,'html.parser')
price_netshoes = parsing_response_netshoes.select('.new-price')

response_madrugadao = bs4.BeautifulSoup(response_madrugadao.text,'html.parser')
price_madrugadao = response_madrugadao.select('.special-price span .price')

print('NETSHOES | MADRUGADAO | SUBMARINO | DECATHLON')

prices_lists_players = [(price_netshoes[0].getText()),(price_madrugadao[0].getText())]
 
print(prices_lists_players[0]+ "|"+prices_lists_players[1])

"""

print("O preco do Madrugadao eh " +  )

print('O preco da Netshoes eh ' + price_netshoes)
print('O preco no Madrugadao Suplemento eh ' + price_madrugadao)
print('O preco no Madrugadao Suplemento eh ' + price_madrugadao)
print('O preco no Madrugadao Suplemento eh ' + price_madrugadao)
"""