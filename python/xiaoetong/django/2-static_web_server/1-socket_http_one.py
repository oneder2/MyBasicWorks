import socket

if __name__ == '__main__':
    # create tcp server socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set port release
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # bind a ip address && port no
    tcp_server_socket.bind(("", 9000))
    # set listener
    tcp_server_socket.listen(128)

    while True:
        # wait for connection request from client-end
        new_socket, ip_port = tcp_server_socket.accept()
        # connection success, accept information
        recv_client_data = new_socket.recv(4096)
        # sent binary data to client-end
        recv_client_content = recv_client_data.decode('utf-8')
        print(recv_client_content)

        with open('templates/server_http.html', 'rb') as file:
            file_data = file.read()

        # response line
        response_line = 'HTTP/1.1 200 OK\r\n'
        # response head
        response_header = 'Server:PWS1.0\r\n'
        # response_body
        response_body = file_data

        # response reporter（响应报文）
        response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
        new_socket.send(response_data)

        new_socket.close()




