import time, ds18x20, onewire

def read_temp():
    
    ow = onewire.OneWire(Pin(4))
    ds = ds18x20.DS18X20(ow)
    read_data = ds.scan()
    ds.convert_temp()
    time.sleep_ms(750)

    result = []

    for f in read_data:
        #print(ds.read_temp(f))
        result.append(ds.read_temp(f))

    return result

def web_page():
   
    html = """{"sensors": [{ "temperature": """+str(read_temp()[0])+ """},{"temperature": """+str(read_temp()[1])+"""}]}"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Received HTTP GET connection request from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('GET Rquest Content = %s' % request)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        #conn.send('Content-Type: text/html\n')
        conn.send('Content-Type: application/json\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')