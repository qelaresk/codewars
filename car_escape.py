def escape(carpark):
    '''
    03.04.2019 Fatma Coskunfirat
    Input : Car place in List
    Output: Direction to escape from car place in List   
    '''
    # Link: https://www.codewars.com/kata/591eab1d192fe0435e000014

    result = []
    row    = len(carpark[0])
    column = len(carpark)
    weare = -1                                              # initialize weare       

    for j in range(0,column):
        stair = -1                                          #initialize stair each floor
        for i in range(0,row):
            if carpark[j][i] == 1:
                stair = i
            elif carpark[j][i] == 2:
                weare = i
        if weare == -1:                                      # if not find current floor,continue
            continue
        if stair == -1:
            if weare == row - 1:
                break
            direction = 'R' + str(row-weare-1)
            result.append(direction)  
            break
        if stair < weare:
            direction = 'L'+ str(weare-stair)
            result.append(direction) 
        elif stair > weare:
            direction = 'R'+ str(stair-weare)
            result.append(direction)
        temp_down = result[-1]                               #each floor checking how we need to get down 
        if temp_down[0] == 'R' or temp_down[0] == 'L':
            direction = 'D1'
            result.append(direction)
        else:
            direction = 'D' + str(int(temp_down[1]) + 1)
            result[-1] = direction 
        weare = stair                                        #after get down we are same position with stair
   
    return result

if __name__ == '__main__':
    carpark = [[0, 2, 0, 0, 1],
               [0, 0, 0, 0, 1],
               [0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0]]
    print(escape(carpark))

            