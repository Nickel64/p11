import cv2 as cv

from controller.observer import Observer


class DebugGUI:

    ui_name = "Bus-Factor"
    classifications = None
    confidence_threshold = 0.01
    frame = None

    bus_colour = (0, 191, 255)
    not_bus_colour = (0, 0, 0)

    # points of line
    linePt = []
    # points for traffic light
    rectPt = []

    # booleans for whether you should draw a new line/rect or not
    # false means draw, else true means its in process of being drawn).
    line = False
    rect = False

    #the objects
    line_obj = None
    rect_obj = None
    intersects = False

    #the chosen tool, -1 for none, 0 for rectangle, 1 for line
    line_tool = True

    def __init__(self):
        self.frame = None
        # cv.createButton('toolToggle', self.toggleTools, 0,, 1);

        #self.play()

    def update_line(self):
        return self.linePt

    def update_classifications(self, classifications):
        self.classifications = classifications

    def update_rect(self):
        return self.linePt

    def update_collision_boolean(self):
        return self.intersects


    def toggleTools(self):
        pass

    """
        Method is responsible for performing the correct actions depending on 
        the mouse event passed in. First it checks the appropriate tool being used.
        Then, it will mark the first point of the shape and follow the mouse until 
        it is released where it records the second point. 
    """
    def click_and_crop(self, event, x, y, flags, params):

        if event == cv.EVENT_RBUTTONDOWN:
            self.line_tool = not self.line_tool

        if self.line_tool:
            if event == cv.EVENT_MOUSEMOVE and self.line:
                self.linePt.append((x, y))
            if event == cv.EVENT_LBUTTONDOWN:
                self.linePt = [(x, y)]
                self.line = True
                # check to see if the left mouse button was released
            elif event == cv.EVENT_LBUTTONUP:
                # record the ending (x, y) coordinates
                self.linePt[1] = (x, y)
                self.line = False
        elif not self.line_tool:
            print('enters')
            if event == cv.EVENT_MOUSEMOVE and self.rect:
                self.rectPt.append((x, y))
            if event == cv.EVENT_LBUTTONDOWN:
                self.rectPt = [(x, y)]
                self.rect = True
                # check to see if the left mouse button was released
            elif event == cv.EVENT_LBUTTONUP:
                # record the ending (x, y) coordinates
                self.rectPt[1] = (x, y)
                self.rect = False



    def update_frame(self, frame):
        """
            Updates the frame by drawing the line and/or rectangle shape using the information
            stored from the user's clicks.
        """
        self.frame = frame
        self.draw_classifications_on_frame()
        cv.setMouseCallback(self.ui_name, self.click_and_crop)

        print("X:" + str(self.linePt))
        if len(self.linePt) > 1:
            self.line_obj = cv.line(self.frame, self.linePt[0], self.linePt[1], (0, 255, 0), 5)
        if len(self.rectPt) > 1:
            self.rect_obj = cv.rectangle(self.frame, self.rectPt[0], self.rectPt[1], (0,0,255), 5)

        cv.imshow(self.ui_name, self.frame)



    def draw_classifications_on_frame(self):
        """
            Method to display a box around a classified object, using the points from the
            classifications made by the model.
            tl = top left of classification box.
            br = bottom right of classification box.
        """

        if self.classifications is None or self.frame is None: return
        # check every detected object
        for i in range(0, len(self.classifications)):
            c = self.classifications[i]
            # confidence level of detected object has to be above threshold
            if c.conf > self.confidence_threshold:

                smallBox = self.small_box(c.tl.get('x'), c.tl.get('y'), c.br.get('x'), c.br.get('y'))

                if c.label == "bus":
                    rect = cv.rectangle(self.frame, (c.tl.get('x'), c.tl.get('y')), (c.br.get('x'), c.br.get('y')), self.bus_colour, 2)
                    if(self.detect_event(smallBox[0][0], smallBox[0][1], smallBox[1][0], smallBox[1][1])):
                        # event has been detected, increment counter
                        print("bus has past the intersection")
                        self.intersects = True
                    else:
                        # Reset intersection boolean
                        self.intersects = False
                    cv.putText(self.frame, c.label,(c.tl.get('x'), c.tl.get('y') + 15), cv.FONT_HERSHEY_SIMPLEX, 0.7, self.bus_colour, 2)
                else:
                    rect = cv.rectangle(self.frame, (c.tl.get('x'), c.tl.get('y')), (c.br.get('x'), c.br.get('y')), self.not_bus_colour, 2)
                    # self.detect_event(c.tl.get('x'), c.tl.get('y'), c.br.get('x'), c.br.get('y')) - bounding for bix box
                    self.detect_event(smallBox[0][0], smallBox[0][1], smallBox[1][0], smallBox[1][1])
                    cv.putText(self.frame, c.label, (c.tl.get('x'), c.tl.get('y') + 15), cv.FONT_HERSHEY_SIMPLEX, 0.7, self.not_bus_colour, 2)


    def small_box(self, x1: int, y1: int, x2: int, y2: int):
        """
            This returns the top left and bottom right coordinates that define a small bounding box
            that make up a certain percentage. x1, y1 are top left, x2, y2 are bottom right.
        """
        width = abs(x2-x1)
        height = abs(y2-y1)

        percentageToRemove = 0.3
        removedSectionWidth = width * percentageToRemove
        removedSectionHeight = height * percentageToRemove

        newX1 = int(removedSectionWidth + x1)
        newY1 = int(removedSectionHeight + y1)
        newX2 = int(x2 - removedSectionWidth)
        newY2 = int(y2 - removedSectionHeight)

        rectangle = cv.rectangle(self.frame, (newX1, newY1), (newX2, newY2), self.bus_colour, 2)
        return [(newX1, newY1), (newX2, newY2)]


    def detect_event(self, x1: int, y1: int, x2: int, y2: int):
        """
            Method to check if a classified object is intersecting the intersection
            line specified by the user. point (x1, y2) are top left and (x2, y2)
            is bottom right of rectangle.
        """
        if(self.linePt != None):
            if(len(self.linePt) >= 2):

                lineXPoints = []
                lineYPoints = []

                xWidth = (self.linePt[1][0] - self.linePt[0][0])
                yWidth = (self.linePt[1][1] - self.linePt[0][1])

                xIteration = (xWidth/50)
                yIteration = (yWidth/50)

                #Required to account for different directions that the line can be drawn.
                currentXPoint = self.linePt[1][0]
                currentYPoint = self.linePt[1][1]
                yIteration = yIteration * -1
                xIteration = xIteration * -1

                #Iterates through the line and selects 50 intervals/points.
                for i in range(50):
                    lineXPoints.append(currentXPoint)
                    lineYPoints.append(currentYPoint)
                    currentXPoint += xIteration
                    currentYPoint += yIteration

                #Iterates through the 50 points and checks if the point is within the box, if it is then
                #we can determine that the object intersects the line.
                for i in range(50):
                    if(self.contains(x1, y1, x2, y2, int(lineXPoints[i]), int(lineYPoints[i]))):
                        self.intersects = True
                        print(lineXPoints[i])
                        cv.circle(self.frame, (int(lineXPoints[i]), int(lineYPoints[i])), 5, (244, 40, 0))



    def contains(self, x1: int, y1: int, x2: int, y2: int, px: int, py: int):
        """
            Check if point (px, py) is contained within rectangle [(x1, y1), (x2, y2)],
            where points are top left and bottom right respectively.
        """
        return x1 < px < x2 and y1 < py < y2

    def play(self):
        while True:
            if self.frame is None:
                print("None")
                continue
            cv.imshow(self.ui_name, self.frame)
            # waits forever for the esc key to be pressed before exiting
            if cv.waitKey(50) == 27:
                break  # esc to quit
        cv.destroyAllWindows()