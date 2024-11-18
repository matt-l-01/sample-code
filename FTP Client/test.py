msg = "Claro che si cnnc (123,123,123,123,123,123)"
msg = msg[msg.index('(')+1:msg.index(')')]
lst = msg.split(',')
print(msg)
print(lst)

# Change string into integer
#
# @param str: The string to convert
# @return: The integer value of the string
def toInt(str: str):
    try:
        return int(str)
    except ValueError:
        return None

            