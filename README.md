# Shark_Bot
Project contain 3 files. 

*Image_Clarification.py, clears the underwater image through histogram equilization to restore brightness and colors in the image. 

*"Motor control.py" detects the underwater goal post through template matching and derives the motors to pass the post, it also detects the colors. 

*"temp.py"simply detects goal post and colors. add the image clarification code inside the loop in "Motor control.py" and then use the clarified output to detect template and colors.
