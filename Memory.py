#!/usr/bin/env python3

data = {
    1 : {
        1 : 2,
        2 : 2,
        3 : 3,
        4 : 4
    },
    2 : {
        1 : '4',
        2 : 'pos_1',
        3 : 1,
        4 : 'pos_1'
    },
    3 : {
        1 : 'label_2',
        2 : 'label_1',
        3 : 3,
        4 : '4'

    },
    4 : {
        1 : 'pos_1',
        2 : 1,
        3 : 'pos_2',
        4 : 'pos_2'
    },
    5 : {
        1 : 'pos_1',
        2 : 'pos_2',
        3 : 'pos_3',
        4 : 'pos_4',
    }
}

levels = eval(input())

#Fix off by one errors
levels.insert(0,[])
for level in levels:
    level.insert(0, None)
positions = [None]
labels = [None]

#last is prompt, others are buttons
pin = ""
for i in range(1,len(levels)):
    stage = data[i]
    prompt = levels[i][-1]

    solution = stage[prompt]

    if type(solution) is int:
        pin += str(levels[i][solution])
        positions.append(solution)
        labels.append(levels[i][solution])

    elif 'pos' in solution:
        stage_position = int(solution[-1])
        pin += str(levels[i][positions[stage_position]])
        positions.append(positions[stage_position])
        labels.append(positions[stage_position])

    elif 'label' in solution:
        stage_position = int(solution[-1])
        pin += str(labels[stage_position])
        positions.append(levels[i].index(stage_position))
        labels.append(stage_position)

    else:
        pin += str(solution)
        labels.append(solution)
        positions.append(levels[i].index(int(solution)))

print(pin)
# [[1,3,2,4,1],[3,1,2,4,3],[2,3,4,1,2],[2,1,4,3,1],[4,1,2,3,4]]
