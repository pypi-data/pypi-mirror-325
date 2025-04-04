#!/bin/bash

cd .. 

# Define the repository URL and the target directory
REPO_URL="https://github.com/apple/ml-depth-pro.git"
TARGET_DIR="depthProSrc"  # You can change this if you want a different name

# Check if the target directory already exists
if [ -d "$TARGET_DIR" ]; then
  echo "Target directory '$TARGET_DIR' already exists.  Please remove it or choose a different name."
  exit 1
fi

# Clone the repository (this is the most efficient way to get the source)
git clone "$REPO_URL" "$TARGET_DIR"

# Navigate into the cloned directory
cd "$TARGET_DIR"

# Sparse checkout to only get the 'src' directory (and its contents)
git config core.sparsecheckout true
echo "src/*" >> .git/info/sparse-checkout # Specify the path to include
git checkout main  # Or whatever branch you need. Replace 'main' if needed.

# (Optional) Remove the .git directory if you only need the source code and not the git history.
#  Be very sure you want to do this as you will lose all git information.
#  If you want to keep the .git directory, skip the next two lines.
#rm -rf .git

echo "Successfully downloaded the 'src' directory to '$TARGET_DIR'."

# (Optional) If you want to only have the src directory and nothing else
# You can remove all other files and directories from the cloned repo
# except the src directory. Be *very* careful with this.
#rm -rf *  # Remove everything
#mkdir src_only  # Create a new directory
#mv src src_only  # Move src into it
#cd src_only  # Change to new directory
#echo "Successfully extracted only the 'src' directory into 'src_only'"
#ls -l #List the contents of the directory
#exit 0

exit 0 # Successful completion