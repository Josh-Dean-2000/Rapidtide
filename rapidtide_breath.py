# python C:\Users\Joshua\Documents\Research\Paper\rapidtide_breath.py
# Junction created for OneDriveNU <<===>> OneDrive - Northwestern University

import os
# dir_path = os.chdir('C:\Users\Joshua\OneDriveNU\Euskalibur')
cwd = os.getcwd()
os.chdir(cwd)
print("Current working directory is:", cwd)

#Determine the start time of running this python script
from datetime import datetime
from pytz import timezone
start_time = datetime.now(timezone('America/Chicago'))
start_time = start_time.strftime("%H-%M-%S")

#Make a new text file to write to which subjects/sessions errors occurred in
f = open("C:/Users/Joshua/OneDriveNU/Euskalibur/derivatives/rapidtide/Errors_" + start_time + ".txt", 'w')
f.write('Errors occurred in these subjects/sessions:\n')
f.close()

#subjects = ["sub-006"]  # "sub-001", "sub-002", "sub-003", "sub-004", "sub-006","sub-007", "sub-008", "sub-009", "sub-010" 
#data_types = ["ses-02"] # "ses-02", "ses-03"
subjects = ["sub-001", "sub-002", "sub-003", "sub-004", "sub-007", "sub-008", "sub-009"]  #Removed 5, 6, and 10
data_types = ["ses-02", "ses-03"]
for s in subjects:
    for d in data_types:
        try:
            input_file = "C:/Users/Joshua/OneDriveNU/Euskalibur/raw_data/" + s + "/" + d + "/" + "00." + s + "_" + d + "_task-breathhold_optcom_bold_native_preprocessed.nii.gz"
            output_prefix = "C:/Users/Joshua/OneDriveNU/Euskalibur/derivatives/rapidtide/" + s + "/" + d + "/" + s + "_" + d + "_task-breathhold_optcom"
            rapidtide_command = "python " + "C:/Users/Joshua/anaconda3/Scripts/rapidtide" + " " + input_file + " " + output_prefix + " " \
                '--globalmeaninclude "C:/Users/Joshua/OneDriveNU/Euskalibur/raw_data/' + s + "/" + s + '_GM_eroded.nii.gz:2 " --refineinclude "C:/Users/Joshua/OneDriveNU/Euskalibur/raw_data/' + s + "/" + s + "_GM_eroded.nii.gz:2 " + \
                        '--delaymapping --autosync --datatstep 1.5 --detrendorder 3 --oversampfac 5 --passes 3 --despecklepasses 4 --filterband lfo' + " " + \
                            '--searchrange -15 15 --pickleft --nolimitoutput --spatialfilt -1'
            print(rapidtide_command)
            os.system(rapidtide_command) #not sure why we need line 14&15? <--I think it's to actually run the command that was printed
        except:
            #Write a text file that says which subject and data type didn't work
            #NOTE: this doesn't work yet because the error isn't in python, it encounters it in the command prompt. That is, regardless of what the code is doing, this script successfully copied and entered the command, so it never gets to the except component.
            with open("C:/Users/Joshua/OneDriveNU/Euskalibur/derivatives/rapidtide/Errors_" + start_time + ".txt", 'a') as new_lines:
                new_lines
                line1 = '\n'
                line2 = 'subject: ' + subjects + '\n'
                line3 = 'session: ' + data_types + '\n'
                line4 = '\n'
                new_lines.writelines([line1, line2, line3, line4])
            #pass







# THE OG RAPIDTIDE COMMAND
# rapidtide \
#     C:\Users\Joshua\Documents\Research\rapidtide\data\test1\00.sub-007_ses-02_task-breathhold_optcom_bold_native_preprocessed_brain.nii.gz \
#     C:\Users\Joshua\Documents\Research\rapidtide\data\test1\sub-007_ses-02_task-breathhold_optcom \
#     --globalmeaninclude C:\Users\Joshua\Documents\Research\rapidtide\data\test1\sub-007_GM_eroded.nii.gz:1 \
#     --refineinclude C:\Users\Joshua\Documents\Research\rapidtide\data\test1\sub-007_GM_eroded.nii.gz:1 \
#     --delaymapping \
#     --autosync \
#     --datatstep 1.5 \
#     --detrendorder 3 \
#     --oversampfac 5 \
#     --passes 3 \
#     --despecklepasses 4 \
#     --filterband lfo \
#     --searchrange -15 15 \
#     --pickleft \
#     --nolimitoutput \
#     --spatialfilt -1
