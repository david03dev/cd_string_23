def verify_usernames(n, usernames):
    seen_usernames = {}
    res = ""
    for username in usernames:
        if username not in seen_usernames:
            seen_usernames[username] = 1
            res = res + "Verified" + " "
        else:
            new_username = f"{username}{seen_usernames[username]}"
            seen_usernames[username] += 1
            res = res + new_username + " "

    print(res.strip())

# Sample Input
n = input()
usernames = list(input().split(" "))

# Function Call
verify_usernames(n, usernames)






"""Guvi developed a new system to make sure no two usernames are same. 
So, they hired you as a developer to develop this system. 
They have set some rules to do the same.
If you see the same username that already exists, just add a number at the end of that username ,else print "Verified".

Input Description:
First line consists of an integer N, denoting number of usernames. Second line consists of N spaced separated Strings, denoting usernames.

Output Description:
print the required output in a new line.

Sample Input :
4
abc aab abc aba

Sample Output :
Verified Verified abc1 aba"""
