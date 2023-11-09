11/04/2023

Place to store my thoughts as I work on the project. 

What is the goal of kelp sim?

Kelp sim is a 2D simulation of a central California kelp forest with procedurally animated kelp and other elements

What features do I want to implement? 

- Kelp segments are procedurally animated are are affected by:
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
- dynamic weather events

- control of lobster player character

Great, now that I have a list of features I have no idea how to implement, its time to select a start task. 

Lets start with loading a map for the kelp strands to attach to. 

I figured out map loading for black and white bitmaps in a previous project, now I need to figure it out for colored bitmaps

---
Kelp strands will be animated based off of a set of points. The number of these points and their distance from each other is derived from the initial length of the kelp. The segments become smaller as the kelp reaches its tip. Each segment joint to the next segment will have an angle associated with it that defines its position relative to the last segment. Each joint will also have a "spring weight" to it that defines how much it tries to restore itself to a default position when an outside force interacts with it.

11/05/2023

After doing some googling I've figured out that I need to use inverse kinematics for the kelp.

basically I want to derive the location of the joints based on the location of the final joint. The final joints location will be determined by the anchor point and the water level. If the water level exceeds the max vertical length of the kep, it stands up straight, if its below, the kep either sags to the left or right. 

How the heck am I supposed to add water flow? 


https://www.youtube.com/watch?v=hbgDqyy8bIw

https://www.reddit.com/r/proceduralgeneration/comments/8yz4fv/my_first_successful_attempt_at_procedural/



guess I need to learn about forward and inverse kinematics again (took a course on this during college for robot arm control)


11/06/2023

I've made some decent progress. 

- got the water line implemented
- sky paints above water line
- kelp moves in relation to the waves (this needs work)

what needs work:
- kelp interaction with water line
- algo for defining kelp movement relative to waves
- kelp detail (leaves, water bladders)
- need a sea floor
- need final segments of kelp to be skinnier/ dynamically smaller
- need better kelp graphics (outlines to determine one from other)
- seafloor
- lobster player character - see animation for wonky lizards
- lighting - how??? Know zero about this, seems really really complicated

if performance drops off, may need to migrate from pygame directly to SDL to cut out the middle layer of SW for better performance, but then its all C++ land


What did I learn?
instead of using neg X offset for the sinewave water line you can vary the amplitude of the wave between pos and neg with a bit of noise to get a more realistic looking water line - this must be how rain world does it


cont later in the day

I got rainworld looking water working (not 3D, just front wave) by varying the amplitude and keeping the offset but decreasing it


https://www.xconvert.com/downloads


11/09/2023

The project is beginning to grow on me. I've improved the kelp to have better wave tracking and surface interactions

