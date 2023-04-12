# ask user for input // Remove whitespace from str // Capitalize the user's name // pergunta o input do usuario // remove o espaço em branco da string // Letra maiuscula no inicio 
name = input("whats your name? ").strip().title()

# Split user's name into first and last name

first, middle, last = name.split(" ")

# Say hello to user // hello para usuario
print(f"hello, {first}")
#positional parameters
