# File me data likhna (Write)

# file me likhna
# w = write mode
# f = open("myfile.txt", "w")   
# f.write("Hello, this is my first file!")
# f.close()

# print("Data written successfully!")

# File ka data padhna (Read)

# file ka data padhna
# r = read mode
# f = open("myfile.txt", "r")   
# data = f.read()
# f.close()

# print("File content:")
# print(data)

# File me data add (Append) karna

# existing file me data add karna
# a = append mode
# f = open("myfile.txt", "a") 
# f.write("\nThis line is added later.")
# f.close()

# print("Additional data added!")

# Best method – with open (Auto close)

# Yeh method sabse best hai, file automatically close ho jati hai.
# with open safe method
# with open("myfile.txt", "r") as f:
#     data = f.read()

# print(data)
