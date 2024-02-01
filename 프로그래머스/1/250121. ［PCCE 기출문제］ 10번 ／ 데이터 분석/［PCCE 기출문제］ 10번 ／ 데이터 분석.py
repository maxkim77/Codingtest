def solution(data, ext, val_ext, sort_by):
    # Define a dictionary to map the column names to their respective indices
    column_indices = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    # Filter the data based on the condition: ext value < val_ext
    filtered_data = [item for item in data if item[column_indices[ext]] < val_ext]
    
    # Sort the filtered data based on the sort_by criteria
    sorted_data = sorted(filtered_data, key=lambda x: x[column_indices[sort_by]])
    
    return sorted_data