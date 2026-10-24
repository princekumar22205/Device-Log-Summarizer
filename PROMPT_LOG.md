# AI Prompt Log --- Device Log Summarizer

## 1. Initial Prompt

> Write a Python script named `temperature_chart.py` that reads the
> aggregated device data from `summary.json`, extracts each device's ID
> and average temperature, and creates a Matplotlib bar chart comparing
> average temperatures by device. Add a chart title and axis labels,
> save the chart as `temperature_chart.png`, and handle a missing or
> invalid JSON file and an empty dataset gracefully.

## 2. Bug or Formatting Issue Identified During Review

The chart must remain readable when device IDs are long or several
devices are included. A formatting issue to check in the initial draft
is whether the x-axis labels overlap or are cut off, and whether the
chart layout leaves enough room for the labels and title.

**Record the issue that you actually observed in your first generated
version before submitting.** For example, if the labels overlapped,
state that the x-axis labels were difficult to read because they were
horizontal or too close together. Do not claim a bug that was not
present in your version.

## 3. Follow-up Prompt

> Please fix the chart-formatting issue identified during review. Rotate
> the x-axis device labels so they are easier to read, align the labels
> neatly, and adjust the layout to prevent the labels or title from
> being cut off. Keep the chart title and axis labels, save the result
> to `temperature_chart.png`, and retain the error handling for missing
> or invalid JSON and empty data.

## 4. Changes to Check in the Final Script

-   Read `summary.json` and extract `device_id` and
    `average_temperature`.
-   Create a bar chart with a descriptive title and labeled axes.
-   Rotate and align x-axis labels when needed to improve readability.
-   Use `tight_layout()` to reduce the risk of labels being clipped.
-   Save the chart as `temperature_chart.png`.
-   Handle missing/invalid JSON and an empty result set without an
    unhandled exception.

## 5. Verification

After running the scripts, verify the following and update this section
with the result:

-   [ ] Run `main.py` to create `summary.json` from the sample
    `device_telemetry.csv`.
-   [ ] Run `temperature_chart.py` successfully.
-   [ ] Confirm that `temperature_chart.png` is created and displays the
    device IDs and their average temperatures.
-   [ ] Check that labels, title, and axes are readable and not cut off.
-   [ ] Confirm that devices with average temperatures above `80.0` are
    absent from the JSON and chart.
