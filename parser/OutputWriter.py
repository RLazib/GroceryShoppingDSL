output_file = None

def open_output_file(filename):
    global output_file
    if output_file is None:
        output_file = open(filename, "w+")
    return output_file
    
def get_output():
    global output_file
    return output_file
    
def close_output_file():
    global output_file
    res = output_file.close()
    output_file = None
    return res
    