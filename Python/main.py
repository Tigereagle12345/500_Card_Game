import random

num = ""
suite = ""
card_format = "\n________________\n| {}              |\n|                |\n|                |\n|       {}        |\n|                |\n|                |\n|              {} |\n|________________|\n".format(num, suite, num)

print("Starting...")

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

player1_hand = []
player2_hand = []
player3_hand = []
player4_hand = []
def deal():
  print("Dealing...")
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
    num = str(i[0])
    suite = str(i[1])
    if suite == "s":
      suite = "spades"
      
    elif suite == "c":
      suite = "clubs"
      
    elif suite == "d":
      suite = "diamonds"
      
    elif suite == "h":
      suite = "hearts"
    
    card = card_data[suite]["cards"][num]
    card_color = card_data[suite]["color"]
    
    #print("\nYour hand:\n\n" + card_form)
    
  return player1_hand
  #print(kitty)
  #print(player1_hand)
  #print(player2_hand)
  #print(player3_hand)
  #print(player4_hand)
hand = deal()
