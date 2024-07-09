Certainly! If you can't use Conda on your university machine, you can set up a virtual environment using Python's built-in venv module and pip. Here's an alternative approach:

1. First, ensure you have Python installed on your machine. You can check this by running:

   ```
   python --version
   ```

2. Clone the repository as before:

   ```
   git clone https://github.com/hasan1292/mDDPM.git
   cd mDDPM
   ```

3. Create a virtual environment using venv:

   ```
   python -m venv mDDPM_env
   ```

4. Activate the virtual environment:
   
   On Windows:
   ```
   mDDPM_env\Scripts\activate
   ```
   
   On Unix or MacOS:
   ```
   source mDDPM_env/bin/activate
   ```

5. Install the required packages using pip:

   ```
   pip install -r requirements.txt
   ```

   Note: If the environment.yml file contains some Conda-specific packages, you might need to find and install their pip equivalents manually.

6. If there are any issues with specific packages, you may need to install them individually or find alternative packages that are compatible with your system.

This approach should work on most systems where you have Python installed but can't use Conda. Remember to activate the virtual environment each time you want to work on this project.

If you encounter any specific package installation issues, let me know and I can provide more targeted advice.