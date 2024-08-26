# def decode(s):
#     out = []
#     decoder = {"1": "A",
#                "2": "B",
#                "3": "C",
#                "4": "D",
#                "5": "E",
#                "6": "F",
#                "7": "G",
#                "8": "H",
#                "9": "I",
#                "10": "J",
#                "11": "K",
#                "12": "L",
#                "13": "M",
#                "14": "N",
#                "15": "O",
#                "16": "P",
#                "17": "Q",
#                "18": "R",
#                "19": "S",
#                "20": "T",
#                "21": "U",
#                "22": "V",
#                "23": "W",
#                "24": "X",
#                "25": "Y",
#                "26": "Z",
#                }

#     singleWords = ""
#     for i in range(len(s)):
#         es = s[i]
#         if es in decoder:
#             singleWords += decoder[es]
#     if len(singleWords) != 0:
#         out.append(singleWords)

#     # for i in range(0, len(s), 2):
#     #     es = s[i:i+2]
#     #     if es in decoder:
#     #         out.append(decoder[es])

#     for i in range(len(s)):
#         if i < len(s)-1:
#             es = s[i:i+2]
#             print("es -> ", es)
#             if es in decoder:
#                 out.append(decoder[es])

#     print("Decoded str -> ", out)
#     return len(out)

def decode(s):
    decoder = [str(i) for i in range(1, 27)]
    sLen = len(s)
    out = [0] * (sLen + 1)

    out[0] = 1
    for i in range(1, sLen+1):
        if s[i-1] in decoder:
            out[i] += out[i-1]
        if i > 1 and s[i-2:i] in decoder:
            out[i] += out[i-2]
    print(out)
    return out[-1]


encodedStr = "226"
print("Encoded str -> ", encodedStr)
out = decode(encodedStr)
print(out)
