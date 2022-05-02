from algorithmML import Algorithms as Algo
if __name__ == "__main__":
    truthValue = True
    print("Please enter the name of an image (.png, .jpg) with its extension.")
    imgStr = str(input())
    algorithms = "k_means,color_detection,bit_masking"
    algorithms = algorithms.split(",")
    for count, algorithm in enumerate(algorithms):
        print(count, algorithm)
    while truthValue: 
        algoInt = int(input("\nEnter the number of the algorithm you want to use: "))
        imgToRead = Algo.readImage(imgStr, algoInt)
        try:
            if algoInt == 0:
                Algo.Kmeans(imgToRead)
            elif algoInt == 1:
                Algo.Cdetect(imgToRead)
            elif algoInt == 2:
                Algo.Bmask(imgToRead)
            else:
                raise ValueError("Invalid integer entered, enter 0, 1, or 2.")
        except ValueError:
            print("Invalid value entered, enter another value: ")
            algoStr = int(input())
        contStr = input("Continue typing algorithms? (Y/N): ")
        if contStr.upper() == "Y":
            continue
        print("Bye...")
        break



