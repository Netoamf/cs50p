user_input = input("File name: ").strip().lower()

if user_input.endswith(".jpg") or user_input.endswith(".jpeg"):
    print("image/jpeg")
elif user_input.endswith(".png"):
    print("image/png")
elif user_input.endswith(".gif"):
    print("image/gif")
elif user_input.endswith(".pdf") or user_input.endswith(".txt"):
    print("text file")
elif user_input.endswith(".zip"):
    print("zip file")
else:
    print("application/octet-stream")