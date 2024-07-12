# dontpad.com/ralflima
# IMPORTAÇÕES
import http.server
import socketserver
import json

# LISTA DE PRODUTOS
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