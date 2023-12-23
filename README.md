# NSE Bhavcopy Fetcher

## Overview

The NSE Bhavcopy Fetcher is a simple tool to automatically fetch the National Stock Exchange (NSE) Bhavcopy data and store it in a Google Sheet. This tool is implemented using Google Apps Script, allowing you to automate the process of updating stock market data in your Google Sheet.

## Features

- Automatically fetches NSE Bhavcopy data for the current date.
- If data for the current date is unavailable, it iterates over the past 10 days to find a valid Bhavcopy.
- Displays the fetched data in a Google Sheet named "NSE BhavCopy."

## Setup Instructions

1. **Google Sheets Setup:**
   - Create a new Google Sheet or use an existing one.
   - Optionally, create a sheet named "NSE BhavCopy" where the fetched data will be displayed.

2. **Google Apps Script Setup:**
   - Open the Google Sheet.
   - Go to "Extensions" -> "Apps Script."
   - Delete any existing code in the script editor and paste the provided script.
   - Save the script.

3. **Run the Script:**
   - In the script editor, run the `fetchData` function by clicking on the play button.
   - Authorize the script to access your Google Sheets.

4. **Optional: Set up Time-Driven Trigger:**
   - In the script editor, click on the clock icon (Triggers).
   - Click on the "+ Add Trigger" button.
   - Choose the `fetchData` function, select the event type (e.g., time-driven), and set the frequency.

Now, your Google Sheet will automatically fetch the NSE Bhavcopy data at the specified intervals.

## Important Note

- Be mindful of any terms of use or restrictions imposed by the NSE on automated data retrieval.
- Ensure that the Bhavcopy URL format provided in the script is up-to-date.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize this README based on additional information about your project, usage instructions, or any other relevant details.
