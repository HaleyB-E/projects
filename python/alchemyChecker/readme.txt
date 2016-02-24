This script was part of a (much) larger original project - a weekend-long, 50-person live-action roleplaying game set in a steampunk/Lovecraftian England.

One part of the game involved a number of players attempting to re-discover the underlying theory behind the construction of Wards - geometrical figures filled with alchemical symbols. The objective was to make sure any of the three gamemasters could quickly and accurately tell players whether the Wards they constructed were valid (and what in-game effect the valid Wards would have).

Some of the logic is likely a bit abstruse absent the context of the game world and the giant spreadsheet that produced the Ward difficulty, in-game effect balancing, etc. but fundamentally the way this works is:

1. The user inputs the elements they want to check. 
2. The script returns whether or not every possible type of ward succeeds and why any failures occur (this was added near the end of the game to allow GMs to give players more detailed feedback when things weren't behaving the way they expected, but can be commented out to declutter output).
3. If any valid Wards were formed, the user can choose to see either a quick summary of these wards or a complete mapping of how each valid Ward was created (which elements from the input were used, which properties of the Ward they matched to, etc.)
4. The user can then see which in-game effects any of the created Wards produced - there were two possible cases (with items and without) that produced slightly different effects.
5. The user is prompted to see if another round of testing should occur. If not, the script exits.

This code could probably do with more comments, though this is to some extent ameliorated by the text outputs. Also there are a few things that could make the user experience more pleasant, namely: making it possible to pick from a list instead of typing out everything, ability to quit the script in places other than the end, more verbose error messages for failed wards, and ability to turn "results of every ward" listing on/off within the script. Since the event for which this was written happened about a year ago and we do not have any intention of running the game again, it is unlikely that these improvements will be made unless I get very bored later.