from colorama import init, Fore, Back, Style

# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# from colorama import init
# init(autoreset=True)
# print(Fore.RED + Back.BLACK + 'some red text')
# print("hello")
# print(Fore.RED + Back.BLACK + 'some red text')
# print('automatically back to default color again')

# init(convert=True)
# a = []
# for i in range(10):
#     a.append(Back.WHITE + " ")

# for i in range(10):
#     print(a[i])

# deinit()

# """ 
# prints table of formatted text format options 
# """
# for style in range(8): 
#     for fg in range(30, 38): 
#         s1 = '' 
#         for bg in range(40, 48): 
#             format = ';'.join([str(style), str(fg), str(bg)]) 
#             s1 += '\033[%sm %s \x1b[0m' % (format, format) 
#         print(s1) 
#     print('\n')  

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

# import time
# import os

# size = os.get_terminal_size()

# display_width = size[0]
# display_height = size[1]

# print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "hello".center(display_width)+Style.RESET_ALL)



# colormap = {
#     1: [Back.RED,Back.YELLOW],
#     2: Back.BLACK,
#     9: Back.WHITE
# }

# print(colormap[1][0])
# print(colormap[1][1])
# print(colormap[2])
# print(colormap[9])
# print(Back.RESET)
a= []
for i in range(1):
    a += [Back.BLACK]

print(a[0] + 'yo')
# a[6] = 'O'
# print(a[6])

for i in range(1):
    print(str(i) + a[i] + 'yo',end='')
print(Back.RESET)