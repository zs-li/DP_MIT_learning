import numpy as np


def badness(text_length,i,j,col_width):
    current_length = 0
    for k in range(i,j+1):
        current_length += text_length[k]
    if current_length>col_width:
        badness_value =float("inf")
    else:
        badness_value=pow((col_width-current_length),3)
    # print(badness_value)
    return badness_value


if __name__=='__main__':
        text_length=[2,5,2,3,11,10,7,7,5,7,1,5,2,7,10,12,9,2,2,7,10,9,3,4,2,7,3,7,5,12,2,1,11,6,2,6,2,3,10]  #N=39
        col_width=57
        N=len(text_length)
        DP=np.zeros(N)
        DP[N-1]=0
        for i in range(N-2,-1,-1):
            # count how much j fits
            j_list=[]
            j=i+1
            while True:
                if j<=N-1 and sum(text_length[i+1:j+1])<col_width: # text_length[i+1:j+1]=text_length[i+1,i+1,...,j]
                    j_list.append(j)
                    j += 1
                else:
                    break

            # last_break=j
            # while True:
            #     if j<=last_break and sum(text_length[i+1:last_break])<col_width:
            #         j_list.append(j)
            #         j+=1
            #     else:
            #         last_break=i
            #         break
            # construct list of badness+DP
            temp_DPlist = []
            for j in j_list:
                # print(badness(text_length,i,j,col_width),DP[j])
                temp_DPlist.append( badness(text_length,i,j,col_width)+DP[j] )
            DP[i]=min(temp_DPlist)

            print(i,DP[i])

        # print result
        now_badness = 0
        for i in range(N):
            output = ''
            for k in range(text_length[i]):
                output += '*'
            output += ' '
            print(str(output), end="")
            if DP[i]<now_badness: # LINE BREAKING
                print()
                now_badness=0
            else:
                now_badness = DP[i] # in the line




