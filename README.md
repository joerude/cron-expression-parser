## Technical Task - Cron Expression Parser

Write a command line application or script which parses a cron string and expands each field to show the times at which
it will run. You may use whichever language you feel most comfortable with.
You should only consider the standard cron format with five time fields (minute, hour, day of month, month, and day of
week) plus a command, and you do not need to handle the special time strings such as "@yearly". The input will be on a
single line.
The cron string will be passed to your application as a single argument.

```bash
~$ your-program ＂*/15 0 1,15 * 1-5 /usr/bin/find＂
```

The output should be formatted as a table with the field name taking the first 14 columns and the times as a
space-separated list following it.

For example, the following input argument:

```bash
*/15 0 1,15 * 1-5 /usr/bin/find
```

Should yield the following output:

```
minute 0 15 30 45 
hour 0 
day of month 1 15 
month 1 2 3 4 5 6 7 8 9 10 11 12 
day of week 1 2 3 4 5 
command /usr/bin/find
```

Cron format supports multiple input types :

```
- 5     : a fixed value
- 5-10  : a range
- */5   : a frequency
- 5,7   : a list of values 
```

**Note**: Please email your completed project as a zipped attachment to careers@vertex.kg with subject line “Technical
task - Your name”. You should spend no more than three hours on this exercise. If you do not have time to handle all
possible cron strings then an app which handles a subset of them correctly is better than one which does not run or
produces incorrect results.

You should see your project reviewer as a new team member you are handing the project over to. Provide everything you
feel would be relevant for them to ramp up quickly, such as **unit/acceptance tests**, a README and instructions for how
to
run your project in a clean macOS/Linux environment.


## Launch the app

1. Clone the repository:
```bash
git clone https://github.com/joerude/cron-expression-parser.git
```