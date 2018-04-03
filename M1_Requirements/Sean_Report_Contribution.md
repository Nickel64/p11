# Project Proposal and Requirements Document

The aim of the project proposal and requirements document is to
capture the requirements for the software your group is to build. It
should communicate clearly to the supervisor, client and course
coordinator exactly what the software you build is going to do, and
what constraints it must meet while doing so.

The document should also demonstrate your understanding of the main
analysis principles and quality guidelines, using tools and associated
notations as necessary to communicate the requirements precisely,
unambiguously and clearly in a written technical document. Page specifications below are *limits not targets* and refer to the pages in the PDF generated from the markdown. Because the size of your document is necessarily limited, you should ensure
that you focus your efforts on those requirements that are most
important to completing a successful system: if sections are at their
page limit, indicate how many would items be expected in a complete
specification. 

The ENGR 301 project proposal and requirements document should be based
on the standard ISO/IEC/IEEE 29148:2011(E), primarily sections 8.4 and
9.5, plus section 9.4 for projects involving hardware and ISO 25010
SQuaRE for systemic requirements. The proposal and requirements
document should contain the sections listed below, and conform to the
formatting rules listed at the end of this brief. 

### 3.2 Functions

This is typically the longest subsection in the document - see 9.5.11.
List up to fifty use cases (in order of priority for development), and
for at least top ten focal use cases, write a short goal statement and
use case body (up to seven pages).  Identify the use cases that
comprise a minimum viable product.

Plug in webcam and software renders
Select area for traffic lights
Select area for bus detection

Engineering Standard for Functions:
* I/O relationships
* Validity checks
* Respose to abnormal input
* Sequence of operations
* Effect of parameters

Input:
* Camera feed, video of scene
* GUI for selecting lights
* Training data (Images)

Output: 
* Training data weights
* Alert (Box + red light)
* Info of scene 
    * Time/Date
    * License plate
    * Image/video of moment

MVP
* Run GUI, select lights
* Selected area and scanned/processed
* When movement detected/line passed alert
* Static image of moment
* Overlay interface with video









## MVP: 
    * Video input from consumer webcam using angle from Podcast
    * User input for detecting intersection, define light with circle, define bus with a line that is crossed w/ User interface
    * Output static image of moment offending occurs
    * Works on windows
Priority list:
## END GOAL
    * Consumer webcam and hardware, any intersection, any angle
    * Plug in webcam, run program and auto detects intersection elements
    * Output video of moment offending occurs
    * User defined code when event occurs
    * Works on Linux
    
## EXTRAS
    * License plate detection
    * Events of interest
        * Police intervention
        * Bus collisions w/ Pedestrians
        * Near Misses
    * OBS Integration
    * Prediction/statistics based on time, weather etc
    * Detecting different kinds of busses, other vehicles
        * Reporting statistics of event to parent company (Or Traffic authority)
        * could use licence plate detection
    * Speed Detection


### 3.10 Supporting information


Dylan's section 

Define all inputs into and outputs from the software system. The description should complement the interface
descriptions in 9.5.3.3.1 through 9.5.3.3.5, and should not repeat information there.
Each interface defined should include the following content:
a) Name of item;
b) Description of purpose;
c) Source of input or destination of output;
d) Valid range, accuracy, and/or tolerance;
e) Units of measure;
f) Timing;
g) Relationships to other inputs/outputs;
h) Screen formats/organization;
i) Window formats/organization;
j) Data formats;
k) Command formats;
l) Endmessages. 

9.5.3.1 System interfaces
List each system interface and identify the functionality of the software to accomplish the system requirement
and the interface description to match the system.

9.5.3.2 User interfaces
Specify the following:

a) The logical characteristics of each interface between the software product and its users. This includes
those configuration characteristics (e.g., required screen formats, page or window layouts, content of any
reports or menus, or availability of programmable function keys) necessary to accomplish the software
requirements.
b) All the aspects of optimizing the interface with the person who uses, maintains, or provides other support
to the system. This may simply comprise a list of do's and don'ts on how the system will appear to the
user. One example may be a requirement for the option of long or short error messages. This may also
be specified in the Software System Attributes under a section titled Ease of Use.
NOTE A style guide for the user interface can provide consistent rules for organization, coding, and interaction of the
user with the system.

9.5.3.3 Hardware interfaces
Specify the logical characteristics of each interface between the software product and the hardware elements
of the system. This includes configuration characteristics (number of ports, instruction sets, etc.). It also covers
such matters as what devices are to be supported, how they are to be supported, and protocols. For example,
terminal support may specify full-screen support as opposed to line-by-line support.

9.5.3.4 Software interfaces
Specify the use of other required software products (e.g., a data management system, an operating system,
or a mathematical package), and interfaces with other application systems (e.g., the linkage between an
accounts receivable system and a general ledger system).
For each required software product, specify:

a) Name;
b) Mnemonic;
c) Specification number;
d) Version number;
e) Source.

For each interface specify:
a) Discussion of the purpose of the interfacing software as related to this software product.
b) Definition of the interface in terms of message content and format. It is not necessary to detail any welldocumented
interface, but a reference to the document defining the interface is required. 

9.5.3.5 Communications interfaces
Specify the various interfaces to communications such as local network protocols. 

Output: 
* Training data weights
* Alert (Box + red light)
* Info of scene 
    * Time/Date
    * License plate
    * Image/video of moment

a) Training data weight output
b) If machine learning is required we will be gathering output from the training in the form of weights and biases that will influence and classify future input.
This will be used to set up the camera and it will autodetect the intersection layout from a variety of angles. If the weights and biases
are fine tuned enough we should have a good system for detection. 
c) Program will be the recipient of the output, as the output is fed back in for more training and testing.
d) 90% tolerance for how accurately the output is used to detect whether the bus has passed a red light.
<!--e) Units of measure;-->
<!--f) Timing;-->
<!--g) Relationships to other inputs/outputs;-->
<!--h) Screen formats/organization;-->
<!--i) Window formats/organization;-->
<!--j) Data formats;-->
<!--k) Command formats;-->
<!--l) Endmessages.-->

a) Alert from trigger
b) An alert should be issued via email, push notification or through the software when a bus runs a red light. 
c) User of system should recieve an alert when the issue occurs.
d) Every instance of detection the alert should send.
e) If we provide it false positives and see if it detects a static image of the offense, and issues the email to the user.
<!--f) Timing;-->
<!--g) Relationships to other inputs/outputs;-->
<!--h) Screen formats/organization;-->
<!--i) Window formats/organization;-->
<!--j) Data formats;-->
<!--k) Command formats;-->
<!--l) Endmessages.-->

a) Info of scene
b) The moment of the red light breach there should be data taken of the time, data and a visual of the scene (image or video)
c) Emailed or provided to the user via a server which would host the images.
d) Every instance of detection the info should be captured.
e) Visually inspecting the data vs real time and see if there are any discrepancies of when it is and is not outputting the signal.
<!--g) Relationships to other inputs/outputs;-->
<!--h) Screen formats/organization;-->
<!--i) Window formats/organization;-->
<!--j) Data formats;-->
<!--k) Command formats;-->
<!--l) Endmessages.-->







