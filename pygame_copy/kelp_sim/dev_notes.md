04/11/2023

Place to store my thoughts as I work on the project. 

What is the goal of kelp sim?

Kelp sim is a 2D simulation of a central California kelp forest with procedurally animated kelp and other elements

What features do I want to implement? 

- Kelp segments are procdeurally animated are are affected by:
    - Cursor dragging
    - water level
    - water flow
    - mechanical damage (getting cut, ripped up by storm)

- Map can be easily loaded from a bitmap made in MS paint or equivalent
- Multiple pieces of kelp
- Tide simulator that reflects real time tides or can be manually set
- ocean current simulation
- (Difficult) wave simulation
- smaller kelp plants
- fish
- dynamically casted shadows

Great, now that I have a list of features I have no idea how to implement, its time to select a start task. 

Lets start with loading a map for the kelp strands to attach to. 

I figured out map loading for black and white bitmaps in a previous project, now I need to figure it out for colored bitmaps

---
Kelp strands will be animated based off of a set of points. The number of these points and their distance from each other is derived from the initial length of the kelp. The segments become smaller as the kelp reaches its tip. Each segment joint to the next segment will have an angle associated with it that defines its position relative to the last segment. Each joint will also have a "spring weight" to it that defines how much it tries to restore itself to a default position when an outside force interacts with it.