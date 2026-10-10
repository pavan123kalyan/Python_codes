n=67
res = ""
while n > 0:
    res = str(n % 2) + res
    n //= 2
print(res)
# def to_binary(n):
#     return bin(n)[2:]

#java
# public static String toBinary(int n) {
#     StringBuilder sb = new StringBuilder();
#     while (n > 0) {
#         sb.append(n % 2);
#         n /= 2;
#     }
#     return sb.reverse().toString();
# }

# public static String toBinary(int n) {
#     return Integer.toBinaryString(n);
# }

