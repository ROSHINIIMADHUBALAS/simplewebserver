from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>Device details</title>
        <body align="center"bgcolor="lavender">

            <h2>Roshinii madhubala-26007010</h2>
            <h3>My laptop configurations</h3>
            <table border="2" align="center" cellspacing="2 cellpading=2">
                <tr align="center">
                    <th>S.no</th>
                    <th>Device type</th>
                    <th>Device info</th>
                </tr>
                <tr>
                    <td>1</td>
                    <td>Device name</td>
                    <td>TL15-53M-G2</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Processor</td>
                    <td>Intel(R) Core(TM) 5 210H (2.20)GHz</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Installed ram</td>
                    <td>16.0 GB (15.7 GB usable)</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Graphic card</td>
                    <td>Intel(R) Graphics (128 MB)</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Storage</td>
                    <td>119 GB of 477 GB used</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td>Device ID</td>
                    <td>D2CB5340-7E03-4BB2-BC38-E14508B0FF20</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td>Product ID</td>
                    <td>00342-42954-11336-AAOEM</td>
                </tr>
            </table>
        </body>
    </head>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()