from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    
    # Создаем SSL контекст
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # Генерируем самоподписанный сертификат
    context.load_cert_chain('server.crt', 'server.key')
    
    # Оборачиваем сервер в SSL
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print("Сервер запущен на порту 8000 (HTTPS)...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
