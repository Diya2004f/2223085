import pandas as pd
def find_absent_straks(attendance_df):
    attendance_df['attendance_date'] = pd.to_datetime(attendance_df['attendance_date'])
    attendance_df = attendance_df.sort_values(by='attendance_date')
    results =[]
    for student_id, group in attendance_df.groupby(student_id):
        absences = group[group['status'] == 'Absent']
        absences_date = absences['attendance_date'].tolist()
        
        start_date = None
        prev_date = None
        count = 0
        
        for data in absences_date:
            if prev_date and (data -prev_date).days == 1:
                count += 1
           
                
                    


