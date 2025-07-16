# import string
# import random
# if __name__ == "__main__":
#     S1 = string.ascii_lowercase
#     # print(S1)

#     S2 = string.ascii_uppercase
#     # print(S2)

#     S3 = string.digits
#     # print(S3)

#     S4 = string.punctuation
#     # print(S4)

#     plen = int(input("Enter the length of password:\n"))
    

#     S = []
#     S.extend(list(S1))
#     S.extend(list(S2))
#     S.extend(list(S3))
#     S.extend(list(S4))

#     # print(S)
#     random.shuffle(S)
#     # print(S)
# <<<<<<< HEAD
#     print("Your Password Are:")
# =======
#     print("Your Password is:")
# >>>>>>> 141684ef065607d23c37324540d8cfaf80c3d3b2
#     print("".join(S[0:plen]))




import string
import random

if __name__ == "__main__":
    S1 = string.ascii_lowercase
    S2 = string.ascii_uppercase
    S3 = string.digits
    S4 = string.punctuation

    plen = int(input("Enter the length of password:\n"))

    S = []
    S.extend(list(S1))
    S.extend(list(S2))
    S.extend(list(S3))
    S.extend(list(S4))

    random.shuffle(S)

    print("Your Password is given :")
    print("".join(S[:plen]))
