# SE-assignment2
This is my second assignment for my Software Engineering class.

## Project Overview
This project is part of the COMP 3322 Software Engineering course, focusing on learning GitHub for version control, collaboration, and conflict resolution. The repository contains a simple "Hello, World!" program that accepts user input and randomly selects a greeting.

## Features
- Basic "Hello, World!" program
- User input for personalized greeting
- Random greeting selection
- Demonstrates Git branching and merging

## Installation Instructions
1. Clone the Repository
```sh 
git clone https://github.com/your-username/SE-assignment2.git
cd SE-assignment2
```
2. Run the Program
```sh
 python hello_world.py
```

## Issues and Resolutions
Issue 1: Merge Conflicts

Problem: A merge conflict occurred while merging feature-2 into main due to simultaneous edits in hello_world.py. Resolution:
```sh
# Identify the conflict
git status

# Open the file and manually resolve the conflict
# Remove conflict markers (<<<<<<<, =======, >>>>>>>)

# Stage and commit the resolved file
git add hello_world.py  
git commit -m "Resolved merge conflict in hello_world.py"  
git push origin main  
```
GitHub’s web interface was also used to resolve the conflict manually.

## Issue 2: Unclear Instructions

Problem: The professor's instructions did not fully align with the merge conflict scenario encountered. Resolution:
Used independent research and GitHub’s conflict resolution tool.
Documented the process for future reference.

## Issue 3: Pushing Rejected Due to Non-Fast-Forward

Problem: Attempting git push origin main resulted in an error due to remote updates. Resolution:
```sh
# Pull the latest changes before pushing
git pull origin main --rebase  
git push origin main  
```
