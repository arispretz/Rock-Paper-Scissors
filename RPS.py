# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        prev_play = 'R'

    opponent_history.append(prev_play)
    prediction = 'P'

    if len(opponent_history) > 4:
        last_five = "".join(opponent_history[-5:])
        play_order[last_five] = play_order.get(last_five, 0) + 1
        
        potential_plays = [
            "".join([*opponent_history[-4:], i]) 
            for i in ['R', 'P', 'S']
        ]

        sub_order = {
            j: play_order[j]
            for j in potential_plays if j in play_order
        }

        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    return ideal_response[prediction]
