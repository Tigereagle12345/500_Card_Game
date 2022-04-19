import random

players = ["player1", "player2", "player3", "player4"]

card_data = {
  "spades": {
    "color": "black", "cards": {
      "5": {"name": "5 of Spades"},
      "6": {"name": "6 of Spades"},
      "7": {"name": "7 of Spades"},
      "8": {"name": "8 of Spades"},
      "9": {"name": "9 of Spades"},
      "10": {"name": "10 of Spades"},
      "q": {"name": "Queen of Spades"},
      "k": {"name": "King of Spades"},
      "a": {"name": "Ace of Spades"},
      "j": {"name": "Jack of Spades"},
      }
    },
  "clubs": {
    "color": "black", "cards": {
      "5": {"name": "5 of Clubs"},
      "6": {"name": "6 of Clubs"},
      "7": {"name": "7 of Clubs"},
      "8": {"name": "8 of Clubs"},
      "9": {"name": "9 of Clubs"},
      "10": {"name": "10 of Clubs"},
      "q": {"name": "Queen of Clubs"},
      "k": {"name": "King of Clubs"},
      "a": {"name": "Ace of Clubs"},
      "j": {"name": "Jack of Clubs"},
      }
    },
  "diamonds": {
    "color": "red", "cards": {
      "4": {"name": "4 of Diamonds"},
      "5": {"name": "5 of Diamonds"},
      "6": {"name": "6 of Diamonds"},
      "7": {"name": "7 of Diamonds"},
      "8": {"name": "8 of Diamonds"},
      "9": {"name": "9 of Diamonds"},
      "10": {"name": "10 of Diamonds"},
      "q": {"name": "Queen of Diamonds"},
      "k": {"name": "King of Diamonds"},
      "a": {"name": "Ace of Diamonds"},
      "j": {"name": "Jack of Diamonds"},
      }
    },
  "hearts": {
    "color": "red", "cards": {
      "4": {"name": "4 of Hearts"},
      "5": {"name": "5 of Hearts"},
      "6": {"name": "6 of Hearts"},
      "7": {"name": "7 of Hearts"},
      "8": {"name": "8 of Hearts"},
      "9": {"name": "9 of Hearts"},
      "10": {"name": "10 of Hearts"},
      "q": {"name": "Queen of Hearts"},
      "k": {"name": "King of Hearts"},
      "a": {"name": "Ace of Hearts"},
      "j": {"name": "Jack of Hearts"}
      }
    }
}
cards = [
  "5s", "6s", "7s", "8s", "9s", "10s", "qs", "ks", "as", "js",
  "5c", "6c", "7c", "8c", "9c", "10c", "qc", "kc", "ac", "jc",
  "4d", "5d", "6d", "7d", "8d", "9d", "10d", "qd", "kd", "ad", "jd",
  "4h", "5h", "6h", "7h", "8h", "9h", "10h", "qh", "kh", "ah", "jh",
  "joker"
]

kitty = []
bid = []

player1_hand = []
player2_hand = []
player3_hand = []
player4_hand = []
player_hand = []
def deal(dealer):
    if dealer == players[3]:
        dealer = players[0]
    else:
        dealer = players[int(dealer[6]) + 1]
    #print(dealer)
    print(str(dealer) + " is dealing...\n")
    for i in range(10):
        card = random.choice(cards)
        player1_hand.append(card)
        cards.remove(card)
    
        card = random.choice(cards)
        player2_hand.append(card)
        cards.remove(card) 
    
        card = random.choice(cards)
        player3_hand.append(card)
        cards.remove(card) 
    
        card = random.choice(cards)
        player4_hand.append(card)
        cards.remove(card) 
    
        if i == 3 or i == 6 or i == 9:
            card = random.choice(cards)
            kitty.append(card)
            cards.remove(card)
    
    for i in player1_hand:
        if str(i[1]) == "0":
            suite = str(i[2])
            num = str("10")
        else:
            suite = str(i[1])
            num = str(i[0])
        #print(i)
        #print(suite)
        #print(num)
        if suite == "s":
            suite = "spades"
      
        elif suite == "c":
            suite = "clubs"
        
        elif suite == "d":
            suite = "diamonds"
      
        elif suite == "h":
            suite = "hearts"
    
        if i == "joker":
            card = "Joker"
            #print(card)
        else:
            card = card_data[str(suite)]["cards"][str(num)]["name"]
        player_hand.append(card)
    
    print("Your hand: \n")
    for card in player_hand:
        print(card)
    
    return dealer

def bid_hand(bidder):
  if bidder == "player2":
    hand = player2_hand
  elif bidder == "player3":
    hand = player3_hand
  elif bidder == "player4":
    hand = player4_hand
  return hand
  
def bid_ai(bidder):
  hand = bid_hand(bidder)
  for card in hand:
    if str(i[1]) == "0":
            suite = str(i[2])
            num = str("10")
        else:
            suite = str(i[1])
            num = str(i[0])
        if suite == "s":
            suite = "spades"
        elif suite == "c":
            suite = "clubs"
        elif suite == "d":
            suite = "diamonds"
        elif suite == "h":
            suite = "hearts
        elif suite == "o":
          suite = ""
          
  
def ask_bid():
    bid = input("Please place a bid (format as number before suite, with 10 as t. Example 7 Hearts would be 7h. Misere and Open Misere should be written as m and om, respectivly ):\n")
    return bid

def bid(first_bid):
    bids = ["6s", "6c", "6d", "6h", "7s", "7c", "7d", "7h", "8s", "8c", "8d", "8h", "9s", "9c", "9d", "9h", "ts", "tc", "td", "th", "m", "om"]
    trumps = ""
        
    if first_bid == "player1":
        current_bid = ask_bid()
        if current_bid in bids:
            bid.append(current_bid)
        else:
            print("Invalid Bid, Please Try Again.")
            bid_dealer(first_bid)
    else:
      bid_ai(first_bid)
        
    return trumps

dealer = "player4"
dealer = deal(dealer)
if dealer == players[3]:
    first_bid = players[0]
else:
    first_bid = players[int(dealer[6]) + 1]
trumps = bid(first_bid)
