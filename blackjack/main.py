import random
import functions
import art

def random_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return cards[random.randint(0, len(cards)-1)]

def deal_cards():
  dealt = []
  for _ in range(2):
    dealt.append(random_card())
  return dealt

def output(dealers_hand, players_hand, show_card):
  print(f"Dealer\'s {show_hand(dealers_hand, show_card)}")
  print(f"Your {show_hand(players_hand)}")

def show_hand(hand, show_card=False):
  if show_card:
    return f"cards: [{hand[0]}, *]"
  return f"cards: {hand}"

def get_total(hand):
  total = 0
  for ix in range(len(hand)):
    if hand[ix] == 11 and (total + hand[ix]) > 21:
      hand[ix] = 1
    total += hand[ix]
  return total

def over_twenty_one(hand):
  total = get_total(hand)
  if total > 21:
    return True
  return False

# Start of Game
restart_game = False
default_win = False

while not restart_game:
  dealer_hand = deal_cards()
  player_hand = deal_cards()
  pass_turn = False
  functions.clear()
  print(art.logo)

  # Player's turn
  while not pass_turn:
    print("\n")
    output(dealer_hand, player_hand, True)
    another_card = input("Type \'y\' to get another card, type \'n\' to pass: ").lower()

    if another_card == 'y':
      print("\tHit me!")
      player_hand.append(random_card())
      if over_twenty_one(player_hand):
        pass_turn = True
        default_win = True
    else:
      print("\tI'm good!")
      pass_turn = True

  # Dealer's turn
  pass_turn = False
  while not pass_turn and not default_win:
    print("\n")
    output(dealer_hand, player_hand, False)

    if get_total(dealer_hand) < 18:
      dealer_hand.append(random_card())
      print(f"\tDealer takes a card.")
      if over_twenty_one(dealer_hand):
        pass_turn = True
    else:
      pass_turn = True

  print("\n\n** Final Cards **\n")
  output(dealer_hand, player_hand, False)
  dealer_total = get_total(dealer_hand)
  player_total = get_total(player_hand)

  if player_total > 21:
    print("---\nYou went over 21. Dealer wins.")
  elif dealer_total > 21:
    print("---\nDealer went over 21. You win.")
  else:
    if player_total > dealer_total:
      print("---\nYou win.")
    elif player_total == dealer_total:
      print("---\nIt's a tie. Dealer wins.")
    else:
      print("---\nDealer wins.")

  # restarting the game
  restart = input("\nDo you want to play again? (y/n) ").lower()
  if restart == "n":
    print("Goodbye.")
    restart_game = True