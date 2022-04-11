#converting data cleaning process code into a function
def process_results(data):
    nested_values = ['video', 'author','music','shareCover','challenges','duetInfo','textExtra', 'stickersOnItem','stats','authorStats']
    skip_values = ['shareCover','challenges','duetInfo','textExtra', 'stickersOnItem']

        #create blank dictionary
    flattened_data = {}
    #looping through each video
    for idx, value in enumerate(data):
        flattened_data[idx] = {}
        #looping through each property in each video
        for prop_idx, prop_value in value.items():
            #check if nested
            if prop_idx in nested_values:
                if prop_idx in skip_values:
                    pass
                else:
                    #loop through each nested property
                    for nested_idx, nested_value in prop_value.items():
                        flattened_data[idx][prop_idx+'_'+nested_idx] = nested_value  
            #if its not nested, add it back to the flattened dictionary        
            else:
                flattened_data[idx][prop_idx] = prop_value
                
    return flattened_data