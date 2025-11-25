from calculations import calculate_parameters, probability_of_performance
from preprocess import read_data

def main():
    """
    Main function to run the program.
    """
    data = read_data("processed_data.csv")
    parameters = calculate_parameters(data)

    for key, value in parameters.items():
        print(f"{key}: {value}")
        
    print("--------------------------------")
    probability = probability_of_performance(parameters, 1, 1, 1, 1, 1)
    print("--------------------------------")
    print(f"P(E=1 | H=1, S=1, A=1, P=1) = {probability}")
    probability = probability_of_performance(parameters, 0, 1, 1, 1, 1)
    print(f"P(E=0 | H=1, S=1, A=1, P=1) = {probability}")
    probability = probability_of_performance(parameters, 1, 0, 0, 0, 0)
    print(f"P(E=1 | H=0, S=0, A=0, P=0) = {probability}")
    probability = probability_of_performance(parameters, 0, 0, 0, 0, 0)
    print(f"P(E=0 | H=0, S=0, A=0, P=0) = {probability}")

if __name__ == "__main__":
    main()