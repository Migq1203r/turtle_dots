# 🐢 Turtle Dot Painting (Hirst Style) 

This project uses **Python Turtle Graphics** to create a colorful dot painting inspired by Damien Hirst’s artwork.
Instead of extracting colors from an image at runtime, this version uses a **predefined RGB color palette**, making it easier to run in most local environments.

⚠️ **Note:**
Even though `colorgram` is imported in the file header (from the original lesson), it is **not required** for this version because the colors are already defined in `rgb_colors`.

## Features

* Uses Python’s built-in `turtle` module
* Draws a grid of evenly spaced colored dots
* Random color selection from a predefined RGB palette
* Fast rendering using maximum turtle speed
* Beginner-friendly graphics project

## Requirements

* Python 3.x
* `turtle` (included with standard Python installations)

No external libraries are required for this version.

## How It Works

1. A list of RGB color tuples (`rgb_colors`) is predefined.
2. The turtle starts at the left side of the screen.
3. Each row:

   * Draws 10 dots
   * Moves forward after each dot
4. After finishing a row, the turtle “teleports” upward to start the next row.
5. The process repeats until the full grid is completed.
6. Clicking the window closes the program.

## Running the Code

Run the script locally with:

```bash
python main.py
```

Click anywhere on the Turtle window to exit when the drawing is complete.

## Code Behavior Notes

* `turtle.colormode(255)` allows the use of RGB values.
* `turtle.speed(0)` sets the fastest drawing speed.
* `timmy.dot(20)` is used instead of drawing lines for clean circular dots.
* `teleport()` is used to jump between rows without drawing lines.

## License

This project is licensed under the **GNU General Public License v3.0**.

You are free to:

* Use the code
* Modify it
* Share it
* Distribute derivative works

As long as all copies and derivatives remain under the **GPL v3 license**.

📄 Full license text:
[https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)
