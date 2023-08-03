# The skills required for the job, and the candidate's skills are stored in sets.
# Complete the program to output the matched skill.

skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}


print(list(skills & job_skills)[0])


