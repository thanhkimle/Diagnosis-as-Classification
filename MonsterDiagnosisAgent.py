from itertools import combinations
import numpy as np

class MonsterDiagnosisAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    def solve(self, diseases, patient):
        # Add your code here!
        #
        # The first parameter to this method is a list of diseases, represented as a
        # list of 2-tuples. The first item in each 2-tuple is the name of a disease. The
        # second item in each 2-tuple is a dictionary of symptoms of that disease, where
        # the keys are letters representing vitamin names ("A" through "Z") and the values
        # are "+" (for elevated), "-" (for reduced), or "0" (for normal).
        #
        # The second parameter to this method is a particular patient's symptoms, again
        # represented as a dictionary where the keys are letters and the values are
        # "+", "-", or "0".
        #
        # This method should return a list of names of diseases that together explain the
        # observed symptoms. If multiple lists of diseases can explain the symptoms, you
        # should return the smallest list. If multiple smallest lists are possible, you
        # may return any sufficiently explanatory list.

        disease_names = []
        updated_symptoms = []
        # convert disease's level from +/0/- to 1/0/-1
        for disease, symptoms in diseases.items():
            disease_names.append(disease)
            updated_levels = []
            for vitamin, level in symptoms.items():
                if level == "+":
                    updated_levels.append(1)
                if level == "0":
                    updated_levels.append(0)
                if level == "-":
                    updated_levels.append(-1)
            
            updated_symptoms.append(updated_levels)
        
        # convert patient's level from +/0/- to 1/0/-1
        updated_patient = []
        for vitamin, level in patient.items():
            if level == "+":
                updated_patient.append(1)
            if level == "0":
                updated_patient.append(0)
            if level == "-":
                updated_patient.append(-1)
        # convert list to numpy array
        updated_patient = np.asarray(updated_patient)
        
        # get the number of diseases
        n = len(disease_names)
        # get the number of vitamins
        m = len(updated_patient)    
        # assume the max number of diseases that a patient could get is 6
        for r in range(1,7,1):
            # generate all test cases per r number of diseases
            cases = list(combinations(range(n), r))
            # print(cases)
            for case in cases:
                # print(case)
                curr_symptoms = np.zeros(m)
                names = []
                # loop through each diease and add the level
                for disease in case:
                    curr_symptoms = np.add(curr_symptoms, updated_symptoms[disease])
                    names.append(disease_names[disease])
                # normalize the combined levels
                for idx in range(len(curr_symptoms)):
                    if curr_symptoms[idx] > 0:
                        curr_symptoms[idx] = 1
                    if curr_symptoms[idx]  < 0:
                        curr_symptoms[idx] = -1
                # check if the test case generated match with the paitent symptoms
                if (curr_symptoms == updated_patient).all():
                    return names

        return None

