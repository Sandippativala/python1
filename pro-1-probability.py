# 1).find the probability of it being neither a king nor a spade.

total_cards = 52    #total cards 52
kings = 4           # cards in kings 4
spades =13          # cards in spades 13
k_and_s = 1         #king and spades both 

nokingnospade = total_cards - (kings + spades - k_and_s) # cards in no king and no sapde
probability = nokingnospade / total_cards 

print("probability of drawing a card that if neither a king nor a spade :",probability)