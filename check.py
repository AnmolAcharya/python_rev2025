# neg_val = 0
# pos_val = 1
# zer_val = 2

# new_arr = [neg_val, pos_val, zer_val]

# print(new_arr)

# min_arr = min(new_arr)
# print(min_arr)


str1 = "SAAS"
str2 = "PWWS"

u_str1 = set(str1)
u_str2 = set(str2)

common_str = u_str1.intersection(u_str2)

if not common_str:
    print("NO")
else:
    print("YES")



