output_file = None

def open_output_file(filename):
    global output_file
    if output_file == None:
        output_file = open(filename, "w+")
    return output_file
    
def get_output_file():
    return output_file
    
def close_output_file():
    return output_file.close()
    