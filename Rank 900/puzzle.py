def find_goal(array,goal,n,start_row,start_col,index_row,index_col):
    if index_row<0 or index_row >= n or index_col<0 or index_col >= n:
        return
    array[start_row][start_col],array[index_row][index_col] = array[index_row][index_col],array[start_row][start_col]
    if goal == array:
        print(array)
        return
    
    find_goal(array,goal,n,index_row,index_col,index_row-1,index_col)
    find_goal(array,goal,n,index_row,index_col,index_row,index_col+1)
    find_goal(array,goal,n,index_row,index_col,index_row,index_col-1)
    find_goal(array,goal,n,index_row,index_col,index_row+1,index_col)
    
def main():
    array = [[1,5,3],[2,7,4],[2,0,8]]
    goal = [[1,2,3],[4,5,6],[7,8,0]]
    find_goal(array,goal,3,2,1,2,1)


main()