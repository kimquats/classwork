import sys

def score_file_to_dict():
    """
    Opens the file containing players' scores and enters the information contained within
    into a dictionary containing 
    """
    try:
      with open('scores.txt', 'r') as f:
        scores = f.read()
      scores = scores.split()
    except IOError:
      print "There was an error opening or reading scores.txt. Exiting."
      sys.exit()
    d = {}
    for i in range(len(scores)):
        if scores[i].isalpha():
            player = scores[i]
            d[player] = []
        else:
            d[player].append(int(scores[i]))
    p = sorted(d.keys())
    return d, p

def print_scores(scores, players):
    print "Total points per player:"
    for i in range(len(players)):
      print players[i], ':', sum(scores[players[i]])

def ask_for_scores(scores, players):
    for i in range(len(players)):
        score = 'a'
        while score.translate(None, '-').isdigit() == False:
            try:
              print "How many points did", players[i], "score?",
              score = raw_input()
              scores[players[i]].append(int(score))
            except ValueError:
              print "The score you enter must be an integer. Try again."
    print_scores(scores, players)

def write_to_scores_file(scores, players):
  try:
    with open('scores.txt', 'w') as f:
      for player in players:
        f.write(player)
        f.write("\n")
        for i in range(len(scores[player])):
          f.write(str(scores[player][i]))
          f.write("\n")
  except IOError:
    print "There was an error writing to scores.txt. Exiting (and erasing all of your changes)."
    sys.exit()

scores, players = score_file_to_dict()
print_scores(scores, players)
ask_for_scores(scores, players)
write_to_scores_file(scores, players)
