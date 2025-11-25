import pandas as pd

def calculate_parameters(data: pd.DataFrame) -> dict:
    """
    Calculate the parameters for the Naive Bayes model.
    
    Args:
        data: pd.DataFrame - the dataframe containing the data
        
    Returns:
        dict - a dictionary containing the parameters for the Naive Bayes model
    """
    
    dict = {
        # P(E=1) and P(E=0)
        "e_1": -1,
        "e_0": -1,
        
        # P(P=1|E=1) and P(P=1|E=0) and all other combinations of P and E
        "p_1_given_e_1": -1,
        "p_1_given_e_0": -1,
        "p_0_given_e_1": -1,
        "p_0_given_e_0": -1,
        
        # P(S=1|E=1) and P(S=1|E=0) and all other combinations of S and E
        "s_1_given_e_1": -1,
        "s_1_given_e_0": -1,
        "s_0_given_e_1": -1,
        "s_0_given_e_0": -1,
        
        # P(A=1|E=1) and P(A=1|E=0) and all other combinations of A and E
        "a_1_given_e_1": -1,
        "a_1_given_e_0": -1,
        "a_0_given_e_1": -1,
        "a_0_given_e_0": -1,
        
        # P(H=1|E=1) and P(H=1|E=0) and all other combinations of H and E
        "h_1_given_e_1": -1,
        "h_1_given_e_0": -1,
        "h_0_given_e_1": -1,
        "h_0_given_e_0": -1,
    }
    
    # Calculate P(E=1) and P(E=0)
    num_students_e_1 = data[data["exam_score"] == 1].shape[0]
    num_students_e_0 = data[data["exam_score"] == 0].shape[0]
    dict["e_1"] = num_students_e_1 / data.shape[0]
    dict["e_0"] = num_students_e_0 / data.shape[0]
    
    # Calculate P(P=1|E=1) and P(P=1|E=0) and all other combinations of P and E
    num_students_p_1_given_e_1 = data[(data["exam_score"] == 1) & (data["previous_scores"] == 1)].shape[0]
    num_students_p_1_given_e_0 = data[(data["exam_score"] == 0) & (data["previous_scores"] == 1)].shape[0]
    num_students_p_0_given_e_1 = data[(data["exam_score"] == 1) & (data["previous_scores"] == 0)].shape[0]
    num_students_p_0_given_e_0 = data[(data["exam_score"] == 0) & (data["previous_scores"] == 0)].shape[0]
    
    dict["p_1_given_e_1"] = num_students_p_1_given_e_1 / num_students_e_1
    dict["p_1_given_e_0"] = num_students_p_1_given_e_0 / num_students_e_0
    dict["p_0_given_e_1"] = num_students_p_0_given_e_1 / num_students_e_1
    dict["p_0_given_e_0"] = num_students_p_0_given_e_0 / num_students_e_0
    
    # Calculate P(S=1|E=1) and P(S=1|E=0) and all other combinations of S and E
    num_students_s_1_given_e_1 = data[(data["exam_score"] == 1) & (data["sleep_hours"] == 1)].shape[0]
    num_students_s_1_given_e_0 = data[(data["exam_score"] == 0) & (data["sleep_hours"] == 1)].shape[0]
    num_students_s_0_given_e_1 = data[(data["exam_score"] == 1) & (data["sleep_hours"] == 0)].shape[0]
    num_students_s_0_given_e_0 = data[(data["exam_score"] == 0) & (data["sleep_hours"] == 0)].shape[0]
    
    dict["s_1_given_e_1"] = num_students_s_1_given_e_1 / num_students_e_1
    dict["s_1_given_e_0"] = num_students_s_1_given_e_0 / num_students_e_0
    dict["s_0_given_e_1"] = num_students_s_0_given_e_1 / num_students_e_1
    dict["s_0_given_e_0"] = num_students_s_0_given_e_0 / num_students_e_0
    
    # Calculate P(A=1|E=1) and P(A=1|E=0) and all other combinations of A and E
    num_students_a_1_given_e_1 = data[(data["exam_score"] == 1) & (data["attendance_percent"] == 1)].shape[0]
    num_students_a_1_given_e_0 = data[(data["exam_score"] == 0) & (data["attendance_percent"] == 1)].shape[0]
    num_students_a_0_given_e_1 = data[(data["exam_score"] == 1) & (data["attendance_percent"] == 0)].shape[0]
    num_students_a_0_given_e_0 = data[(data["exam_score"] == 0) & (data["attendance_percent"] == 0)].shape[0]
    
    dict["a_1_given_e_1"] = num_students_a_1_given_e_1 / num_students_e_1
    dict["a_1_given_e_0"] = num_students_a_1_given_e_0 / num_students_e_0
    dict["a_0_given_e_1"] = num_students_a_0_given_e_1 / num_students_e_1
    dict["a_0_given_e_0"] = num_students_a_0_given_e_0 / num_students_e_0
    
    # Calculate P(H=1|E=1) and P(H=1|E=0) and all other combinations of H and E
    num_students_h_1_given_e_1 = data[(data["exam_score"] == 1) & (data["hours_studied"] == 1)].shape[0]
    num_students_h_1_given_e_0 = data[(data["exam_score"] == 0) & (data["hours_studied"] == 1)].shape[0]
    num_students_h_0_given_e_1 = data[(data["exam_score"] == 1) & (data["hours_studied"] == 0)].shape[0]
    num_students_h_0_given_e_0 = data[(data["exam_score"] == 0) & (data["hours_studied"] == 0)].shape[0]
    
    dict["h_1_given_e_1"] = num_students_h_1_given_e_1 / num_students_e_1
    dict["h_1_given_e_0"] = num_students_h_1_given_e_0 / num_students_e_0
    dict["h_0_given_e_1"] = num_students_h_0_given_e_1 / num_students_e_1
    dict["h_0_given_e_0"] = num_students_h_0_given_e_0 / num_students_e_0
    
    return dict

def extract_terms(parameters: dict, e: int, p: int, s: int, a: int, h: int):
    """
    For a specific value e, return the terms used for the naive bayes calculation.
    
    Args:
        parameters: dict - the parameters for the Naive Bayes model
        e: int - exam_score
        p: int - previous_scores
        s: int - sleep_hours
        a: int - attendance_percent
        h: int - hours_studied
        
    Returns:
        dict - a dictionary containing the terms
    """
    
    dict = {
        "e_term": -1,
        "p_term": -1,
        "s_term": -1,
        "a_term": -1,
        "h_term": -1,
    }
    
    if e == 1:
        dict["e_term"] = parameters["e_1"]
        dict["p_term"] = parameters["p_1_given_e_1"] if p == 1 else parameters["p_0_given_e_1"]
        dict["s_term"] = parameters["s_1_given_e_1"] if s == 1 else parameters["s_0_given_e_1"]
        dict["a_term"] = parameters["a_1_given_e_1"] if a == 1 else parameters["a_0_given_e_1"]
        dict["h_term"] = parameters["h_1_given_e_1"] if h == 1 else parameters["h_0_given_e_1"]
    else:
        dict["e_term"] = parameters["e_0"]
        dict["p_term"] = parameters["p_1_given_e_0"] if p == 1 else parameters["p_0_given_e_0"]
        dict["s_term"] = parameters["s_1_given_e_0"] if s == 1 else parameters["s_0_given_e_0"]
        dict["a_term"] = parameters["a_1_given_e_0"] if a == 1 else parameters["a_0_given_e_0"]
        dict["h_term"] = parameters["h_1_given_e_0"] if h == 1 else parameters["h_0_given_e_0"]
    
    return dict
    
def probability_of_performance(parameters: dict, e: int, h: int, s: int, a: int, p: int) -> float:
    """
    Calculate the probability of a student's performance on the final exam given the parameters and the evidence.
    
    Args:
        parameters: dict - the parameters for the Naive Bayes model
        e: int - exam_score
        h: int - hours_studied
        s: int - sleep_hours
        a: int - attendance_percent
        p: int - previous_scores
        
    Returns:
        int - the predicted performance of the student
    """
    if e == 1:
        numerator_terms = extract_terms(parameters, 1, p, s, a, h)
        denominator_terms = extract_terms(parameters, 0, p, s, a, h)
        
    elif e == 0:
        numerator_terms = extract_terms(parameters, 0, p, s, a, h)
        denominator_terms = extract_terms(parameters, 1, p, s, a, h)
        
    numerator = numerator_terms["e_term"] * numerator_terms["p_term"] * numerator_terms["s_term"] * numerator_terms["a_term"] * numerator_terms["h_term"]
    
    denominator = numerator + denominator_terms["e_term"] * denominator_terms["p_term"] * denominator_terms["s_term"] * denominator_terms["a_term"] * denominator_terms["h_term"]
    
    return numerator / denominator

def calculate_individual(parameters: dict, factor: str) -> float:
    """
    Calculate P(E=1 | factor=1) using Bayes' theorem for a single factor.
    
    Args:
        parameters: dict - the parameters for the Naive Bayes model
        factor: str - the factor to calculate the probability for ("p", "s", "a", or "h")
        
    Returns:
        float - the probability P(E=1 | factor=1)
    """
    
    
    e_1 = parameters["e_1"]
    e_0 = parameters["e_0"]
    
    if factor == "p":
        term1 = parameters["p_1_given_e_1"]
        term2 = parameters["p_1_given_e_0"]
    elif factor == "s":
        term1 = parameters["s_1_given_e_1"]
        term2 = parameters["s_1_given_e_0"]
    elif factor == "a":
        term1 = parameters["a_1_given_e_1"]
        term2 = parameters["a_1_given_e_0"]
    elif factor == "h":
        term1 = parameters["h_1_given_e_1"]
        term2 = parameters["h_1_given_e_0"]
    else:
        raise ValueError("Invalid factor")
    
    return (term1*e_1) / (term1*e_1 + term2*e_0)