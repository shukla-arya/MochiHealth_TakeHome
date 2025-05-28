from flask import Flask, render_template, request, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, date
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

app = Flask(__name__)

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Mood Logger").sheet1

MOODS = {
    "Frustrating": "Frustrating",
    "Joyful": "Joyful",
    "Confusing": "Confusing",
    "Sad": "Sad",
    "Satisfaction": "Satisfaction",
    "Hopeful": "Hopeful",
    "Distress": "Distress"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mood = request.form["mood"]
        note = request.form.get("note", "")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([timestamp, mood, note])
        return redirect("/")

    # Read all data
    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    # Filter for today
    if not df.empty:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df_today = df[df["timestamp"].dt.date == date.today()]
        mood_counts = df_today["mood"].value_counts()
    else:
        mood_counts = pd.Series()

    # Create bar chart with Plotly
    fig = go.Figure([go.Bar(x=mood_counts.index, y=mood_counts.values)])
    fig.update_layout(title="Mood Count Today", xaxis_title="Mood", yaxis_title="Count")
    plot_div = pyo.plot(fig, output_type="div")

    return render_template("index.html", plot_div=plot_div, moods=MOODS)

if __name__ == "__main__":
    app.run(debug=True)