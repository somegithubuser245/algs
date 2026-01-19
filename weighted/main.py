import random

threes = [
[
    0, 1, 1, 1, 0,
    0, 0, 0, 1, 0,
    0, 0, 1, 1, 0,
    0, 0, 0, 1, 0,
    0, 1, 1, 1, 0
],
[
    0, 1, 1, 1, 0,
    0, 0, 0, 1, 0,
    0, 0, 1, 1, 0,
    0, 0, 1, 1, 0,
    1, 1, 1, 0, 0
],
[
    0, 1, 1, 1, 0,
    1, 1, 0, 1, 0,
    0, 0, 1, 1, 1,
    0, 0, 0, 1, 0,
    0, 1, 1, 1, 0
],
]

not_threes = [
    [
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, -1
    ],
    [
        1, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 1, -1
    ],
    [
        0, 0, 1, 1, 0,
        0, 0, 0, 1, 0,
        0, 0, 0, 1, 0,
        0, 0, 0, 1, 0,
        0, 0, 0, 1, 0, -1
    ]
]


def get_delta_weights(inputs, model_result, training_result):
    if model_result == training_result:
        return [0 for _ in range(ARR_LENGTH)]
    
    delta_weights = [NU * input_value * (training_result - model_result) for input_value in inputs]
    return delta_weights

def update_weigths(model_weights, delta_weights):
    result = []
    for model_weight, delta_weight in zip(model_weights, delta_weights):
        result.append(model_weight + delta_weight)

    return result

def get_prediction(input, weights):
    return 1 if sum([input[i] * weights[i] for i in range(ARR_LENGTH)]) >= 0 else 0
    


NU = 0.5
ARR_LENGTH = 26

EPOCHS = 3
# bias bit
[three.append(1) for three in threes]

random = random.Random()
weights = [0 for _ in range(len(threes[0]) + 1)]


for _ in range(EPOCHS):
    for three, not_three in zip(threes, not_threes):
        # model_result = get_prediction(not_three, weights)
        # delta_weights = get_delta_weights(not_three, model_result, 0)
        # weights = update_weigths(weights, delta_weights)
        
        model_result = get_prediction(three, weights)
        delta_weights = get_delta_weights(three, model_result, 1)
        weights = update_weigths(weights, delta_weights)




print(weights)

rand_three = [
    1, 1, 1, 1, 0,
    0, 0, 0, 1, 0,
    0, 1, 1, 1, 0,
    0, 0, 1, 1, 0,
    0, 1, 1, 1, 0, 1
]

not_three = [
    0, 0, 1, 1, 0,
    0, 0, 0, 1, 0,
    0, 0, 0, 1, 0,
    0, 0, 0, 1, 0,
    0, 0, 0, 1, 1, 1
]

seven = [
    0, 1, 1, 1, 1,
    0, 0, 0, 1, 0,
    0, 0, 1, 0, 0,
    0, 1, 0, 0, 0,
    0, 1, 0, 0, 0, 1
]

one = [
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    1, 0, 0, 0, 0,
    1, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 1
]

print(get_prediction(seven, weights))
        

