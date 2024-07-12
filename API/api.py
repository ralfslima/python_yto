# dontpad.com/ralflima
# IMPORTAÇÕES
import http.server
import socketserver
import json

# LISTA DE VENDAS
produtos = []

# ESTRUTURA BASE DA API
class MyHandler(http.server.BaseHTTPRequestHandler):

    # CABEÇALHO DE REQUISIÇÃO
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # CORS 
    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    # APLICAR CORS
    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    # REQUISIÇÃO POST
    def do_POST(self):
        if self.path == '/cadastrar':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = post_data.decode('utf-8')
            novo_produto = json.loads(post_data)
            produtos.append(novo_produto)
            
            self._set_response()
            self.wfile.write("Produto cadastrado com sucesso.".encode('utf-8'))

    # REQUISIÇÃO GET
    def do_GET(self):
        if self.path == '/listar':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self._send_cors_headers()
            self.end_headers()
            
            # Transforma a lista em JSON
            response_json = json.dumps(produtos)
            
            # Envia a resposta
            self.wfile.write(response_json.encode('utf-8'))

        elif self.path == '/vendas':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self._send_cors_headers()
            self.end_headers()

            # Dicionário para armazenar temporariamente os totais de vendas por vendedor
            vendas_por_vendedor_temp = {
                'Cleber': 0,
                'Daniel': 0,
                'Lucas': 0,
                'Paula': 0,
                'Sabrina': 0
            }
            
            # Iterar sobre a lista de produtos para calcular as vendas por vendedor
            for produto in produtos:
                if 'vendedor' in produto and produto['vendedor'] in vendas_por_vendedor_temp:
                    # Convertendo o valor de produto['total'] para float, se possível
                    try:
                        total_venda = float(produto['total'])
                    except ValueError:
                        total_venda = 0  # Em caso de erro na conversão, assume 0
                    
                    vendas_por_vendedor_temp[produto['vendedor']] += total_venda
            
            # Transforma o dicionário de vendas por vendedor em JSON
            response_json = json.dumps(vendas_por_vendedor_temp)
            
            # Envia a resposta
            self.wfile.write(response_json.encode('utf-8'))

        elif self.path == '/marcas':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self._send_cors_headers()
            self.end_headers()
            
            # Dicionário para armazenar temporariamente as quantidades por marca
            quantidade_por_marca_temp = {
                'Apple': 0,
                'Samsung': 0,
                'Sony': 0,
                'Philips': 0,
                'HP': 0,
                'Epson': 0,
                'Microsoft': 0
            }
            
            # Iterar sobre a lista de produtos para calcular as quantidades por marca
            for produto in produtos:
                if 'marca' in produto and produto['marca'] in quantidade_por_marca_temp:
                    # Convertendo o valor de produto['quantidade'] para int, se possível
                    try:
                        quantidade_produto = int(produto['quantidade'])
                    except ValueError:
                        quantidade_produto = 0  # Em caso de erro na conversão, assume 0
                    
                    quantidade_por_marca_temp[produto['marca']] += quantidade_produto
            
            # Transforma o dicionário de quantidade por marca em JSON
            response_json = json.dumps(quantidade_por_marca_temp)
            
            # Envia a resposta
            self.wfile.write(response_json.encode('utf-8'))

        elif self.path == '/produtos':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self._send_cors_headers()
            self.end_headers()
            
            # Lista para armazenar os produtos com nome e valor total
            lista_produtos_valor = []
            
            # Iterar sobre a lista de produtos para obter nome e valor total de cada produto
            for produto in produtos:
                if 'nome' in produto and 'total' in produto:
                    produto_info = {
                        'nome': produto['nome'],
                        'valor_total': produto['total']
                    }
                    lista_produtos_valor.append(produto_info)
            
            # Transforma a lista de produtos com nome e valor total em JSON
            response_json = json.dumps(lista_produtos_valor)
            
            # Envia a resposta
            self.wfile.write(response_json.encode('utf-8'))


    # REQUISIÇÃO DELETE
    def do_DELETE(self):
        if self.path.startswith('/remover/'):
            parts = self.path.split('/')
            index = int(parts[2])
            del produtos[index]
            self._set_response()
            self.wfile.write("Produto removido com sucesso.".encode('utf-8'))


# CONFIGURAÇÃO DO SERVIDOR
port = 8080
server_address = ('', port)

# CRIAR SERVIDOR HTTP
httpd = socketserver.TCPServer(server_address, MyHandler)

# MENSAGEM DE RETORNO
print(f'Servidor rodando na porta {port}')

# INICIAR SERVIDOR
httpd.serve_forever()