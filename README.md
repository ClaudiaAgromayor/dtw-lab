# Version Control Lab DTW Lab
# By Daniel Aguilera and Claudia Agromayor

Small, hands‑on lab project from Digital Transformation Workshops. It loads a battery dataset from Google Drive, cleans it, plots exploratory charts, and prints a quick statistic for the charge left percentage.

### What’s inside

- Data ingestion from a Google Drive CSV
- Cleaning and basic outlier filtering
- Exploratory visualizations saved to the graphs/ folder
- Simple summary statistic (mean/median/mode)

### Project structure

- main.py — entry point that runs the full workflow
- src/dtw_lab/lab1.py — data utilities (read, clean, visualize, stats)
- graphs/ — generated plots
- tests/ — placeholder for tests

### Setup

Requires Python 3.12.

Install dependencies:

- pip install -e .

### Run

Run the full pipeline:

- python main.py

This will:

- download the CSV from Google Drive
- clean the dataset
- save plots to graphs/
- print the mean charge left percentage

### Outputs

Generated figures:

- graphs/scatter_plots.png
- graphs/boxplots.png
- graphs/histograms.png

### Notes

If you change the Google Drive file id or the dataset schema, update the expected column names in src/dtw_lab/lab1.py accordingly.

### What our group changed

- Updated main.py to compute and print the median charge-left percentage instead of the mean.

### License

See LICENSE.md.
