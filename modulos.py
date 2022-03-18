def acmTeam(topic):
    # Write your code here
    members = []
    i = 0
    while i < len(topic)-1:
        j = i+1
     #   print(topi)
        while j < len(topic):
            x = int(topic[i]) + int(topic[j])
            members.append(len(str(x)) - str(x).count("0"))
            j += 1
        i += 1
    return [max(members), members.count(max(members))]

topic = ["10101", "11100", "11010", "00101"]
print(acmTeam(topic))