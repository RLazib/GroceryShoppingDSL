from Tokenizer import *
from OutputWriter import *
from Program import Program

def main():
    tokenizer = create_tokenizer("input.txt")
    open_output_file("output.txt")
    close_output_file()
    program = Program()
    program.parse()
    tokenizer.destroy_tokenizer()
    

if __name__ == "__main__":
    main()