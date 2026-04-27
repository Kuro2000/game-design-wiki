# GDC 2020 — Blockers: Analyzing Difficulty Drivers in Candy Crush Games

**Source**: `GDC2020 Final PPT.pdf` — Lucien Chen, Senior Level Designer at King, GDC 2020.
**Pages**: 71

Text extracted from PDF; layout artifacts may remain. Each `## Page N` corresponds to one slide. Selected pages are also rendered to `wiki/assets/<slug>/page-NN.png` for visual reference.

---

## Page 1

Lucien Chen, Senior Level Designer
Blockers: Analyzing Difficulty Drivers in Candy Crush Games

## Page 2

WHO AM I?
Lucien Chen
Senior Level Designer

## Page 3

3
Ways Of Raising Difficulty
Blockers: analyzing difficulty drivers in candy crush games

## Page 4

BlockersSpawn RateDesign StylesLevel Layout
4
4 Ways of Raising Difficulty
AnalysisDifficultyDriversin Candy Crush Games

## Page 5

5
4 Waysof RaisingDifficulty
Level Layout
Open / NarrowShapes Empty Position
Multi Screens

## Page 6

6
4 Waysof RaisingDifficulty
Design Style
Explosive SnipeyJourney Puzzly Grindy

## Page 7

7
4 Waysof RaisingDifficulty
Design Style
Easy Hard
Explosive SnipeyJourney Puzzly Grindy

## Page 8

• Rate of SpecialCandies,Blocker,or RegularCandies
• Frequencyof ObjectiveSpawning
• Numbersof Candy Color Spawning
8
4 Waysof RaisingDifficulty
Spawn Rate
4 colors 5 colors 6 colors SpecialCandies,Blocker ,or RegularCandies

## Page 9

9
Blockers

## Page 10

10
Hard Core Games
RPG, ARPG, ACT ,D&D…etc

## Page 11

11
What Defines an Enemy?
Hard Core Game
Reference Dungeons and Dragons Next, Wizards of the Coast, & Eternal Poison, Banpresto & Atlus USA

## Page 12

12
Stats Define the Style of Enemies
Hard Core Game
Reference Dungeons and Dragons Next, Wizards of the Coast, & Eternal Poison, Banpresto & Atlus USA

## Page 13

13
What Enemies Do…
• Providevariousgameplayexperience
• Slow Player Progression
• Stop Player to Win the Game
• Increasing the Difficulty
Hard Core Games
Reference Dungeons and Dragons Next, Wizards of the Coast, & Eternal Poison, Banpresto & Atlus USA

## Page 14

14
What Enemies Do…
Blockers
Hard Core Games
Match 3 Games

## Page 15

15
What Blockers Do…
Match3 Games
• Providevariousgameplayexperience
• Slow Player Progression
• Stop Player to Win the Game
• Increasing the Difficulty

## Page 16

16
Blockers = Enemies
Knowledgetransferfrom Hard Core Game to Match3
• Stats for Hard Core Game
• Can we have the same conceptin Match 3 game?
• Can we have Stats for Match 3 game?
Reference Dungeons and Dragons Next, Wizards of the Coast, & Eternal Poison, Banpresto & Atlus USA

## Page 17

17
BLOCKER FRAMEWORK

## Page 18

16 Characteristics
18
The stats define blockers in casual switcher games
Blocker Framework

## Page 19

16 Characteristics
BlockerFramework
19
Colorless
Colored
Layered
Single
Space
Stationary
Removable
Locked
Irremovable
Movable
Match Beside
Match On
Chained
Impenetrable
Hiding
Dynamic

## Page 20

20
16 Characteristics
BlockerFramework
NATURE
Colorless Colored
LayeredSingle
Space
MOVEMENT
Stationary
Locked
Movable
DISCOVERY
Chained
Hiding
Dynamic
DESTRUCTION
RemovableIrremovable
MatchBesideMatchOn
Impenetrable

## Page 21

21
Colorless
 Colored
 Layered
Single
 Space
To remove the 
blocker, players only 
need to do adjacent 
match or explode 
the power-ups once 
to break the 
blocker.
In order to remove 
or damage this 
blocker, players need 
to match the certain 
color of the tiles 
with this blocker or 
to explode power-
ups next to the 
blocker.
Players can remove 
or break this blocker 
with any adjacent 
match or by 
exploding power-ups 
next to the blocker.
A single blocker that 
takes more than 1x1 
space on the board 
from the beginning, 
until it is removed.
In order to remove 
the blocker, players 
need to do adjacent 
match or explode 
power-ups more 
than one time to 
break the blocker.
NATURE

## Page 22

DESTRUCTION
22
In order to break the 
blocker, players need 
to match the candy 
on the top of the 
blocker.
The blockers can be 
removed by adjacent 
matches, exploding 
power-ups during 
the gameplay, or 
fulfill the certain 
condition.
Players are not able 
to remove this 
blocker from the 
board. It stays until 
end of the level.
Break the blocker by 
matches or 
exploding power-
ups, but the blocker 
is able to block the 
power-up effect 
from going through. 
The candies or 
blockers behind are 
not damaged by the 
power-up.
To break the blocker, 
player needs to 
match adjacent 
candies or explode 
the power-ups 
beside the blocker.
Irremovable Removable MatchBesideMatchOn Impenetrable

## Page 23

23
In player’s turn, 
players are able to 
swap the position of 
the blocker with the 
adjacent candy (tile). 
The blocker will fall 
into the empty cells 
in the gravity 
direction.
Blocker can lock a 
candy or a blocker 
inside. Visibility of 
the locked object is 
the difference 
between Hiding and 
Lock.
The blocker cannot 
be moved and it 
does not fall into the 
gravity direction. It is 
tied on the cell to 
the end of the game.
Stationary Locked Movable
MOVEMENT

## Page 24

Discovery
24
The blocker 
performs an action 
after player’s every 
move or several 
moves.
Candy, blocker, or 
objective can be 
hidden under the 
blocker which has 
hidden 
characteristic. The 
item is not able to 
identify until it 
removed.
The set of blockers 
will be affected only 
if the blocker(s) 
reach the certain 
condition.
Chained Hiding Dynamic
DISCOVERY

## Page 25

25
16 Characteristics
Candy Crush Franchise

## Page 26

16 CharacteristicsTable
Candy Crush Soda Saga Blockers
26
Liquorice
Swirl
● ● ● ● ● ●
Liquorice Lock ● ● ● ● ● ● ● ●
Honey ● ● ● ● ● ●
Ice Blocker ● ● ● ● ● ●
Cupcake ● ● ● ● ●
Chainblocker ● ● ● ●
Chainblocker
Lock
● ● ● ● ●
White
Chocolate
● ● ● ● ● ● ●
Chocolate ● ● ● ● ● ● ●
Bubble Gum ● ● ● ● ● ● ● ●
Candy Cane ● ● ● ● ● ● ●
Jelly Cake ● ● ● ● ● ●
Pancake ● ● ● ● ● ●

## Page 27

Destruction
Nature
27
Candy Crush
Saga Blockers
16 CharacteristicsRadar Chart
Discovery
Movement
Colorless Colored
Layered
Single
Space
Stationary
RemovableLocked
Irremovabl
e
Movable
Match
Beside
MatchOn
Chained
Impenetrable
Hiding
Dynamic

## Page 28

28
Candy Crush
Saga Blockers
16 CharacteristicsRadar Chart
• The radar chart shows us the 
general experience of the game 
would feel like.
• This point out areas of opportunity 
when designing new blockers in the 
future.
• You can see there are some 
characteristics are used more often 
in Candy Crush Soda .
Colorless Colored
Layered
Single
Space
Stationary
RemovableLocked
Irremovabl
e
Movable
Match
Beside
MatchOn
Chained
Impenetrable
Hiding
Dynamic

## Page 29

29
Colorless Colored
Layered
Single
Space
Stationary
RemovableLocked
IrremovableMovable
MatchBeside
MatchOn
Chained
Impenetrable
Hiding
Dynamic
Colorless Colored
Layered
Single
Space
Stationary
RemovableLocked
IrremovableMovable
MatchBeside
MatchOn
Chained
Impenetrable
Hiding
Dynamic
Colorless Colored
Layered
Single
Space
Stationary
RemovableLocked
IrremovableMovable
MatchBeside
MatchOn
Chained
Impenetrable
Hiding
Dynamic
Colorless Colored
Layered
Single
Space
Stationary
RemovableLocked
IrremovableMovable
MatchBeside
MatchOn
Chained
Impenetrable
Hiding
Dynamic

## Page 30

30
What We Found
In Comparison

## Page 31

Similarities
31

## Page 32

32
Similarities
Candy FranchiseComparison
• Most common characteristics are Stationary, 
Colorless, Layered, Removable, & Match Beside
• All the low numbersarea are the same areas.

## Page 33

Differences
33

## Page 34

34
Differences
Candy FranchiseComparison
• CCS has more Dynamic,Single &
Movablethan others
• Less Hiding in Franchise
• Focus on Few Directionsof the Radar
• MatchOn > MatchBeside in Jelly

## Page 35

35
Stationary Layered Colorless Removable MatchBeside
The Most Common Characteristics

## Page 36

36
WHY??

## Page 37

37
Gameplay Experience
The purpose of the most common characteristics
Blocker Framework

## Page 38

38
Visual Difference
 Progression 
Based
 Accessibility

## Page 39

39
Visual Difference
What We Found

## Page 40

40
Stationary
•All the candies moves beside blockers, it 
stand out obviously.
Visual
Difference
What We Found
Stationary 
Blockers
Stationary

## Page 41

41
Colorless
•Easier to distinguish between candy and 
none-candy objective.
What We Found
Colorless
Colorless Blockers Colored Blockers
Visual
Difference

## Page 42

42
Layered
•All the candies are removed except the 
blockers with layers. 
What We Found
Layered Blockers
Layered
Visual
Difference

## Page 43

43
Progression Based
What We Found

## Page 44

44
Progression
Based
What We Found
Layered
•Removinglayersgive playerspositive
feedbackto their action.
Layered Blockers
Layered

## Page 45

45
Removable
•Creating more space for better 
matches.
Progression
Based
What We Found
RemovableBlockers
Removable

## Page 46

46
Accessibility
of Reaching out a Blocker
What We Found

## Page 47

47
Accessibility
Of Reaching out
a Blocker
What We Found
Type of Match #
Match 3 6
Match 4 8
Match 5 10
2 x 2 Match 4
Match 6 16
Total 44
Match On

## Page 48

48
What We Found
Match Beside
Type of 
Match
#
Match 3 16
Match 4 20
Match 5 24
2 x 2 Match 8
Match 6 36
Total 104
Accessibility
Of Reaching out
a Blocker

## Page 49

49
What We Found
Type of 
Match
#
Match 3 16
Match 4 20
Match 5 24
2 x 2 Match 8
Match 6 36
Total 104
Type of Match #
Match 3 6
Match 4 8
Match 5 10
2 x 2 Match 4
Match 6 16
Total 44
Match On Match Beside
Accessibility
Of Reaching out
a Blocker

## Page 50

50
Visual Difference
 Progression 
Based
Accessibility
Stationary Layered Colorless Removable MatchBeside

## Page 51

51
Difficulty of Characteristics
What We Found

## Page 52

52
Difficulty of Characteristic
16 Characteristics
LeastDifficult Neutral Most Difficult

## Page 53

53
Difficulty of Characteristic
16 Characteristics
LeastDifficult Neutral Most Difficult

## Page 54

54
Win Rate & Characteristics
What We Found

## Page 55

55
Win Rate & Characteristics
16 Characteristics
Characteristic Distribution of Top 20 Easiest & Hardest Levels
Low win rate High win rate

## Page 56

56
Win Rate & Characteristics
16 Characteristics
Characteristic Distribution of Top 20 Easiest & Hardest Levels
Low win rate High win rate

## Page 57

57
Win Rate & Characteristics
16 Characteristics
Characteristic Distribution of Top 20 Easiest & Hardest Levels
Low win rate High win rate

## Page 58

58
Production Benefit
How the blocker framework help
Blocker Framework

## Page 59

59
Benefits?
BlockerFramework
• Common Language
• EveryoneunderstandBlockers
• A SystematicMethod
• Design Faster
How It Helps
the Production

## Page 60

60
Designers
BlockerFramework
• Shared common language within 
design team = more unified design 
direction.
• Across the studios and projects.
• Looking for inspirationand focus on 
overall game experience.
Designers
to

## Page 61

61
Artists
BlockerFramework
• How characteristic helps artist to 
visualize the blocker idea.
• Easier to visualize the new blocker 
based on the characteristics.
Designers
to

## Page 62

62
Developers
BlockerFramework
• Using the same terminology in the 
design document and the coding.
• Modularizingthe 16 characteristics.
Designers
to

## Page 63

63
BlockerFramework
Characteristics Level Editor Blocker Tool
Characteristics
Modularization

## Page 64

64
BlockerFramework
Speed Up the
Production
Pipeline
• Blocker Framework tool concept
• Speed up the pipeline and reduce 
the production cost
• Reducing the time of making new 
blocker from scratch!

## Page 65

Timeline
65
Speed Up the Production Pipeline
A BlockerCustomizationTool(WIP)
Brainstorming
& Pitching Prototyping the idea Playtesting Finalizing
Iterating
New
Blocker
Design
Start
Without the tool

## Page 66

Timeline
66
Speed Up the Production Pipeline
A BlockerCustomizationTool(WIP)
Brainstormin
g & Pitching
Prototyping
the idea Playtesting Finalizing
Brainstorming
& Pitching Prototyping the idea Playtesting Finalizing
Iterating
New
Blocker
Design
Start
Without the tool
With the tool

## Page 67

67
Recap
Blockers: Analyzing Difficulty Drivers in Candy Crush Games

## Page 68

68
Recap Everything
AnalysisDifficultyDriversin Candy Crush Games
• 4 Waysof Raising Difficulty
• BlockerFramework
• 16 Blocker Characteristics
• Candy Crush FranchiseComparision
• Player Experience
• The Pattern
• Visual Difference,ProgressionBased &
Accessibility
• Difficultyof Characteristics
• Win Rate& Characteristics

## Page 69

69
Recap Everything
AnalysisDifficultyDriversin Candy Crush Games
• Production Benefits
• How it help Designers
• How it help Artists
• How it help Developers
• Blocker Customization T ool
• Speed up the pipeline

## Page 70

70
Key Takeaways
• Encourage you to use this framework to 
breakdown your game.
• New characteristics are always WELCOME!
• Everyone can think about a new blocker in a 
systematic way
• Speed up your production!
• Fail faster and learn faster!

## Page 71

lucien.chen@king.com
Lucien Chen
 @LucienChen923
