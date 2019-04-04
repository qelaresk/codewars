def escape(carpark):
    result = []
    row    = len(carpark[0])
    column = len(carpark)
    weare = -1

    print('column: ', column)
    print('row: ', row)

    for j in range(0,column):
        stair = -1
        for i in range(0,row):
            if carpark[j][i] == 1:
                stair = i
            elif carpark[j][i] == 2:
                weare = i
        print('stair: ', stair)
        print('weare: ',weare)
        if weare == -1:
            continue
        if stair == -1:
            if weare == row - 1:
                break
            direction = 'R' + str(row-weare-1)
            result.append(direction)  
            print('Last column:' , result)
            break
        if stair < weare:
            direction = 'L'+ str(weare-stair)
            result.append(direction) 
            print('Left:', result)
        elif stair > weare:
            direction = 'R'+ str(stair-weare)
            result.append(direction)
            print('Right:',result )
        temp_down = result[-1]
        if temp_down[0] == 'R' or temp_down[0] == 'L':
            direction = 'D1'
            result.append(direction)
            print('Down first:', result)
        else:
            direction = 'D' + str(int(temp_down[1]) + 1)
            result[-1] = direction
            print('down multi:', result)
        weare = stair

    return result

if __name__ == '__main__':
    carpark = [[0, 2, 0, 0, 1],
               [0, 0, 0, 0, 1],
               [0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0]]
    print(escape(carpark))

            