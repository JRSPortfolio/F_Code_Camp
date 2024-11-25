import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history = None, guess_history = None):
    if not hasattr(player, "knn"):
        player.knn = None
        player.opponent_history = []
        player.guess_history = []
        player.model_tresh = np.arange(0, 1000, 20)
        
    if opponent_history is None:
        opponent_history = player.opponent_history
    if guess_history is None:
        guess_history = player.guess_history
    
    opponent_history.append(prev_play)
                        
    if prev_play:
        guess_map = {'R': 1, 'P' : 2, 'S': 3}
        playmap = {'R': {'R': 1, 'P': 0, 'S': 0, 'guesses': guess_map[guess_history[-1]]},
                   'P' : {'R': 0, 'P': 1, 'S': 0, 'guesses': guess_map[guess_history[-1]]},
                   'S' : {'R': 0, 'P': 0, 'S': 1, 'guesses': guess_map[guess_history[-1]]}}
        playanswer = {1 : 'R', 2 : 'P', 3 : 'S'}
        
        if len(opponent_history) <  20:
            guess = guess = ('R', 'P', 'S')[np.random.randint(0, 3)]
            
        elif len(opponent_history) in player.model_tresh:                  
            player.knn = set_knn(opponent_history, guess_history, guess_map)
            pred_play = pd.DataFrame(playmap[prev_play], columns = ['R', 'P', 'S', 'guesses'], index = [0])        
            prediction = player.knn.predict(pred_play)
            guess = playanswer[prediction[0]]   
                    
        else:
            pred_play = pd.DataFrame(playmap[prev_play], columns = ['R', 'P', 'S', 'guesses'], index = [0])        
            prediction = player.knn.predict(pred_play)
            guess = playanswer[prediction[0]]
            
    else:
        guess = ('R', 'P', 'S')[np.random.randint(0, 3)]
       
    guess_history.append(guess)    

    if (len(opponent_history)) == 1000:
        opponent_history.clear()
        guess_history.clear()
        prev_play = None
             
    return guess

def set_knn(opponent_history, guess_history, guess_map):
    data = {'R': [], 'P' : [], 'S' : [], 'guesses' : [], 'answer' : []}

    op_history = [i for i in opponent_history if i]
    g_history = guess_history.copy()
    
    while len(op_history) > len(g_history):
        g_history.pop(0)
    
    for play in op_history[: -1]:
        match play:
            case 'R':
                data['R'].append(1)
                data['P'].append(0)
                data['S'].append(0)
            case 'P':
                data['R'].append(0)
                data['P'].append(1)
                data['S'].append(0)
            case 'S':
                data['R'].append(0)
                data['P'].append(0)
                data['S'].append(1)
                
    for play in op_history[1:]:
        match play:
            case 'R':
                data['answer'].append(2)
            case 'P':
                data['answer'].append(3)
            case 'S':
                data['answer'].append(1)
                
    for guess in g_history[: -1]:
        data['guesses'].append(guess)
        
    df = pd.DataFrame(data, columns = ['R', 'P', 'S', 'guesses', 'answer'])
    df['guesses'] = df['guesses'].map(guess_map)
    
    X = df[['R', 'P', 'S', 'guesses']]
    y = df['answer']
    knn = KNeighborsClassifier(n_neighbors = 4)
    knn.fit(X, y)
    
    return knn


# knn = None

# def player(prev_play, opponent_history = [], guess_history = []):
#     global knn
#     model_tresh = np.arange(0, 1000, 50)
#     opponent_history.append(prev_play)
                        
#     if prev_play:
#         guess_map = {'R': 1, 'P' : 2, 'S': 3}
#         playmap = {'R': {'plays': 1, 'guesses': guess_map[guess_history[-1]]},
#                    'P' : {'plays': 2, 'guesses': guess_map[guess_history[-1]]},
#                    'S' : {'plays': 3, 'guesses': guess_map[guess_history[-1]]}}
#         playanswer = {1 : 'R', 2 : 'P', 3 : 'S'}
        
#         if len(opponent_history) <  50:
#             guess = guess = ('R', 'P', 'S')[np.random.randint(0, 3)]
                        
#         elif len(opponent_history) in model_tresh:                  
#             knn = set_knn(opponent_history, guess_history, guess_map)
#             pred_play = pd.DataFrame(playmap[prev_play], columns = ['plays', 'guesses'], index = [0])        
#             prediction = knn.predict(pred_play)
#             guess = playanswer[prediction[0]]   
                    
#         else:
#             pred_play = pd.DataFrame(playmap[prev_play], columns = ['plays', 'guesses'], index = [0])        
#             prediction = knn.predict(pred_play)
#             guess = playanswer[prediction[0]]
    
#     else:
#         guess = ('R', 'P', 'S')[np.random.randint(0, 3)]

#     guess_history.append(guess)
    
#     if (len(opponent_history)) == 1000:
#         opponent_history.clear()
#         guess_history.clear()
#         prev_play = None

#     return guess

# def set_knn(opponent_history, guess_history, guess_map): 
#     data = {'plays': [], 'guesses' : [], 'answer' : []}

#     op_history = [i for i in opponent_history if i]
#     g_history = guess_history.copy()
    
#     while len(op_history) > len(g_history):
#         g_history.pop(0)
            
#     for play in op_history[: -1]:
#         match play:
#             case 'R':
#                 data['plays'].append(1)
#             case 'P':
#                 data['plays'].append(2)
#             case 'S':
#                 data['plays'].append(3)
                
#     for play in op_history[1: ]:
#         match play:
#             case 'R':
#                 data['answer'].append(2)
#             case 'P':
#                 data['answer'].append(3)
#             case 'S':
#                 data['answer'].append(1)
                
#     for guess in g_history[: -1]:
#         data['guesses'].append(guess)
        
#     df = pd.DataFrame(data, columns = ['plays', 'guesses', 'answer'])
#     df['guesses'] = df['guesses'].map(guess_map)
    
#     X = df[['plays', 'guesses']]
#     y = df['answer']
#     knn = KNeighborsClassifier(n_neighbors = 2)
#     knn.fit(X, y)
    
#     return knn

    
        
