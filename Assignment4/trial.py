try:
    filename = input("Enter the filename: ")
    
    with open(filename, "r",encoding="utf-8") as file:
        data = file.read()

    modified_data = data.upper()
    with open("output.txt", "w",encoding="utf-8") as firstfile:
        firstfile.write(modified_data)
        
    print("File written successfully."+filename+"")
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
