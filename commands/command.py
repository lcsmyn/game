"""
Commands

Commands describe the input the account can do to the game.

"""

from evennia.commands.command import Command as BaseCommand
from evennia import default_cmds
import sys
import time

# from evennia import default_cmds


class Command(BaseCommand):
    """
    Base command (you may see this if a child command had no help text defined)

    Note that the class's `__doc__` string is used by Evennia to create the
    automatic help entry for the command, so make sure to document consistently
    here. Without setting one, the parent's docstring will show (like now).

    """

    # Each Command class implements the following methods, called in this order
    # (only func() is actually required):
    #
    #     - at_pre_cmd(): If this returns anything truthy, execution is aborted.
    #     - parse(): Should perform any extra parsing needed on self.args
    #         and store the result on self.
    #     - func(): Performs the actual work.
    #     - at_post_cmd(): Extra actions, often things done after
    #         every command, like prompts.
    #
    pass

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

class bdtroom():
    """
    content = the original content first time visiting, str
    content2 = content second or more times visiting, str
    edges = connections w/ other bdtrooms, dict
    here = is the player here or not, bool
    times = times the player has visited
    """

    def __init__(self, content, content2, edges, here, times):
        self.content = content
        self.content2 = content2
        self.edges = edges
        self.here = here
        self.times = times

s01 = """
The earthy odor of the forest permeates your nose and you blink and stand up.  Around you stretches a vast forest of oaks and beeches, their leaves obscuring the sun.  However, you can tell that it is at high noon.  

The grounds to your west form into a hill, and to your south, you can hear a distant rush of water, as if there were a river.  To your northeast, there is a beaten path that winds its way through the forest.  
"""

s02 = """
The hill is rather steep, and as you walk upon it, the earthy texture of the ground is replaced by gravel and hard stones.  After you have journeyed several dozens of feet, the hill becomes a barren rockscape, with the only signs of vegetation being scraps of green moss and weeds.  To your east, the summit of the hill is occupied by a small shack.  To your north, you see a stretch of distant forest.  To your west, the hill slopes down, to be replaced imposing grey mountains dusted with pale snow.

Finally, to your south, a sedate river winds its way through the valley formed by several foothills, including your own.  It flows from the westerly mountain range and settles in a placid lake, which you find hard to see due to the distance.
"""

s03 = """
You arrive at the summit, panting.  Suddenly, you are acutely aware of a terrible smell.  Walking around the shack, you see the desiccated corpse of a cow lying on the ground.  It has been there for a while, and the few slivers of meat clinging to its ribcage are being pecked off by two hungry ravens.  Averting your eyes from the scene, you round the shack and sit next to the door.

Suddenly, an old, withered hand opens the door and pulls you inside of the shack.  You are placed on a three-legged stool within the shack, and in front of you is a wizened man, brown eyes drooping amid a craggy and well-tanned face of wrinkles.

Old Man:  Hello... haven't seen anyone in a long time, eh?  Where you come from?  Up north, near the town, or a hermit like good ol' me?

You:  Who are you, and who gives you the right to act this rudely?!  I may not know about myself, but I do know that you're insane!

You get up from your chair and stride towards the door.  However, your head is jerked back, and turning around, you see the old man again.

Old Man: Answer my question!  *Where do you come from?*

You: I don't know!  A while ago, I woke up right off the hill!

The old man tenses up.

Old Man: A newcomer...

A muscle in his neck bulges, and he grimaces.  You use the opportunity to interject something.

You: And what's up with the rotting cow in the backyard?  I can smell it, even from in this shack.

Old Man: The thing's been there for the past six months.  As for why it's there, your guess is as good as mine.  I'm no owner of cattle, and that rotting cadaver showed up one day as an unpleasant surprise.  There are rumors abound in the town and such, some cockamamie talk about a cow-killing monster.

You: Huh.  Do you have food, by any chance, and know about a good place to sleep?  I'm rather hungry, and I feel that this shack is not large enough for two...

Old Man: Food I have, somewhere about here. 

He gets out of his chair and rummages within one of his shelves.  After procuring the desired food, he gives you it: two **wrinkly tomatoes**, a **cut of meat**, and a slab of **blue cheese**.

Old Man: I have more food than you expect, guess I can afford some to a poor... newcomer.  As for places to stay, there are fairly nice inns down south in the town, but the best service you can get is at the Farside House to the north.  Slightly pricey, but it's excellent.  Here, I'll hand over some of my money I no longer have use for.

The old man goes to a barrel on the ground, and when it is opened, you are amazed that it is filled with riches.  He grabs a handful of gold coins and dumps it in the sack.

Old Man: That'll cover you for at least a day or two.

You: Thanks for the hospitality.

You: If it is acceptable to ask, where did you amass such a fortune?

The old man gazes into the distance, looking wistful and angry at the same time.

Old Man: In years past, I was a foolish boy.  I pursued wealth and wealth only...  And that led to my downfall.  Oh, yes, that reminds me, I've been waiting for a newcomer to arrive to give you this.

Out of his pocket, the old man takes out a little plate of sorts, intricately colored with swirls of blue, green, and black.  He gives it to you.  It's small enough to fit neatly on the palm of your hand, like a miniature compass.

Old Man: In times of need, remember that the thing you are holding right now exists.  It may help you, as it has helped me.

Nodding with gratitude, you slip the plate into your pocket and head out of the shack.
"""

s04 = """
The mountains are full of large boulders, and as you traverse them, you cut your legs more than once.  The wind is blowing, and your clothes are thin.  Soon, you begin to feel chilly.

The hill lies to your east, the shack visible upon the summit.  Northeast is an expanse of untamed forest, which is broken up by a clearing, a small house, and a much larger house farther to the east.  A wisp of smoke rises from the chimney of the larger house.  However, the details are faint and you cannot see much.

In the distant east, an unbroken flat surface shimmering with reflections indicates a large lake.  

To your south, the river flows down from the mountains, carving a valley between hills.
"""

s05 = """
The forest is huge: trees stretch for as long as eye can see.  To your north, there is a small clearing in which the trees thin and leave a bright space for grasses and bushes to grow.  To your northeast, the brown of a small log cabin catches your eye.  It looks like someone is living there: a yellowish lantern-light shines out of the window.  In the east, you see a faint yellowish line winding through the distant forest: you suspect that it is a path.  Finally, to your south is the mountain range.
"""

s06 = """
The mansion is ornate, even though you can only see it through the gate.  Two stone gargoyles guard the front entrance, made out of great oak plates.  A brass knocker hangs on the door, and the door itself is beneath a large sign that says: "Farside House."  Firelight shines out of the window, and the manor house looks comforting to you, a weary traveler who's been on the road for far too long.  A fence surrounds the entirety of the manor, so the only entrance and exit is the gate you stand before.

As you stare at the huge manor, you see a gardener walk across the fields, her dirty hands plucking weeds out of the delicate flowerbeds that decorate the yard in front of the house.  She's wearing simple white clothing that looks like they've been used and washed many times, and her grey-white hair is tied up behind her head.  Turning, she sees you at the gate.

Quickly, she stops her work and walks before you, undoing a latch and swinging the big metal gates apart with surprising force.  She begins to talk to you.

Gardener: So, young traveler, you are here to stay at the Farside House, I assume?

You: Yes, yes.  May I visit the front desk, for some payment and a room?

The woman laughs.

Gardener: Why, the front desk is right here!  There is a small greeting room, but it mostly goes unused these days.  I'm the hotel manager and clerk.

You: ...What?  Shouldn't you be in your own room, coordinating the workers?  

Gardener: Ah, that's what I should do.  But my hotel staff knows what they're doing, all very experienced.  It's somewhat more efficient for me to chip in on some various tasks, and I enjoy it a lot more than sitting in a stuffy room all day.

You nod.  This woman seemed a little bit eccentric, but very nice, like an amicable old grandmother.  Full of energy, too.

You: Alright, how much does the upfront fee cost?

Gardener: That would be... fifty chips.  After that, each night is ten chips.  

Bringing out your sack, you look through the contents, and produce five gold coins that look like they're worth ten chips each.  You hand them to the hotel manager, who nods in approval.  She leads you within the gate, and you gaze at the well-kempt garden.  It looks perfectly trimmed, and there are only one or two weeds that you can see in each flowerbed.  The manor itself also looks impressive: two stories tall, casting a shadow over the yards.

She takes you to the front door, and unlocks it with an ornate key she produces from one of her pockets.  Inside is a well-lit lobby, with a few people milling about.  Most of them don't seem to be loitering in the greeting room, just using it as a hub to get from place to place.  There's a small desk which has a paper on it, lit by a candle on a small cubical plinth.  The manager looks at the paper and checks off a box.  Then, she procures a plain silver key from a drawer within the desk, giving it to you.

Gardener: You'll be in room 38.  All rooms are on the second floor, each one with a chamber pot.  The baths are on the ground floor, adjacent to the dining hall, which is just left of here.  Have a nice stay!

You: Thank you.  By the way, what happens to be your name?

Gardener: Belle.  My name is Belle.

You: Alright then, Belle.  I'll see you tomorrow.

You climb up the stairs and head towards room 38.  As you walk, it feels like Belle is still watching you... even though you're on the second floor and she's on the first."""

s07 = """
The log cabin is dreary: the wood looks soaked and rotted, and some of it is peeling off.  A rough-hewn stone chimney juts out of the roof at an odd angle, emitting spurts of grey smoke.  The insides are lit by a guttering lantern or two, and between the grimy windows, you can see someone at work.  All around you is forest.

You knock on the front door of the log cabin, and feel an ominous *crunch* as something in the door gives way.  Then, the door swings open and a young man with a short goatee invites you inside.  The floorboards creak as you step on them.

Young Man: So, what will you be doing here, traveler?  I have many friends down south, but you do not seem to be one of them.  Try not to mind my house, I have been trying to find money to repair it, but times have been hard going.

You: I see.  Well, I just thought this cabin would provide a good place to stay.  Better than sleeping in the wilderness, at least.

Young Man: Ah, if you're looking for a place to stay, I'm afraid this isn't the best.  You should check out the Farside House, just east of here.  But it has a fence; you'll only arrive if you go on the path and walk to the front gate.

You nod.

Young Man: It's slightly pricey, but the quality is well worth it.  The initial upfront fee is high, but after that, living is easy.  I don't have much money on me right now, but the man on the hill, I heard, is rich and generous.  He might lend you some, if you haven't visited him already.

You: Nice to know.  So I leave this cabin, go eastwards to get on the path, and go northwards to the House, correct?

Young Man: That is right.  Thanks for visiting, kind traveler!

You: Thanks as well for hosting me!

You walk towards the door across the creaking floorboards and pull it open.  Something else cracks, but you try not to notice as you stride out of the doorway and into the forest.
"""

s08 = """
You emerge into the clearing, glad to get some sunshine after being under the trees for so long.  A fallen log lies on the grass, and you sit on it, giving your legs a rest.  In front of you is a stone well that still looks like it is in use, as the bucket looks wet and the winch handle is worn with the fingers of many people.

You can see nothing besides forest around the well.
"""

s09 = """
The path is well-worn, but ruts on the road (as well as the occasional pile of dung) indicate regular use.  To the north, the large house sits on its property, while to the east, patches of swamp and bog border the calm lake.  To the west, the  forest lies.
"""

s10 = """
You enter the swamp, the wet ground squishing underneath your boots.  Groves of cattails spread their roots on this swamp, their fuzzy ends poking at your body.  East of the swamp is the lake, only punctuated by a single island in the center, and a boat at the shore.  To your north is the forest, and to your south a nest of houses that looks like a village.  Finally, to your west is the river that feeds the lake, crashing down in a series of waterfalls.
"""

s11 = """
Your boat glides across the lake, serene and still.  Below you, a minnow wriggles through the water, only to be caught and eaten by a large bass.  North of you is the island: it is stark and stony, with only two trees growing on it.  All around you, to the west and to the east, is the swamp.  Finally, to your southwest, the river empties its load into the lake via waterfall.
"""

s12 = """
The island is chilly, buffetted by drafts from the lake.  The ground is more gravel than dirt, and a boulder lies in the center of the island.  Surrounding the boulder is two pines: unusual, given that those trees don't seem to frequent the area.  However, it is not just the trees; the island itself feels *wrong* somehow, as if a huge finger had pressed on the fabric of the world, warping it.  *It is not a good place,* you think, and look around.  All is surrounded by lake.
"""

s13 = """
As you walk along the river valley, you breath in the cold, fresh air and admire the series of waterfalls than the river takes, culminating in the large lake.  Stones litter the edges of the river, some large, some small.

To your north, there is the hill.  To your northeast, you see the lake and to your east is the swamp.  To your southeast, there's a warren of houses, and directly to your south is a bustling city center.  Meanwhile, you see a mountain to your southwest.  Finally, to your northwest is a mountain range.
"""

s14 = """
The mountain is steep and rocky, and you hit your knees more than once going up.  As you climb, you see that the slope finally narrows into a peak, one that looks more like a spire jabbing through the sky.  To your north, the river continues to meander its course, and to your northeast, a less precipitous mountain sits.  To your east, there sits a small vale between the twin peaks, in which a few meager trees and bushes grow.
"""

s15 = """
In the vale between the peaks, you settle yourself on the grass.  It looks as if someone has been here before: there is a small campfire with clumps of charcoal in it, and beside the campfire lies a few skewers for cooking.  To your east, the lesser mountain sits, and to your west, the mountain with the tall peak looms imposingly over you.
"""

s16 = """
The lesser peak was not of much importance.  You feel that the slope is much less steep, and easier to climb.  To your north, you see the river valley.  To your northwest, the tall peak sits in the distance.  Between the lesser peak and the taller one, you see the vale.  Finally, looking down your east slope, you see a bustling town full of markets and shops.
"""

s17 = """
As you walk into the town, you see that it is full of people.  People talk in the open, some people shout about their wares in the market, and yet others creep around in back alleys.  Your stomach growls: you have done much traveling, and you are very hungry.  

To the north of the town, you see the river, and to the northeast, you see the skinny road that goes from the marketplaces to the river, along with many houses.  On the eastern side, there is a large manor house bearing the words: "The Old House."  Finally, to your west, a mountain rises out of the edge of the town.
"""

s18 = """
The road is beaten and used well, bordered by the riverbed to the north, the suburbs to the east, and the town square to the south.  Many people traverse the road alongside you, some of them leading mule-carts, other on horseback, and yet others on foot.
"""

s19 = """
You first enter the warren of houses through the fringe, passing through a narrow road that winds itself around several farmhouses and barns.  There aren't many people outside, but the few who are give you looks of hostility.  Glancing at your clothes, ragged from use, you feel self-conscious.  They probably think you are a beggar.

Then, you notice a ruddy-faced farmer pulling a wagon full of manure, as you can guess from the smell.  As his eyes pass over you, he drops his wagon and starts yelling.

Farmer: Dirty beggar!  Get out of here!

You: I'm not a beggar!  I'm new!

Farmer: What do you mean, you're new?  I've never heard a more unclear term in my life!  New to what?!

You sigh.

You: 'New' as in I woke up on a hill not a while back.  I don't remember who I am, and you aren't making this better, old farmer.

Farmer: A traveler?  Really?  I see you going around with torn and worn clothes and you stink more than this pile of manure!  I'd expect a traveler to be much more well-funded, *beggar*.

Spittle is flying out of the farmer's mouth as he sneers at you, and his face has turned even more red.  Disappointed, you continue to walk into the inner suburbs, not caring to talk with the angry farmer anymore.

Northwest to the suburbs is the river valley, and northeast is the swampland.  To your southwest, you can see the town square, and directly south you can see the manor house.
"""

s20 = """
The manor house is old and made out of stone.  To you, it looks more like a fortress than an actual place to live.  The windows are small and slitted, and the roof is flat.  Two chimneys poke out of the roof on opposite sides.  Enveloping the manor is a stony wall, and gates of wrought-iron block your entrance.  A sign above the hardwood doors says "The Old House."
"""

s21 = """
You shake off the unsettling feeling and walk along the hallway until you see the number "38" chiseled on a plaque on the wall.  Putting key into lock, you step into your room for the first time.

It's simple yet elegant, with polished wooden furniture which looks well-worn but inviting.  Several oil lamps gutter a pale yellow light, illuminating the room.  The bed is fluffy, white, and soft.  After a long day of traveling, you collapse into it.  The second your head hits the pillow, you drift into sleep.



The next day, you wake up and descend the stairs, ending up in the lobby again.  You can either go to the dining hall towards your east, or the bathhouse to your west.
"""

s22 = """
You enter the dining hall, and are immediately hit by the smell of cooking food.  There are several long tables laid lengthwise across the hall, while several servers scurry about, carrying food and drink on their plates.  The room is somewhat crowded, with clumps of different people congregated at separate tables.  Only a few loners such as yourself are present, scattered around the room.

You decide to take the table closest to you.  There's a group of rich-looking men close by, talking about the next harvest season.  You conclude that they're probably farmers looking for a place to stay.  

A sound of a server's walk pulls you out of your contemplations.  To your surprise, the server is Belle.

You: How many jobs do you work here?

Belle: Ah, very many.  It's not a matter of a specific one, it's a matter of where help is needed, after all.  

You're still bewildered, but you keep it to yourself.  *How does an old lady be so skilled at everything?  There's something she's hiding, for sure,* you think.

Belle hands out the food: a hunk of bread and a small cup of watered wine.  The bread is soft and delicious, and you dig into it, finishing the loaf all too soon.  The wine is worse: it tastes like it's been infused with a splash of vinegar, burning your mouth.  However, the others don't really seem to care, so you drink it, hiding your disgust.



Breakfast is finishing and people are trickling away from the dining room.  You get up to go back to room 38, but the hall lurches beneath your feet.  Your head feels like it's spinning wildly, and you can barely walk.  *What... what?* you think, confused and dizzy.

You attempt to step over the seats, but bang your knee on the leg of a chair.  Stumbling in pain, you almost fall on the ground, but you jut out your elbows to support yourself on the table.  No one seems to notice your odd behavior, and their eyes glide across the room without even noticing you.  *That's pretty strange,* you wonder.  

Making your way across the room, you trip several times, but there's always been a handy piece of furniture for you to support yourself on before trying again.  By the time you reach the doorway, everyone has already left, even the servers.  But the dizziness only gets worse: stars seem to flash in your vision, and everything hurts.  

*Crap, it's the wine... that glass of wine...* are your last thoughts before you slump against the wall and lose consciousness.
"""

s23 = """
The bathhouse is empty, and there's a sign saying that it is not open on Mondays.  You sigh in disappointment.
"""

s24 = """
You wake up in the middle of the night, in the lobby.  Your head still aches, but you're no longer dizzy, so you stand up with a groan.  Slivers of moonlight illuminate the room, from the windows set up on the wall.  A cold breeze brushes your shoulder, and you glance at the door.  It is slightly ajar, letting in the sweet night air.  Peeking through the door, you can see footsteps winding their way across the garden to some place unknown.

You can either follow the footsteps to your north, or go back to the room to your south.  
"""

s25 = """
It's a chilly night for you in your ragged clothes, and the moon is a pale crescent in the sky.  Everything is silent, except for the rustle of the tree leaves in the wind.  A squirrel scampers, and you jump in fright.

The footsteps go around the Farside House and end at a grove of limber pines.  The trees are knotted together and gnarled, creating a dense forest.  There is something eerie about the grove, maybe due to the fact that the wind is not blowing here, or the air seems to be sinking and dead, or the trees look like they are reaching out to grab you, or the oppressive silence that dominates.  Or maybe it's the hole that the trees grow around, creating a woody passageway into the depths of the forest.

*This feels like a bad idea,* you think.  *But something is off.  It's got to have to do with Belle, the strange hotel manager.  And my drink, poisoned, maybe?*  You feel something deep in your heart.  It's fear, yes, but mixed with curiosity.  You wish to *find out* what is happening.  So you enter.



Pine needles poke at your clothes, and the air seems to get even more stuffy.  Even worse, there seems to be a stinking smell, something visceral.  It reminds you of... rotting flesh.  

As the smell turns ever more pungent, the tunnel widens, allowing you to rest your hunched back.  There's also a humming in the distance, getting ever closer.  It's like the buzzing of flies around dead meat.

You pinch your nose, and emerge into a large clearing.  There are objects on the ground, which at first you are not sure about.  Then you look at it more closely, and see the contours of the head and the four legs... they are corpses of cows.  

*At least I know where the smell is coming from,* you think morbidly.  You are about to turn away in disgust when you notice a figure among the cow corpses.  It is kneeling down, then it rises--in a contented and *full* manner.  This figure has been *feeding.*

And the figure is awfully familiar.

A slight form, like an old woman, but graceful and calm.  Like an innocent hotel manager.

Belle and you lock eyes in the darkness, and you *run.*  You run as fast as you can, sprinting out of the grove of pines, not caring about the needles ripping at your skin.  You run across the grass and the garden, until finally arriving at the fence.  You do not care, and you scale the fence like a nimble cat, and continue to run, into the dark forest beyond.



You are running on pure instinct, and at last your adrenaline dies down.  Stumbling into a clearing, you see the well.  Your eyes glance around the forest, in each shadow seeing the form of Belle and the dead cattle, the writhing groves of pines, and your moment of terror.  *She'll find me,* you think.  *And then... if Belle eats the cattle raw... and she gave me my poisoned drink... she's trying to kill me.*

Then, you look at the well, with its ladder.  *She would not notice if I was in the well,* you think.  So you clamber onto the rim of the well, and go down, down, down.  The above world disappears, slice by slice, as you lower yourself into the bowels of the well.  But your fingers slip and your feet slip and you end up falling down, hitting the shallow pool of water with a splash.  It's up to your knees, soaking your pants.  But your eyes are focused on something else: this well isn't a well.  There's a narrow tunnel at the bottom, lined with guttering torches.  It piques your curiosity, and you head forward, wading through the water.

A short walk later, the stone floor of the tunnel turns into stairs and you step out of the water.  You're in a small, circular room, which has four openings to other tunnels.  The one to your south was the tunnel you entered in, and you have no desire to go back to the well.  The one to your west has a wooden sign attached to its top, reading "The hilltop (closest)."  The one to your north is called "The foundry (less close)."  Finally, the one to your east is labeled "The island (far)."
"""

s26 = """
You scale the stairs, head still rather numb from the poison that was in your wine.  Everything seems wrong.  What happened?  A stay at an innocent hotel, and all of this has happened.  A poisoned drink, a pair of footsteps, and a peculiar manager... *Something is tying these events together,* you think.  But you are not sure what.  Everything is silent except for the creaking of the floorboards as you go up to room 38.  

Inside the room, you slip into the bed, and hope for a more peaceful sleep than the drug-induced stupor that you have just experienced.



When you wake up, you realize that you are hungry.  A day of skipped meals and an unsatisfactory breakfast before that.  You decide to go down to the dining hall again.  (*But avoid the wine,* you think).  However, when you try to open the door, you find out that it is locked.  Attempting your room key, the door still does not budge.  It is then when you notice a slip of paper on the ground, 

​	*Now locked in, eh?  I find that rather amusing, don't you think?  It's just a matter of time, be patient and wait.  I'll introduce you to something you've never even imagined before... But you might not like it at the beginning.  It'll be fine, you'll get used to it.  Remember: sit tight and wait.*

​	*From B.*

​	*P.S. It was I who poisoned your drink.  Could have followed through, but I was... craving for food.*

You shiver in surprise and shock.  "From B."  It wasn't much of a stretch to assume that "B." was short for "Belle."  Belle, the old hotel manager who catered to your needs, gave you a good place to live, and attempted to kill you.  And the something she mentioned in the letter sounded ominous.  

*There is no way to escape from her,* you realize.  *I'm stuck.*

Exhausted from thinking, you go to the tap and pour yourself a cup of water.  If you can't be full, at least you won't be thirsty.

The taste hits your tongue the second you gulp down the water.  It's the vinegar, the burn, but much more concentrated.  It's acrid and bitter and tastes like death.  You spit it out, but the poison is already spreading, going down into your stomach and stretching its tendrils into your bloodstream.  Your brain feels the lurch and then the dizziness, causing you to fall on the ground.  Before your head hits the floor, you black out.
"""

s27 = """
You wake up in a stone room, lit by smoky torches and a more sinister light in the distance.  The room is sweltering, and you can feel beads of sweat running down your forehead into your eyes.  Upon trying to move, you find that you are bound to the wall and gagged, while your head pounds from the poison.  

The smoke shifts and a figure emerges.  Belle.  She still sports the grandmotherly appearance, and she is in the clothes she wears in the hotel, but her expression is different.  It is hungry, greedy.  

Belle: Ah, hello there.  I see that you are awake.

You: Mmph!  Hrrrngh!

Belle: You're just not perceptive enough, are you?  Took you a while for you to figure out that I was something other than you expected... well, I think it was because I gave you the note.  You ought to thank me.

Belle: So because you're here, I should probably tell you what I'm going to do.  It may feel unpleasant for you at the beginning, but you'll get used to it, I promise.  What I'm offering you is the chance to join this world, for real.  You've always been an outsider, haven't you?  You will become part of this world shortly.

You: Grnghrgrrhgr...

Belle: So you're asking me *why* I have this power?  *Why* you were inducted into this world?  Well, I will tell you now.

Belle: Once I had a family, in another world.  And I lost... I lost my daughter.

She says this with a broken passion, like she's been waiting to tell her soul to someone but couldn't find a person that would listen.  You glimpse tears in her eyes.

Belle: After that event, I did some shameful things that I am terribly sorry for.  But those *monsters* in that other world, they thought I was evil and wicked and they forced me out and away...  I do repent for my actions, but they were too harsh...  Those seven children were a nuisance, it was better for me to eliminate them.  And why would the annoying brats live while my beautiful, wonderful daughter perished?

Belle: I was a woman of magic back then, and I took some souvenirs.  Which I used to make this world, this world where you and everyone else respects me.  Because the people back then didn't, someone needs to pay the price.  

You: Hrm? 

Belle: Oh yes, I will show you those things.  In fact, here they are now.

The smoke cleared and revealed the source of the light.  It was a plant, but unlike anything you had ever seen.  It grew on a solid lump of obsidian, and it grew despite the lack of sunlight.  You could recognize it as a deadly nightshade plant, but it was bigger and thicker than even a tree.  Six vines branched out from the main stem, and at the end of each vine was a purplish flower emitting the ghostly light.  At the top of the stem, there was one flower larger than all of the rest.

Belle: In order to be inducted into this world, you will have to let my plant embrace you.  My soul is in these flowers, and since I am the creator of this world, you will only become part of it if you allow my soul in.  It will accompany you for the rest of your life, guiding your actions.  I'm sure it will be a very enjoyable experience, not having to make any decisions.

You realize that Belle intends to control you, and you writhe in your bonds.  They don't give, and you can only lie there, watching the scene unfold.

Belle: Now I will let you down.  Get ready, there may be initial discomfort.

The bonds unwind themselves and you stagger onto the ground.  Your feet ready themselves for running, but you are rooted to the spot, unable to move.  The nightshade is wrapping its tendrils on your shoes, and vines are climbing up your legs.  You try to scream, but find that you cannot: the words are stuck in your throat.

Now you feel the pain.  It's pain beyond what anyone could imagine, like the thousand stings of a wasp, a fire along the bones, electricity through the flesh.  And it kept on coming, the nightshade making its way along your body.

It's been an eternity and a nanosecond before you realize that the plant has covered you from neck to toe, and it is expanding its reach up towards your head.  You close your eyes, trying to resist the pain, but to no avail.  It swamps everything else in your mind, and all you can focus on is nothing.  

Then, blissful release.  The plant has captured your entire body, and everything explodes into shattered white.
"""

s28 = """
You walk through the murky tunnel towards the hilltop.  The air feels dry and unused, which was a welcome reprieve from the wetness of the well.  At one point, the tunnel begins to slope up, with a steep gradient, like someone was too lazy to quarry stairs.  After mindless minutes of walking up, the tunnel levels off and concludes in... a dead end.  You sigh in disappointment before you notice the bottom of a trapdoor on the roof of the tunnel.  Opening it up, you emerge into a very familiar room.  The smell of leather and wood hits you hard: it's the room of the old man on the hill.

The man is at his desk, and turns around.  His pupils dilate and he stiffens as he notices you in his room.  

You: Belle... the hotel manager... she was, she poisoned my drink, she was doing something in the forest, I think she's following me...

The man doesn't say a word, and stares at you blankly.  Then, one of his arms shoots out onto the table in a rigid fashion, like he's resisting something.  His fingers claw at a wooden tablet, and he points to it.  You walk over, disturbed by his strange behavior.  At his table, the man is scrawling something on the tablet with a pencil.

​	*I'm being forced--*

The pencil snaps in his hands.  But the man uses the side with the graphite to continue to write.

​	*By B-*

​	*She's evil, will tak-*

​	*your soul-*

Before he could write more, his other hand slaps his face.  Hard.  The pencil nub flies out of his palm and hits the side of the wall.  The man mutters three words, almost a whisper out of his mouth.

Man: *Remember the plate.*

Then his head snaps back and his body relaxes into unconsciousness.  A trickle of blood drips from the edge of his mouth.

You look at your pocket, where the miniature plate-thing (you're still not sure what it is) lies.  To confirm, you stick your hand in and feel the intricate patterns drawn on the object.  Nodding to yourself, you enter the trapdoor and walk the way back to the circular room.

Not feeling the strength to walk all the way to the island, you decide to visit the foundry.  You're not sure what it is, but it sounds like something promising and dangerous.  A foundry: a place to forge weapons.  Perhaps you will find a weapon to kill Belle there.
"""

s29 = """
You walk through the murky tunnel to the island.  Somewhere around halfway, the air begins to moisten and water drips through the ceiling, forming large puddles on the ground.  You find the conditions uncomfortable, so soon after wading through knee-deep water.  After what seems like hours of this drudgery, the tunnel stops and an old, rusted lader extends upwards.  It's a long climb, but you reach the top, just to realize that it's dirt.  In your anger at walking for so long to get to an impassable roof, you punch it.  It gives, dirt and sod raining from the cover and into the tunnel below.  

You nod in pleasant surprise and emerge onto the island.  Like before, it has an unexplainable *wrongness* to it, which spikes as you get closer to a large white boulder.  Confused as to why this is happening, you look around the base of the boulder and notice a dull, pulsating light.  It's glowing red and brown, so faint that you could almost lose it, but not faint enough to not show in the night.  

With a reasonable degree of caution, you pick the light up, and realize that it is not a light: it's a seed that's *emitting* light.  Light that turns much more vivid when it rolls onto your palm.  And so does the wrongness.

*Given that I haven't yet died a horrible death, this is probably safe to carry,* you think.  *If it's a slow poison, I'll be killed by Belle before it does its thing.*

So you pocket it, and head back to the circular room, the strange feeling constantly nagging at the edge of your consciousness.

When you get back, you decide to go for the foundry.  You're not sure what it is, but it sounds like something promising and dangerous.  A foundry: a place to forge weapons.  Perhaps you will find a weapon to kill Belle there.
"""

s30 = """
You head directly north and towards the foundry.  It's a long and tedious walk, and the air is dry and unused.  After a monotonous time walking, you arrive at a wooden door reinforced with iron.  Pulling it open, you find that it is unlocked.

The second you walk in, you are hit with sweltering heat and the smoke from torches on the walls.  It clouds the room, making it impossible to see.  Your foot bumps on something soft, and you realize it is rope.  But it's too late, the rope uncoils and wraps around your ankles and wrists, tying you to hooks on the wall, all by its own accord.  When the binding is done, a rag leaps from the ground and stuffs itself into your mouth, creating a gag.

The smoke shifts and a figure emerges.  It is Belle, and you tense in fright.  She still sports the grandmotherly appearance, and she is in the clothes she wears in the hotel, but her expression is different.  It is hungry, greedy.  

Belle: Ah, hello there.  I see that you have walked in here of your own accord.  Very, very stupid of you.

You: Mmph!  Hrrrngh!

Belle: You're just not perceptive enough, are you?  Took you a while for you to figure out that I was something other than you expected.  It was just when you spotted me feeding that you realized.

Belle: So because you're here, I should probably tell you what I'm going to do.  It may feel unpleasant for you at the beginning, but you'll get used to it, I promise.  What I'm offering you is the chance to join this world, for real.  You've always been an outsider, haven't you?  You will become part of this world shortly.

You: Grnghrgrrhgr...

Belle: So you're asking me *why* I have this power?  *Why* you were inducted into this world?  Well, I will tell you now.

Belle: Once I had a family, in another world.  And I lost... I lost my daughter.

She says this with a broken passion, like she's been waiting to tell her soul to someone but couldn't find a person that would listen.  You glimpse tears in her eyes.

Belle: After that event, I did some shameful things that I am terribly sorry for.  But those *monsters* in that other world, they thought I was evil and wicked and they forced me out and away...  I do repent for my actions, but they were too harsh...  Those seven children were a nuisance, it was better for me to eliminate them.  And why would the annoying brats live while my beautiful, wonderful daughter perished?

Belle: I was a woman of magic back then, and I took some souvenirs.  Which I used to make this world, this world where you and everyone else respects me.  Because the people back then didn't, someone needs to pay the price.  

You: Hrm? 

Belle: Oh yes, I will show you those things.  In fact, here they are now.

The smoke cleared and revealed the source of the light.  It was a plant, but unlike anything you had ever seen.  It grew on a solid lump of obsidian, and it grew despite the lack of sunlight.  You could recognize it as a deadly nightshade plant, but it was bigger and thicker than even a tree.  Six vines branched out from the main stem, and at the end of each vine was a purplish flower emitting the ghostly light.  At the top of the stem, there was one flower larger than all of the rest.

Belle: In order to be inducted into this world, you will have to let my plant embrace you.  My soul is in these flowers, and since I am the creator of this world, you will only become part of it if you allow my soul in.  It will accompany you for the rest of your life, guiding your actions.  I'm sure it will be a very enjoyable experience, not having to make any decisions.

You realize that Belle intends to control you, and you writhe in your bonds.  They don't give, and you can only lie there, watching the scene unfold.

Belle: Now I will let you down.  Get ready, there may be initial discomfort.

The bonds unwind themselves and you stagger onto the ground.  Your feet ready themselves for running, but you are rooted to the spot, unable to move.  The nightshade is wrapping its tendrils on your shoes, and vines are climbing up your legs.  You try to scream, but find that you cannot: the words are stuck in your throat.

Now you feel the pain.  It's pain beyond what anyone could imagine, like the thousand stings of a wasp, a fire along the bones, electricity through the flesh.  And it kept on coming, the nightshade making its way along your body.

It's been an eternity and a nanosecond before you realize that the plant has covered you from neck to toe, and it is expanding its reach up towards your head.  You close your eyes, trying to resist the pain, but to no avail.  It swamps everything else in your mind, and all you can focus on is nothing.  

Then, blissful release.  The plant has captured your entire body, and everything explodes into shattered white.
"""

s31 = """
You head directly north and towards the foundry.  It's a long and tedious walk, and the air is dry and unused.  After a monotonous time walking, you arrive at a wooden door reinforced with iron.  Pulling it open, you find that it is unlocked.

The second you walk in, you are hit with sweltering heat and the smoke from torches on the walls.  It clouds the room, making it impossible to see.  There is a sinister light in the distance, different from the orange flare of the torches, and you don't want to know what it is.  You finger the plate in your pocket again, making sure you have it ready, though for a purpose unknown.  *Please don't lie, old man,* you think.  

Your foot bumps on something soft, and you realize it is rope.  Then it twists and moves, going for your ankles and your wrists.  Unsure of what dark magic is going on, you stumble back into the wall, but the rope keeps on coming like a malevolent snake.  Afraid that you will not be able to use the plate, you extricate it from your pocket and shove it into your mouth.  The rope continues to wrap around your body, tying you to hooks on the wall.  When the binding is done, a rag leaps from the ground and stuffs itself into your mouth, creating a gag.

The smoke shifts and a figure emerges.  It is Belle, and you tense in fright.  She still sports the grandmotherly appearance, and she is in the clothes she wears in the hotel, but her expression is different.  It is hungry, greedy.  

Belle: Ah, hello there.  I see that you have walked in here of your own accord.  Very, very stupid of you.

You: Mmph!  Hrrrngh!

Belle: You're just not perceptive enough, are you?  Took you a while for you to figure out that I was something other than you expected.  It was just when you spotted me feeding that you realized.

Belle: So because you're here, I should probably tell you what I'm going to do.  It may feel unpleasant for you at the beginning, but you'll get used to it, I promise.  What I'm offering you is the chance to join this world, for real.  You've always been an outsider, haven't you?  You will become part of this world shortly.

You: Grnghrgrrhgr...

Belle: So you're asking me *why* I have this power?  *Why* you were inducted into this world?  Well, I will tell you now.

Belle: Once I had a family, in another world.  And I lost... I lost my daughter.

She says this with a broken passion, like she's been waiting to tell her soul to someone but couldn't find a person that would listen.  You glimpse tears in her eyes.

Belle: After that event, I did some shameful things that I am terribly sorry for.  But those *monsters* in that other world, they thought I was evil and wicked and they forced me out and away...  I do repent for my actions, but they were too harsh...  Those seven children were a nuisance, it was better for me to eliminate them.  And why would the annoying brats live while my beautiful, wonderful daughter perished?

Belle: I was a woman of magic back then, and I took some souvenirs.  Which I used to make this world, this world where you and everyone else respects me.  Because the people back then didn't, someone needs to pay the price.  

You: Hrm? 

Belle: Oh yes, I will show you those things.  In fact, here they are now.

The smoke cleared and revealed the source of the light.  It was a plant, but unlike anything you had ever seen.  It grew on a solid lump of obsidian, and it grew despite the lack of sunlight.  You could recognize it as a deadly nightshade plant, but it was bigger and thicker than even a tree.  Six vines branched out from the main stem, and at the end of each vine was a purplish flower emitting the ghostly light.  At the top of the stem, there was one flower larger than all of the rest.

Belle: In order to be inducted into this world, you will have to let my plant embrace you.  My soul is in these flowers, and since I am the creator of this world, you will only become part of it if you allow my soul in.  It will accompany you for the rest of your life, guiding your actions.  I'm sure it will be a very enjoyable experience, not having to make any decisions.

You realize that Belle intends to control you, and you writhe in your bonds.  They don't give, and you can only lie there, watching the scene unfold.

Belle: Now I will let you down.  Get ready, there may be initial discomfort.

The bonds unwind themselves and you stagger onto the ground.  The gag falls out of your mouth, and you spit the plate onto the ground and before Belle's feet.  At first she just looks disgusted, but then she crumples over the plate, and cries.

Belle: That... that was one of my daughter's creations... oh, my daughter, she was so artistic... Why did the cart have to run her over?  *Why?*

You run towards the nightshade plant while Belle is in tears, thinking.  *That plant contains Belle's soul.  If I kill the plant, I kill her.*

From this close a distance, the plant looks enormous.  *I'll go for the flowers,* you decide.  *And the biggest one first.*

Clambering onto the nightshade, you wince as your feet touches the stem.  You can feel the concentrated hatred and sorrow here, through your skin.  *It's a race against time,* you think, while Belle is still crying.

And then you reach the top.  You grab the base of the flower, and pull hard.  The light dims and gutters.  You pull harder.  It goes out for a second, but comes back.  Belle has noticed, and she is climbing the nightshade furiously, tears still streaming from her eyes.  You pull a third time, and the flower rips off and tumbles to the ground, petals flailing.

In that split second, Belle freezes and disintegrates into motes of light.  Upon her destruction, the other six flowers wither.  The entire plant crumbles, and around it, so does the world.  Pieces fall out of place, and the seams are ripped open, exposing the blank nothingness behind it.  You cling onto the remains of the stem, falling into the void...
"""

s32 = """
You head directly north and towards the foundry.  It's a long and tedious walk, and the air is dry and unused.  After a monotonous time walking, you arrive at a wooden door reinforced with iron.  Pulling it open, you find that it is unlocked.

The second you walk in, you are hit with sweltering heat and the smoke from torches on the walls.  It clouds the room, making it impossible to see.  There is a sinister light in the distance, different from the orange flare of the torches, and you don't want to know what it is.  You finger the seed in your pocket again, making sure you have it ready, though for a purpose unknown.

Your foot bumps on something soft, and you realize it is rope.  Then it twists and moves, going for your ankles and your wrists.  Unsure of what dark magic is going on, you stumble back into the wall, but the rope keeps on coming like a malevolent snake.  Afraid that you will not be able to use the seed, you extricate it from your pocket and shove it into your mouth.  The rope continues to wrap around your body, tying you to hooks on the wall.  When the binding is done, a rag leaps from the ground and stuffs itself into your mouth, creating a gag.

The smoke shifts and a figure emerges.  It is Belle, and you tense in fright.  She still sports the grandmotherly appearance, and she is in the clothes she wears in the hotel, but her expression is different.  It is hungry, greedy.  

Belle: Ah, hello there.  I see that you have walked in here of your own accord.  Very, very stupid of you.

You: Mmph!  Hrrrngh!

Belle: You're just not perceptive enough, are you?  Took you a while for you to figure out that I was something other than you expected.  It was just when you spotted me feeding that you realized.

Belle: So because you're here, I should probably tell you what I'm going to do.  It may feel unpleasant for you at the beginning, but you'll get used to it, I promise.  What I'm offering you is the chance to join this world, for real.  You've always been an outsider, haven't you?  You will become part of this world shortly.

You: Grnghrgrrhgr...

Belle: So you're asking me *why* I have this power?  *Why* you were inducted into this world?  Well, I will tell you now.

Belle: Once I had a family, in another world.  And I lost... I lost my daughter.

She says this with a broken passion, like she's been waiting to tell her soul to someone but couldn't find a person that would listen.  You glimpse tears in her eyes.

Belle: After that event, I did some shameful things that I am terribly sorry for.  But those *monsters* in that other world, they thought I was evil and wicked and they forced me out and away...  I do repent for my actions, but they were too harsh...  Those seven children were a nuisance, it was better for me to eliminate them.  And why would the annoying brats live while my beautiful, wonderful daughter perished?

Belle: I was a woman of magic back then, and I took some souvenirs.  Which I used to make this world, this world where you and everyone else respects me.  Because the people back then didn't, someone needs to pay the price.  

You: Hrm? 

Belle: Oh yes, I will show you those things.  In fact, here they are now.

The smoke cleared and revealed the source of the light.  It was a plant, but unlike anything you had ever seen.  It grew on a solid lump of obsidian, and it grew despite the lack of sunlight.  You could recognize it as a deadly nightshade plant, but it was bigger and thicker than even a tree.  Six vines branched out from the main stem, and at the end of each vine was a purplish flower emitting the ghostly light.  At the top of the stem, there was one flower larger than all of the rest.

Belle: In order to be inducted into this world, you will have to let my plant embrace you.  My soul is in these flowers, and since I am the creator of this world, you will only become part of it if you allow my soul in.  It will accompany you for the rest of your life, guiding your actions.  I'm sure it will be a very enjoyable experience, not having to make any decisions.

You realize that Belle intends to control you, and you writhe in your bonds.  They don't give, and you can only lie there, watching the scene unfold.

Belle: Now I will let you down.  Get ready, there may be initial discomfort.

The bonds unwind themselves and you stagger onto the ground.  The gag falls out of your mouth, and you spit the seed onto the ground and before Belle's feet.  She shouts in disbelief, and reaches to pick up the seed, but it is *rolling.*  It rolls to the nightshade plant, faster than Belle can run, and settles itself next to the main stem.  As if in a time-lapse, the seed grows and grows, taking shape as a strangler fig.  The same red-brown light emitted by the seed now pulsates from the entire plant, which is rapidly climbing up the vines of the nightshade, weighing them down.  The tendrils of the parasitic plant first reach the outer flowers, cutting off their purple glow and replacing it with its own thudding color.  

At last the vines reach the top nightshade flower, and Belle is doubled over in pain.  The loss of six parts of her soul must be agonizing.  Knots of wood form a cage over the blossom.  When the cage is done, you can feel the nightshade withering inside... and then, nothing.  Belle disintegrates into motes of light.  The nightshade begins to fall apart, just as the world does.   Pieces fall out of place, and the seams are ripped open, exposing the blank nothingness behind it.  You hug the wall, even as you fall into the void...
"""

s33 = """
You hear the hiss of trapped steam and the world opens again, nightshade vines curling away from your skin.  Belle is looking at you, but you can't look back at her.  Your eyes refuse to obey.

A single command rings out in your mind.  *Go.*  You try to lie down, but it is as if a giant has pushed you along, and you are forced to walk.  You walk and walk, climbing out of the well and going back to the Farside House.

Inside, you are screaming for help.  Your mind batters itself on the cages Belle's soul has created, but it cannot escape.  Days and months and years pass like this, and by the time someone new has arrived, your mind is slumped in defeat.  You see the poisoned wine Belle gives her, sees her stumble and fall, but your eyes gloss over her like she doesn't exist.  Belle has made you do this, she has stripped you of your free will.  

A day later, the woman is talking animatedly with other "travelers."  And when eye contact is made, all of us, all of the imprisoned, know what has befallen the others.



Credits:

Built with Evennia (https://www.evennia.com)

Hosted by Amazon (https://aws.amazon.com)

Written/coded by me
"""

s34 = """
You wake up in darkness.  

You: Hello?

No one answers.  Everything is gone, and you are residing in the space where Belle's world has fallen.  *Along with the people contained in it.  They're all gone.*

*I hate this place,* you declare to yourself.  Upon this statement, there is an almost imperceptible warping of the world, and the darkness disappears.  It is replaced by a monitor and keyboard.  All around you are other employees, and sun shines through the glass walls of the building.

It all comes back to you in an instant..  *I'm 46 years old, with a wife, two kids, and a cat.  I work at Apple.  And I'm not sure if all of that was a dream.*



Credits:

Built with Evennia (https://www.evennia.com)

Hosted by Amazon (https://aws.amazon.com)

Written/coded by me
"""

s35 = """
You wake up in darkness.  All around you are faces: some of them you recognize, like the old man from the hill, the guy in the log cabin, and several farmers.  Others, you don't.

You: Where are we?

Log Cabin Person: My best guess is the void where the world used to exist.  Oh yes, thanks for saving us!  We've been stuck in here for a long time.  For me personally, I think it's been seven thousand, six hundred, and fifty-five years counting subjectively.  

Hill Man: Look at you, the whippersnapper!  I've been here for several trillion years!  The only thing I do except for give up is count numbers!

You're amazed by the numbers these people have thrown out.  

You: Well, it's been a good run.  I suspect that we're all people in the real world, or possibly alternate realities.  The thing is, if I see a person talking about being imprisoned by an evil woman named Belle, I'll be sure to talk to them.

This earns several chuckles from everyone.

You: In the meantime, I hate this darn place.  I'm going out.

Upon this statement, there is an almost imperceptible warping of the world, and the darkness disappears.  It is replaced by a monitor and keyboard.  All around you are other employees, and sun shines through the glass walls of the building.

It all comes back to you in an instant..  *I'm 46 years old, with a wife, two kids, and a cat.  I work at Apple.  And I'm not sure if all of that was a dream.*



Credits:

Built with Evennia (https://www.evennia.com)

Hosted by Amazon (https://aws.amazon.com)

Written/coded by me
"""

s01t = """
Around you stretches a vast forest of oaks and beeches, their leaves obscuring the sun.  The grounds to your west form into a hill, and to your south, you can hear a distant rush of water, as if there were a river.  To your northeast, there is a beaten path that winds its way through the forest.
"""

s03t = """
You arrive at the summit, panting.  Suddenly, you are acutely aware of a terrible smell.  Walking around the shack, you see the desiccated corpse of a cow lying on the ground.  It has been there for a while, and the few slivers of meat clinging to its ribcage are being pecked off by two hungry ravens.  Averting your eyes from the scene, you round the shack and sit next to the door.
"""

s19t = """
You first enter the warren of houses through the fringe, passing through a narrow road that winds itself around several farmhouses and barns.  There aren't many people outside, but the few who are give you looks of hostility.  Glancing at your clothes, ragged from use, you feel self-conscious.  They probably think you are a beggar.

Northwest to the suburbs is the river valley, and northeast is the swampland.  To your southwest, you can see the town square, and directly south you can see the manor house.
"""

s07t = """
The log cabin is dreary: the wood looks soaked and rotted, and some of it is peeling off.  A rough-hewn stone chimney juts out of the roof at an odd angle, emitting spurts of grey smoke.  The insides are lit by a guttering lantern or two, and between the grimy windows, you can see someone at work.  All around you is forest.
"""

edge01 = {
    "north": "r05",
    "northeast": "r09",
    "east": "r10",
    "southeast": "r13",
    "south": "r13",
    "southwest": "r02",
    "west": "r02",
    "northwest": "r02"
}

edge02 = {
    "north": "r05",
    "northeast": "r05",
    "east": "r03",
    "southeast": "r01",
    "south": "r13",
    "southwest": "r13",
    "west": "r04",
    "northwest": "r04"
}

edge03 = {
    "north": "r02",
    "northeast": "r02",
    "east": "r02",
    "southeast": "r02",
    "south": "r02",
    "southwest": "r02",
    "west": "r02",
    "northwest": "r02"
}

edge04 = {
    "north": "",
    "northeast": "r05",
    "east": "r05",
    "southeast": "r02",
    "south": "r13",
    "southwest": "r13",
    "west": "",
    "northwest": ""
}

edge05 = {
    "north": "r08",
    "northeast": "r07",
    "east": "r09",
    "southeast": "r09",
    "south": "r01",
    "southwest": "r03",
    "west": "r04",
    "northwest": "r04"
}

edge06 = {
    "north": "r21",
    "northeast": "r21",
    "east": "r21",
    "southeast": "r21",
    "south": "r21",
    "southwest": "r21",
    "west": "r21",
    "northwest": "r21"
}

edge07 = {
    "north": "r05",
    "northeast": "r05",
    "east": "r05",
    "southeast": "r05",
    "south": "r05",
    "southwest": "r05",
    "west": "r05",
    "northwest": "r05"
}

edge08 = {
    "north": "r05",
    "northeast": "r05",
    "east": "r05",
    "southeast": "r05",
    "south": "r05",
    "southwest": "r05",
    "west": "r05",
    "northwest": "r05"
}

edge09 = {
    "north": "r06",
    "northeast": "r06",
    "east": "r10",
    "southeast": "10",
    "south": "r01",
    "southwest": "r01",
    "west": "r05",
    "northwest": "r05"
}

edge10 = {
    "north": "r05",
    "northeast": "r05",
    "east": "r11",
    "southeast": "19",
    "south": "r19",
    "southwest": "r13",
    "west": "r13",
    "northwest": "r9"
}

edge11 = {
    "north": "r12",
    "northeast": "r10",
    "east": "r10",
    "southeast": "10",
    "south": "r10",
    "southwest": "r13",
    "west": "r10",
    "northwest": "r10"
}

edge12 = {
    "north": "r11",
    "northeast": "r11",
    "east": "r11",
    "southeast": "r11",
    "south": "r11",
    "southwest": "r11",
    "west": "r11",
    "northwest": "r11"
}

edge13 = {
    "north": "r02",
    "northeast": "r11",
    "east": "r10",
    "southeast": "r19",
    "south": "r17",
    "southwest": "r14",
    "west": "",
    "northwest": "r04"
}

edge14 = {
    "north": "r13",
    "northeast": "r16",
    "east": "r15",
    "southeast": "r16",
    "south": "",
    "southwest": "",
    "west": "",
    "northwest": ""
}

edge15 = {
    "north": "r14",
    "northeast": "16",
    "east": "r16",
    "southeast": "r16",
    "south": "r16",
    "southwest": "r14",
    "west": "r14",
    "northwest": "r14"
}

edge16 = {
    "north": "r13",
    "northeast": "r13",
    "east": "r17",
    "southeast": "r17",
    "south": "",
    "southwest": "r14",
    "west": "r15",
    "northwest": "r14"
}

edge17 = {
    "north": "r13",
    "northeast": "r18",
    "east": "r20",
    "southeast": "r20",
    "south": "",
    "southwest": "r16",
    "west": "r16",
    "northwest": "13"
}

edge18 = {
    "north": "r13",
    "northeast": "r19",
    "east": "r19",
    "southeast": "r19",
    "south": "r17",
    "southwest": "r17",
    "west": "r17",
    "northwest": "r13"
}

edge19 = {
    "north": "r13",
    "northeast": "r10",
    "east": "",
    "southeast": "r20",
    "south": "r20",
    "southwest": "r17",
    "west": "r18",
    "northwest": "r13"
}

edge20 = {
    "north": "r19",
    "northeast": "r19",
    "east": "",
    "southeast": "",
    "south": "",
    "southwest": "r17",
    "west": "r17",
    "northwest": "r19"
}

edge21 = {
    "north": "r22",
    "northeast": "r22",
    "east": "r22",
    "southeast": "r22",
    "south": "r23",
    "southwest": "r23",
    "west": "r23",
    "northwest": "r23"
}

edge22 = {
    "north": "r24",
    "northeast": "r24",
    "east": "r24",
    "southeast": "r24",
    "south": "r24",
    "southwest": "r24",
    "west": "r24",
    "northwest": "r24"
}

edge23 = {
    "north": "r22",
    "northeast": "r22",
    "east": "r22",
    "southeast": "r22",
    "south": "r22",
    "southwest": "r22",
    "west": "r22",
    "northwest": "r22"
}

edge24 = {
    "north": "r25",
    "northeast": "r25",
    "east": "r25",
    "southeast": "r26",
    "south": "r26",
    "southwest": "r26",
    "west": "r26",
    "northwest": "r25"
}

edge25 = {
    "north": "r30",
    "northeast": "r30",
    "east": "r29",
    "southeast": "r29",
    "south": "",
    "southwest": "",
    "west": "r28",
    "northwest": "r28"
}

edge26 = {
    "north": "r27",
    "northeast": "r27",
    "east": "r27",
    "southeast": "r27",
    "south": "r27",
    "southwest": "r27",
    "west": "r27",
    "northwest": "r27"
}

edge27 = {
    "north": "r33",
    "northeast": "r33",
    "east": "r33",
    "southeast": "r33",
    "south": "r33",
    "southwest": "r33",
    "west": "r33",
    "northwest": "r33"
}

edge28 = {
    "north": "r31",
    "northeast": "r31",
    "east": "r31",
    "southeast": "r31",
    "south": "r31",
    "southwest": "r31",
    "west": "r31",
    "northwest": "r31"
}

edge29 = {
    "north": "r32",
    "northeast": "r32",
    "east": "r32",
    "southeast": "r32",
    "south": "r32",
    "southwest": "r32",
    "west": "r32",
    "northwest": "r32"
}

edge30 = {
    "north": "r33",
    "northeast": "r33",
    "east": "r33",
    "southeast": "r33",
    "south": "r33",
    "southwest": "r33",
    "west": "r33",
    "northwest": "r33"
}

edge31 = {
    "north": "r34",
    "northeast": "r34",
    "east": "r34",
    "southeast": "r34",
    "south": "r34",
    "southwest": "r34",
    "west": "r34",
    "northwest": "r34"
}

edge32 = {
    "north": "r35",
    "northeast": "r35",
    "east": "r35",
    "southeast": "r35",
    "south": "r35",
    "southwest": "r35",
    "west": "r35",
    "northwest": "r35"
}

edge33 = {
    "north": "r01",
    "northeast": "r01",
    "east": "r01",
    "southeast": "r01",
    "south": "r01",
    "southwest": "r01",
    "west": "r01",
    "northwest": "r01"
}

edge34 = {
    "north": "r01",
    "northeast": "r01",
    "east": "r01",
    "southeast": "r01",
    "south": "r01",
    "southwest": "r01",
    "west": "r01",
    "northwest": "r01"
}

edge35 = {
    "north": "r01",
    "northeast": "r01",
    "east": "r01",
    "southeast": "r01",
    "south": "r01",
    "southwest": "r01",
    "west": "r01",
    "northwest": "r01"
}

r01 = bdtroom(s01, s01t, edge01, True, 1)
r02 = bdtroom(s02, s02, edge02, False, 0)
r03 = bdtroom(s03, s03t, edge03, False, 0)
r04 = bdtroom(s04, s04, edge04, False, 0)
r05 = bdtroom(s05, s05, edge05, False, 0)
r06 = bdtroom(s06, s06, edge06, False, 0)
r07 = bdtroom(s07, s07t, edge07, False, 0)
r08 = bdtroom(s08, s08, edge08, False, 0)
r09 = bdtroom(s09, s09, edge09, False, 0)
r10 = bdtroom(s10, s10, edge10, False, 0)
r11 = bdtroom(s11, s11, edge11, False, 0)
r12 = bdtroom(s12, s12, edge12, False, 0)
r13 = bdtroom(s13, s13, edge13, False, 0)
r14 = bdtroom(s14, s14, edge14, False, 0)
r15 = bdtroom(s15, s15, edge15, False, 0)
r16 = bdtroom(s16, s16, edge16, False, 0)
r17 = bdtroom(s17, s17, edge17, False, 0)
r18 = bdtroom(s18, s18, edge18, False, 0)
r19 = bdtroom(s19, s19t, edge19, False, 0)
r20 = bdtroom(s20, s20, edge20, False, 0)
r21 = bdtroom(s21, s21, edge21, False, 0)
r22 = bdtroom(s22, s22, edge22, False, 0)
r23 = bdtroom(s23, s23, edge23, False, 0)
r24 = bdtroom(s24, s24, edge24, False, 0)
r25 = bdtroom(s25, s25, edge25, False, 0)
r26 = bdtroom(s26, s26, edge26, False, 0)
r27 = bdtroom(s27, s27, edge27, False, 0)
r28 = bdtroom(s28, s28, edge28, False, 0)
r29 = bdtroom(s29, s29, edge29, False, 0)
r30 = bdtroom(s30, s30, edge30, False, 0)
r31 = bdtroom(s31, s31, edge31, False, 0)
r32 = bdtroom(s32, s32, edge32, False, 0)
r33 = bdtroom(s33, s33, edge33, False, 0)
r34 = bdtroom(s34, s34, edge34, False, 0)
r35 = bdtroom(s35, s35, edge35, False, 0)

room_list = [r01, r02, r03, r04, r05, r06, r07, r08, r09, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29, r30, r31, r32, r33, r34, r35]

class givenum(default_cmds.MuxCommand):
    """
    Simple command example
    
    Usage:
        echo [text]
    
    This command simply echoes text back to the caller.
    """
    
    key = "num"
    
    def func(self):
        for x in room_list:
            self.caller.msg(x.times)
            self.caller.msg(x.here)

class start(default_cmds.MuxCommand):

    key = "start"

    def func(self):
        self.caller.msg("|bWelcome to the game!")
        yield 2
        self.caller.msg("Use 'north,' 'northeast,' 'east,' 'southeast,' 'south,' 'southwest,' 'west,' and 'northwest' to travel in said directions.")
        yield 4
        self.caller.msg("If the text does not give you what place is in what direction, put any of the direction commands to proceed onto the next scene.")
        yield 4
        self.caller.msg("To restart the game, use any of the direction commands when you reach the end. (You can tell it's the end when the credits are given).")
        yield 4
        self.caller.msg("Because of internal consistency bugs, it's highly recommended that you visit these places in the story: the house at the top of the hill, the island, and the log cabin, *before* you go to the large mansion in the forest.")
        yield 6
        self.caller.msg("There may be understanding issues in the plotline if these places are not visited, e.g. having a character reference something they said to you, but you didn't go to that place, and didn't hear their original talk.  Or smaller issues like a person you've not met before being referred to as 'the person' instead of 'a person'.")
        yield 8
        self.caller.msg("These bugs would take a disproportionate amount of time to fix, so I've decided to leave them be.")
        yield 4
        self.caller.msg("Anyways, hope you have fun!")
        yield 4
        self.caller.msg(s01)
        self.caller.msg("-------------------------------------")


class north(default_cmds.MuxCommand):
    
    key = "north"

    def func(self):
        for x in room_list:
            if x.here == True:
                try:
                    y = str_to_class(x.edges["north"])
                except AttributeError:
                    self.caller.msg("You can't go farther north than here!")
                    break
                x.here = False
                y.here = True
                y.times += 1
                if y.times <= 1:
                    self.caller.msg(y.content)
                else:
                    self.caller.msg(y.content2)
                self.caller.msg("-------------------------------------")
                break


class northeast(default_cmds.MuxCommand):

    key = "northeast"

    def func(self):
        for x in room_list:
            if x.here == True:
                try:
                    y = str_to_class(x.edges["northeast"])
                except AttributeError:
                    self.caller.msg("You can't go farther northeast than here!")
                    break
                x.here = False
                y.here = True
                y.times += 1
                if y.times <= 1:
                    self.caller.msg(y.content)
                else:
                    self.caller.msg(y.content2)
                self.caller.msg("-------------------------------------")
                break


class east(default_cmds.MuxCommand):

    key = "east"

    def func(self):
        for x in room_list:
            if x.here == True:
                try:
                    y = str_to_class(x.edges["east"])
                except AttributeError:
                    self.caller.msg("You can't go farther east than here!")
                    break
                x.here = False
                y.here = True
                y.times += 1
                if y.times <= 1:
                    self.caller.msg(y.content)
                else:
                    self.caller.msg(y.content2)
                self.caller.msg("-------------------------------------")
                break

class southeast(default_cmds.MuxCommand):

    key = "southeast"

    def func(self):
        for x in room_list:
            if x.here == True:
                try:
                    y = str_to_class(x.edges["southeast"])
                except AttributeError:
                    self.caller.msg("You can't go farther southeast than here!")
                    break
                x.here = False  
                y.here = True
                y.times += 1
                if y.times <= 1:
                    self.caller.msg(y.content)
                else:
                    self.caller.msg(y.content2)
                self.caller.msg("-------------------------------------")
                break

class south(default_cmds.MuxCommand):

    key = "south"

    def func(self):
        for x in room_list:
            if x.here == True:
                try:
                    y = str_to_class(x.edges["south"])
                except AttributeError:
                    self.caller.msg("You can't go farther south than here!")
                    break
                x.here = False
                y.here = True
                y.times += 1
                if y.times <= 1:
                    self.caller.msg(y.content)
                else:
                    self.caller.msg(y.content2)
                self.caller.msg("-------------------------------------")
                break

class southwest(default_cmds.MuxCommand):

    key = "southwest"

    def func(self):
        for x in room_list:
            if x.here == True:
                try:
                    y = str_to_class(x.edges["southwest"])
                except AttributeError:
                    self.caller.msg("You can't go farther southwest than here!")
                    break
                x.here = False
                y.here = True
                y.times += 1
                if y.times <= 1:
                    self.caller.msg(y.content)
                else:
                    self.caller.msg(y.content2)
                self.caller.msg("-------------------------------------")
                break

class west(default_cmds.MuxCommand):

    key = "west"

    def func(self):
        for x in room_list:
            if x.here == True:
                try:
                    y = str_to_class(x.edges["west"])
                except AttributeError:
                    self.caller.msg("You can't go farther west than here!")
                    break
                x.here = False
                y.here = True
                y.times += 1
                if y.times <= 1:
                    self.caller.msg(y.content)
                else:
                    self.caller.msg(y.content2)
                self.caller.msg("-------------------------------------")
                break

class northwest(default_cmds.MuxCommand):

    key = "northwest"

    def func(self):
        for x in room_list:
            if x.here == True:
                try:
                    y = str_to_class(x.edges["northwest"])
                except AttributeError:
                    self.caller.msg("You can't go farther northwest than here!")
                    break
                x.here = False
                y = str_to_class(x.edges["southwest"])
                y.here = True
                x.times += 1
                if y.times <= 1:
                    self.caller.msg(y.content)
                else:
                    self.caller.msg(y.content2)
                self.caller.msg("-------------------------------------")
                break

# -------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
# -------------------------------------------------------------

# from evennia.utils import utils
#
#
# class MuxCommand(Command):
#     """
#     This sets up the basis for a MUX command. The idea
#     is that most other Mux-related commands should just
#     inherit from this and don't have to implement much
#     parsing of their own unless they do something particularly
#     advanced.
#
#     Note that the class's __doc__ string (this text) is
#     used by Evennia to create the automatic help entry for
#     the command, so make sure to document consistently here.
#     """
#     def has_perm(self, srcobj):
#         """
#         This is called by the cmdhandler to determine
#         if srcobj is allowed to execute this command.
#         We just show it here for completeness - we
#         are satisfied using the default check in Command.
#         """
#         return super().has_perm(srcobj)
#
#     def at_pre_cmd(self):
#         """
#         This hook is called before self.parse() on all commands
#         """
#         pass
#
#     def at_post_cmd(self):
#         """
#         This hook is called after the command has finished executing
#         (after self.func()).
#         """
#         pass
#
#     def parse(self):
#         """
#         This method is called by the cmdhandler once the command name
#         has been identified. It creates a new set of member variables
#         that can be later accessed from self.func() (see below)
#
#         The following variables are available for our use when entering this
#         method (from the command definition, and assigned on the fly by the
#         cmdhandler):
#            self.key - the name of this command ('look')
#            self.aliases - the aliases of this cmd ('l')
#            self.permissions - permission string for this command
#            self.help_category - overall category of command
#
#            self.caller - the object calling this command
#            self.cmdstring - the actual command name used to call this
#                             (this allows you to know which alias was used,
#                              for example)
#            self.args - the raw input; everything following self.cmdstring.
#            self.cmdset - the cmdset from which this command was picked. Not
#                          often used (useful for commands like 'help' or to
#                          list all available commands etc)
#            self.obj - the object on which this command was defined. It is often
#                          the same as self.caller.
#
#         A MUX command has the following possible syntax:
#
#           name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#         The 'name[ with several words]' part is already dealt with by the
#         cmdhandler at this point, and stored in self.cmdname (we don't use
#         it here). The rest of the command is stored in self.args, which can
#         start with the switch indicator /.
#
#         This parser breaks self.args into its constituents and stores them in the
#         following variables:
#           self.switches = [list of /switches (without the /)]
#           self.raw = This is the raw argument input, including switches
#           self.args = This is re-defined to be everything *except* the switches
#           self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                      no = is found, this is identical to self.args.
#           self.rhs: Everything to the right of = (rhs:'right-hand side').
#                     If no '=' is found, this is None.
#           self.lhslist - [self.lhs split into a list by comma]
#           self.rhslist - [list of self.rhs split into a list by comma]
#           self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#           All args and list members are stripped of excess whitespace around the
#           strings, but case is preserved.
#         """
#         raw = self.args
#         args = raw.strip()
#
#         # split out switches
#         switches = []
#         if args and len(args) > 1 and args[0] == "/":
#             # we have a switch, or a set of switches. These end with a space.
#             switches = args[1:].split(None, 1)
#             if len(switches) > 1:
#                 switches, args = switches
#                 switches = switches.split('/')
#             else:
#                 args = ""
#                 switches = switches[0].split('/')
#         arglist = [arg.strip() for arg in args.split()]
#
#         # check for arg1, arg2, ... = argA, argB, ... constructs
#         lhs, rhs = args, None
#         lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#         if args and '=' in args:
#             lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#             lhslist = [arg.strip() for arg in lhs.split(',')]
#             rhslist = [arg.strip() for arg in rhs.split(',')]
#
#         # save to object properties:
#         self.raw = raw
#         self.switches = switches
#         self.args = args.strip()
#         self.arglist = arglist
#         self.lhs = lhs
#         self.lhslist = lhslist
#         self.rhs = rhs
#         self.rhslist = rhslist
#
#         # if the class has the account_caller property set on itself, we make
#         # sure that self.caller is always the account if possible. We also create
#         # a special property "character" for the puppeted object, if any. This
#         # is convenient for commands defined on the Account only.
#         if hasattr(self, "account_caller") and self.account_caller:
#             if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                 # caller is an Object/Character
#                 self.character = self.caller
#                 self.caller = self.caller.account
#             elif utils.inherits_from(self.caller, "evennia.accounts.accounts.DefaultAccount"):
#                 # caller was already an Account
#                 self.character = self.caller.get_puppet(self.session)
#             else:
#                 self.character = None
