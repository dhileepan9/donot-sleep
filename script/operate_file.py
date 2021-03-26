from datetime import datetime

def create_filename():
    dt_obj = datetime.strptime(str(datetime.now()),
                           '%Y-%m-%d %H:%M:%S.%f')
    millisec = dt_obj.timestamp() * 1000
    filename = "donotsleep-"+str(millisec)
    f = open(filename, "x")
    return filename

def write_file(filename):
    f = open(filename, "a")
    f.write("Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto")
    f.close()