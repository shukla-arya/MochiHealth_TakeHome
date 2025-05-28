# MochiHealth_TakeHome
A tool that will help support agents log the mood of the ticket queue throughout the day, and visualize the emotional trend.

## Features
- Selects a mood from a dropdown menu and optionally allows the ability to add a note.
- A bar chart will visually demonstrate the frequency of logged moods for the day.

## Tech Stack
- **Language:** Python  
- **Framework:** Flask  
- **Google Sheets API:** `gspread` and `oauth2client`
- **Visualization:** Plotly
  
## Requirements

```bash
pip install Flask gspread oauth2client plotly pandas

### Link to Deployed Flask App
http://127.0.0.1:5000

### Link to Google Sheet
https://docs.google.com/spreadsheets/d/1JuGb1qrpHZ1C-7Q98seRXxRW-xeHxsMzIPSDoPGHZbI/edit?usp=sharing
