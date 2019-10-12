from Tokenizer import *
from OutputWriter import *
from Program import Program

def main():
    tokenizer = create_tokenizer("input.txt")
    open_output_file("output.txt")
    program = Program()
    program.parse()
    program.evaluate()
    close_output_file()
    tokenizer.destroy()
    

if __name__ == "__main__":
    main()