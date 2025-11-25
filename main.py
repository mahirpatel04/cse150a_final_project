from calculations import calculate_parameters, probability_of_performance, calculate_individual
from preprocess import read_data, clean_data, preprocess, save_data, ProcessingType
import os

def main():
    """
    Main function to run the program.
    """
    for processing_type in ProcessingType:
        data = read_data("student_exam_scores.csv")
        cleaned_data = clean_data(data)
        processed_data = preprocess(cleaned_data.copy(), processing_type)
        save_data(processed_data, "processed_data.csv")
    
        parameters = calculate_parameters(processed_data)
        
        output = f"Processing Type: {processing_type.value.upper()}. Which means the threshold to binarize the each column will be {processing_type.value.upper()} of the data.\nIf the value is greater than the threshold, it will be converted to 1, otherwise 0." + "\n"
        
        output += "="*60 + "\n"
        output += "CONDITIONAL PROBABILITIES WITH MULTIPLE EVIDENCE" + "\n"
        output += "="*60 + "\n"
        
        # All factors positive
        prob_1_all_1 = probability_of_performance(parameters, 1, 1, 1, 1, 1)
        prob_0_all_1 = probability_of_performance(parameters, 0, 1, 1, 1, 1)
        output += f"\nGiven: H=1, S=1, A=1, P=1 (All factors positive)" + "\n"
        output += f"  P(E=1 | H=1, S=1, A=1, P=1) = {prob_1_all_1:.4f} ({prob_1_all_1*100:.2f}%)" + "\n"
        output += f"  P(E=0 | H=1, S=1, A=1, P=1) = {prob_0_all_1:.4f} ({prob_0_all_1*100:.2f}%)" + "\n"
        
        # All factors negative
        prob_1_all_0 = probability_of_performance(parameters, 1, 0, 0, 0, 0)
        prob_0_all_0 = probability_of_performance(parameters, 0, 0, 0, 0, 0)
        output += f"\nGiven: H=0, S=0, A=0, P=0 (All factors negative)" + "\n"
        output += f"  P(E=1 | H=0, S=0, A=0, P=0) = {prob_1_all_0:.4f} ({prob_1_all_0*100:.2f}%)" + "\n"
        output += f"  P(E=0 | H=0, S=0, A=0, P=0) = {prob_0_all_0:.4f} ({prob_0_all_0*100:.2f}%)" + "\n"
        
        output += "\n" + "="*60 + "\n"
        output += "INDIVIDUAL FACTOR PROBABILITIES" + "\n"
        output += "="*60 + "\n"
        
        attribute_names = {
            "p": "Previous Scores",
            "s": "Sleep Hours",
            "a": "Attendance",
            "h": "Hours Studied"
        }
        attribute_probabilities = {
            "p": -1,
            "s": -1,
            "a": -1,
            "h": -1,
        }
        for attribute in attribute_probabilities.keys():
            individual = calculate_individual(parameters, attribute)
            attr_upper = attribute.upper()
            attribute_probabilities[attribute] = individual
            
            output += f"  P(E=1 | {attr_upper}=1) [{attribute_names[attribute]:20s}] = {individual:.4f} ({individual*100:.2f}%)" + "\n"
        
        factor_to_name = {
            "p": "Previous Scores",
            "s": "Sleep Hours",
            "a": "Attendance",
            "h": "Hours Studied"
        }
        
        highest_probability = max(attribute_probabilities.values())
        highest_probability_attribute = max(attribute_probabilities.keys(), key=attribute_probabilities.get)
        
        lowest_probability = min(attribute_probabilities.values())
        lowest_probability_attribute = min(attribute_probabilities.keys(), key=attribute_probabilities.get)
        
        
        # Insights
        
        output += "--------------------------------" + "\n"
        output += "INSIGHTS" + "\n"
        output += "--------------------------------" + "\n"
        output += f"The factor that most strongly predicts a successful exam is {factor_to_name[highest_probability_attribute]} with a probability of {highest_probability:.4f} ({highest_probability*100:.2f}%)" + "\n"
        output += f"The factor that least strongly predicts a successful exam is {factor_to_name[lowest_probability_attribute]} with a probability of {lowest_probability:.4f} ({lowest_probability*100:.2f}%)" + "\n"
        
        
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, "output")
        output_path = os.path.join(output_dir, f"{processing_type.value}.txt")
        
        os.makedirs(output_dir, exist_ok=True)
        with open(output_path, "a") as file:
            file.write(output)
        

if __name__ == "__main__":
    main()