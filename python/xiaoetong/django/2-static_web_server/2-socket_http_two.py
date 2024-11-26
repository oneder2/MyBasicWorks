import socket


def main():
    # create tcp server socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set port release
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # bind a ip address && port no
    tcp_server_socket.bind(("", 8703))
    # set listener
    tcp_server_socket.listen(128)

    while True:
        # wait for connection request from client-end
        new_socket, ip_port = tcp_server_socket.accept()
        # connection success, accept information
        recv_client_data = new_socket.recv(4096)
        if len(recv_client_data) == 0:
            new_socket.close()
        
        # sent binary data to client-end
        recv_client_content = recv_client_data.decode('utf-8')
        print(recv_client_content)

        request_list = recv_client_content.split(" ", maxsplit=2)
        request_path = request_list[1]
        if request_path == '/':
            request_path = '/index.html'

        try:
            with open('templates' + request_path, 'rb') as file:
                file_data = file.read()
        except Exception as e:
            # if request path is wrong
            response_line = 'HTTP/1.1 404 Not Found\r\n'
            response_header = 'Server:PWS1.0\r\n'
            with open('templates/error.html', 'rb') as file:
                file_data = file.read()
            response_body = file_data

            # response message（响应报文）
            response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
            new_socket.send(response_data)
        else:
            # if request path is correct
            response_line =  'HTTP/1.1 200 OK\r\n'
            response_header = 'Server:PWS1.0\r\n'
            response_body = file_data
            response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
            new_socket.send(response_data)
        finally:
            new_socket.close()






if __name__ == '__main__':
    main()
