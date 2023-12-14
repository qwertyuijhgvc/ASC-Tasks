msg = "Agklq ldhum qom ndem, Gembqgax c 4-hmqqmk vdke. Hddp mumkxvomkm. Ycxim gq'l umkx diugdsl"
msg = msg.upper()
alphabet = ["A","B","C","D","E","F","H","I","J","K","L","M","N","O","P","Q","R","X","T","U","V","W","X","Y","Z"]
for x in range (len(alphabet)):
    count = 0
    for i in range (len(msg)):
        if msg[i] == alphabet[x]:
            count = count + 1
        #end if
    #next
    print(alphabet[x], count)
#next