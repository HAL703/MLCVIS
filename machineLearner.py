from algorithmML import Algorithms as algo
if __name__ == "__main__":
    truthValue = True
    print("Please enter the name of an image (.png, .jpg) with its extension.")
    imgStr = str(input())
    algorithms = "k_means,color_detection,bit_masking"
    algorithms = algorithms.split(",")
    print("Please enter which algorithm to utilize, please enter the number beside the algorithm in the list.\n")
    for count, algorithm in enumerate(algorithms):
        print(count, algorithm)
    algoStr = int(input())
    while truthValue: 
        try:
            if(algoStr == 0):
                algo.Kmeans(imgStr)
            elif(algoStr == 1):
                algo.Cdetect(imgStr)
            elif(algoStr == 2):
                algo.Bmask(imgStr)
            else:
                raise Exception
            truthValue=False
        except Exception:
            print("Invalid value entered, enter another value: ")
            algoStr = int(input())


