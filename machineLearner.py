from algorithmML import Algorithms as algo
if __name__ == "__main__":
    truthValue=True
    print("Please enter the name of an image (.png, .jpg) with its extension.")
    imgStr = str(input())
    algorithms = "k_means,color_detection,bit_masking"
    algorithms = algorithms.split(",")
    for count, algorithm in enumerate(algorithms):
        print(count, algorithm)
    while truthValue: 
        algoStr = int(input("\nPlease enter which algorithm to utilize, enter the number beside the algorithm in the list above: "))
        try:
            if(algoStr == 0):
                algo.Kmeans(imgStr)
            elif(algoStr == 1):
                algo.Cdetect(imgStr)
            elif(algoStr == 2):
                algo.Bmask(imgStr)
            else:
                raise Exception("Invalid integer entered, please only enter 0, 1, or 2.")
        except Exception:
            print("Invalid value entered, enter another value: ")
            algoStr = int(input())
        contStr = input("Continue typing algorithms? (Y/N): ")
        if contStr.upper() == "Y":
            continue
        print("Bye...")
        break



