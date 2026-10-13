# Codeforces Solutions

My Python solutions to Codeforces problems, starting with basic 800-rated problems.

[Codeforces profile](https://codeforces.com/profile/Arnav_Deva)

## Browse the solutions

Each file is a standalone solution. The index below describes the approach used in the existing code.

| Solution | Approach |
| --- | --- |
| [Watermelon](Codeforces/Watermelon.py) | Even-number check with a lower bound |
| [Way to long words](Codeforces/Way%20to%20long%20words.py) | Abbreviate strings longer than ten characters |
| [Team](Codeforces/Team.py) | Count rows where at least two participants agree |
| [Next Round](Codeforces/Next%20Round.py) | Filter positive scores against the kth-place score |
| [DominoPiling](Codeforces/DominoPiling.py) | Compute half the grid area using integer division |
| [Bit++](Codeforces/Bit%2B%2B.py) | Simulate increments and decrements |
| [Petya & strings](Codeforces/Petya%20%26%20strings.py) | Compare lowercase strings lexicographically |
| [Helpful maths](Codeforces/Helpful%20maths.py) | Sort digits and join them with plus signs |
| [word capitalization](Codeforces/word%20capitalization.py) | Capitalize the first character |
| [boy or girl](Codeforces/boy%20or%20girl.py) | Count distinct characters using a set |
| [beautiful matrix](Codeforces/beautiful%20matrix.py) | Compute Manhattan distance to the center |
| [bear and big brother](Codeforces/bear%20and%20big%20brother.py) | Simulate repeated growth until one value exceeds another |
| [ACMSGURU/A+B](Codeforces/ACMSGURU/A%2BB.py) | Read two numbers from a file and write their sum |

## Run a solution

From the repository directory:

```bash
python "Codeforces/Team.py"
```

Enter the problem's input through standard input. Quote filenames that contain spaces.

The ACMSGURU solution uses files instead of standard input:

```bash
cd Codeforces/ACMSGURU
python A+B.py
```

Place the two integers in `input.txt` in the working directory; the script writes their sum to `output.txt`.

Some solutions retain interactive input prompts. The scripts are documented here as committed.
