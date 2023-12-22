import os
import requests
from datetime import datetime, timedelta
from zipfile import ZipFile
from github import Github

# Function to download and extract BSE BhavCopy
def download_and_extract_bhavcopy():
    current_date = datetime.now().strftime('%d%m%y')
    base_url = "https://www.bseindia.com/download/BhavCopy/Equity/EQ_ISINCODE_{}.zip"

    for i in range(10):
        date_str = (datetime.now() - timedelta(days=i)).strftime('%d%m%y')
        url = base_url.format(date_str)
        
        response = requests.get(url)
        
        if response.status_code == 200:
            zip_file_path = f"EQ_ISINCODE_{date_str}.zip"
            with open(zip_file_path, 'wb') as f:
                f.write(response.content)

            with ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall()

            os.remove(zip_file_path)
            return True

    return False

# Function to push updated CSV to GitHub
def push_to_github(updated_csv, local_file_path):
    # Replace with your GitHub token and repository information
    github_token = "11321332132121131232313131313132312"
    repository_name = "BSE-BhavCopy"
    file_path = "https://github.com/nikunjbaheti/BSE-BhavCopy.csv"

    g = Github(github_token)
    repo = g.get_repo(repository_name)
    contents = repo.get_contents(file_path)
    
    repo.update_file(contents.path, "Update BSE BhavCopy", updated_csv, contents.sha)

    # Delete local files after pushing to GitHub
    os.remove(local_file_path)

if __name__ == "__main__":
    if download_and_extract_bhavcopy():
        print("BSE BhavCopy downloaded and extracted successfully.")
        
        # Process the CSV file as needed (e.g., read and update data)

        # Example: Assume 'updated_data' is the updated CSV content
        updated_data = "Your updated CSV data here"

        # Save the updated CSV data to a file
        updated_csv_path = "updated_bhavcopy.csv"
        with open(updated_csv_path, "w") as updated_csv_file:
            updated_csv_file.write(updated_data)

        # Push the updated CSV file to GitHub and delete the local files
        push_to_github(updated_csv_path, updated_csv_path)
        print("Updated CSV pushed to GitHub, and local files deleted.")
    else:
        print("BSE BhavCopy not available for the past 10 days.")
