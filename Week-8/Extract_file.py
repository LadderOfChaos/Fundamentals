file = input().split("\\")

last = file[-1].split(".")

print(f'File name: {last[0]}\nFile extention: {last[1]}')