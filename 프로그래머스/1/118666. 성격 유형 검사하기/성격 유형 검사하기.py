def solution(survey, choices):
    answer = ''
    
    survey_dict = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0,
    }
    
    for i, choice in enumerate(choices):
        if choice < 4:
            survey_dict[survey[i][0]] += 4 - choice
        elif choice > 4:
            survey_dict[survey[i][1]] += choice - 4
        
    if survey_dict['R'] >= survey_dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if survey_dict['C'] >= survey_dict['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if survey_dict['J'] >= survey_dict['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if survey_dict['A'] >= survey_dict['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer