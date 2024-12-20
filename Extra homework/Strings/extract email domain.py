# email = input("Enter your email address: ")
# extract = ""
#
# for i in range(len(email)):
#     if email[i] == "@":
#         i += 1
#         while i <= len(email)-1:
#             extract += email[i]
#             i += 1
#
# print(extract)

email = input("Enter your email address: ")
extract = ""


at_index = email.find('@')

if at_index != -1:

    extract = email[at_index + 1:]

print(extract)
