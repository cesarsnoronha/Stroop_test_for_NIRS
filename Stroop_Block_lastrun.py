#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on März 17, 2021, at 15:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'stroop_complex'  # from the Builder filename that created this script
expInfo = {'participant': 'XXX'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='S:\\Freigegebene Ordner\\Support\\Resources\\HelpCenter - Do not edit\\PsychoPy_Experiments\\Prefrontal_Stroop_Block\\Stroop_Block_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1600, 900], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Presenter_Ins"
Presenter_InsClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text='Presenter\nPlease Test LSL Connection\n\nPress space to continue',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ready = keyboard.Keyboard()
from pylsl import StreamInfo, StreamOutlet # import required classes
info = StreamInfo(name='Trigger', type='Markers', channel_count=1, channel_format='int32', source_id='Example') # sets variables for object info
outlet = StreamOutlet(info) # initialize stream.

# Initialize components for Routine "Participant_Ins_1"
Participant_Ins_1Clock = core.Clock()
MoveOn = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Participant:\nOn each screen, Answer:\n \nDo the colors of the top letters\nmatch the meaning of the bottom word?\n    \nq (yes)          p (no)\n\nPress Space to Continue',
    font='Arial',
    pos=(0, 0), height=0.11, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Participant_Ins_2"
Participant_Ins_2Clock = core.Clock()
Moveon2 = keyboard.Keyboard()
PI_2 = visual.TextStim(win=win, name='PI_2',
    text='E.g.: Do the colors of the top letters \nmatch the meaning of the bottom word?\n\n',
    font='Arial',
    pos=(0, 0.70), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text = visual.TextStim(win=win, name='text',
    text='green',
    font='Arial',
    pos=(0.25, 0.4), height=0.2, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='red',
    font='Arial',
    pos=(-0.25, 0.4), height=0.2, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='\nred          blue\n\nno           yes',
    font='Arial',
    pos=(0, -0.1), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Participant_Ins_3"
Participant_Ins_3Clock = core.Clock()
PI_3 = visual.TextStim(win=win, name='PI_3',
    text='You will now practice 10 times\n\nThe stimuli will last for less than 2 sec\nTry to respond before the screen dissapears\n\nq (yes)    p (no)\n\n\nPress Space to Continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
MoveOn3 = keyboard.Keyboard()

# Initialize components for Routine "Prac"
PracClock = core.Clock()
ColorWordP = visual.TextStim(win=win, name='ColorWordP',
    text='',
    font='Arial',
    pos=(0, 0.25), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
WhiteWordP = visual.TextStim(win=win, name='WhiteWordP',
    text='',
    font='Arial',
    pos=(0, -0.25), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Arial',
    pos=(0, 0.25), height=0.15, wrapWidth=None, ori=0, 
    color='orange', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Arial',
    pos=(0, 0.5), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='',
    font='Arial',
    pos=(0, -0.25), height=0.15, wrapWidth=None, ori=0, 
    color='orange', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='Your answer',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "BeginTrials"
BeginTrialsClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='We will now begin the trials\n\nThey will appear in blocks\n\nStare at + sign in between trial blocks\n\nPress space when ready',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Moveon4 = keyboard.Keyboard()

# Initialize components for Routine "Trigger"
TriggerClock = core.Clock()

# Initialize components for Routine "trial"
trialClock = core.Clock()
Colorword = visual.TextStim(win=win, name='Colorword',
    text='',
    font='Arial',
    pos=[0, 0.5], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Whiteword = visual.TextStim(win=win, name='Whiteword',
    text='',
    font='Arial',
    pos=(0, -0.5), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
resp = keyboard.Keyboard()

# Initialize components for Routine "Rest_2"
Rest_2Clock = core.Clock()
Rest_ = visual.TextStim(win=win, name='Rest_',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='This is the end of the experiment.\n\nThanks!',
    font='arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Presenter_Ins"-------
continueRoutine = True
# update component parameters for each repeat
ready.keys = []
ready.rt = []
_ready_allKeys = []
# keep track of which components have finished
Presenter_InsComponents = [instrText, ready]
for thisComponent in Presenter_InsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Presenter_InsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Presenter_Ins"-------
while continueRoutine:
    # get current time
    t = Presenter_InsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Presenter_InsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if instrText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instrText.frameNStart = frameN  # exact frame index
        instrText.tStart = t  # local t and not account for scr refresh
        instrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
        instrText.setAutoDraw(True)
    
    # *ready* updates
    waitOnFlip = False
    if ready.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        ready.frameNStart = frameN  # exact frame index
        ready.tStart = t  # local t and not account for scr refresh
        ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready, 'tStartRefresh')  # time at next scr refresh
        ready.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ready.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ready.status == STARTED and not waitOnFlip:
        theseKeys = ready.getKeys(keyList=['space'], waitRelease=False)
        _ready_allKeys.extend(theseKeys)
        if len(_ready_allKeys):
            ready.keys = _ready_allKeys[-1].name  # just the last key pressed
            ready.rt = _ready_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Presenter_InsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Presenter_Ins"-------
for thisComponent in Presenter_InsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrText.started', instrText.tStartRefresh)
thisExp.addData('instrText.stopped', instrText.tStopRefresh)
# the Routine "Presenter_Ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Participant_Ins_1"-------
continueRoutine = True
# update component parameters for each repeat
MoveOn.keys = []
MoveOn.rt = []
_MoveOn_allKeys = []
# keep track of which components have finished
Participant_Ins_1Components = [MoveOn, text_2]
for thisComponent in Participant_Ins_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Participant_Ins_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Participant_Ins_1"-------
while continueRoutine:
    # get current time
    t = Participant_Ins_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Participant_Ins_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *MoveOn* updates
    waitOnFlip = False
    if MoveOn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MoveOn.frameNStart = frameN  # exact frame index
        MoveOn.tStart = t  # local t and not account for scr refresh
        MoveOn.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MoveOn, 'tStartRefresh')  # time at next scr refresh
        MoveOn.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(MoveOn.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(MoveOn.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if MoveOn.status == STARTED and not waitOnFlip:
        theseKeys = MoveOn.getKeys(keyList=['space'], waitRelease=False)
        _MoveOn_allKeys.extend(theseKeys)
        if len(_MoveOn_allKeys):
            MoveOn.keys = _MoveOn_allKeys[-1].name  # just the last key pressed
            MoveOn.rt = _MoveOn_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Participant_Ins_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Participant_Ins_1"-------
for thisComponent in Participant_Ins_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if MoveOn.keys in ['', [], None]:  # No response was made
    MoveOn.keys = None
thisExp.addData('MoveOn.keys',MoveOn.keys)
if MoveOn.keys != None:  # we had a response
    thisExp.addData('MoveOn.rt', MoveOn.rt)
thisExp.addData('MoveOn.started', MoveOn.tStartRefresh)
thisExp.addData('MoveOn.stopped', MoveOn.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "Participant_Ins_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Participant_Ins_2"-------
continueRoutine = True
# update component parameters for each repeat
Moveon2.keys = []
Moveon2.rt = []
_Moveon2_allKeys = []
# keep track of which components have finished
Participant_Ins_2Components = [Moveon2, PI_2, text, text_3, text_4]
for thisComponent in Participant_Ins_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Participant_Ins_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Participant_Ins_2"-------
while continueRoutine:
    # get current time
    t = Participant_Ins_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Participant_Ins_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Moveon2* updates
    waitOnFlip = False
    if Moveon2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Moveon2.frameNStart = frameN  # exact frame index
        Moveon2.tStart = t  # local t and not account for scr refresh
        Moveon2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Moveon2, 'tStartRefresh')  # time at next scr refresh
        Moveon2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Moveon2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Moveon2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Moveon2.status == STARTED and not waitOnFlip:
        theseKeys = Moveon2.getKeys(keyList=['space'], waitRelease=False)
        _Moveon2_allKeys.extend(theseKeys)
        if len(_Moveon2_allKeys):
            Moveon2.keys = _Moveon2_allKeys[-1].name  # just the last key pressed
            Moveon2.rt = _Moveon2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *PI_2* updates
    if PI_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PI_2.frameNStart = frameN  # exact frame index
        PI_2.tStart = t  # local t and not account for scr refresh
        PI_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PI_2, 'tStartRefresh')  # time at next scr refresh
        PI_2.setAutoDraw(True)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Participant_Ins_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Participant_Ins_2"-------
for thisComponent in Participant_Ins_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Moveon2.keys in ['', [], None]:  # No response was made
    Moveon2.keys = None
thisExp.addData('Moveon2.keys',Moveon2.keys)
if Moveon2.keys != None:  # we had a response
    thisExp.addData('Moveon2.rt', Moveon2.rt)
thisExp.addData('Moveon2.started', Moveon2.tStartRefresh)
thisExp.addData('Moveon2.stopped', Moveon2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('PI_2.started', PI_2.tStartRefresh)
thisExp.addData('PI_2.stopped', PI_2.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# the Routine "Participant_Ins_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Participant_Ins_3"-------
continueRoutine = True
# update component parameters for each repeat
MoveOn3.keys = []
MoveOn3.rt = []
_MoveOn3_allKeys = []
# keep track of which components have finished
Participant_Ins_3Components = [PI_3, MoveOn3]
for thisComponent in Participant_Ins_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Participant_Ins_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Participant_Ins_3"-------
while continueRoutine:
    # get current time
    t = Participant_Ins_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Participant_Ins_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *PI_3* updates
    if PI_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PI_3.frameNStart = frameN  # exact frame index
        PI_3.tStart = t  # local t and not account for scr refresh
        PI_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PI_3, 'tStartRefresh')  # time at next scr refresh
        PI_3.setAutoDraw(True)
    
    # *MoveOn3* updates
    waitOnFlip = False
    if MoveOn3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MoveOn3.frameNStart = frameN  # exact frame index
        MoveOn3.tStart = t  # local t and not account for scr refresh
        MoveOn3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MoveOn3, 'tStartRefresh')  # time at next scr refresh
        MoveOn3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(MoveOn3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(MoveOn3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if MoveOn3.status == STARTED and not waitOnFlip:
        theseKeys = MoveOn3.getKeys(keyList=['space'], waitRelease=False)
        _MoveOn3_allKeys.extend(theseKeys)
        if len(_MoveOn3_allKeys):
            MoveOn3.keys = _MoveOn3_allKeys[-1].name  # just the last key pressed
            MoveOn3.rt = _MoveOn3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Participant_Ins_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Participant_Ins_3"-------
for thisComponent in Participant_Ins_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('PI_3.started', PI_3.tStartRefresh)
thisExp.addData('PI_3.stopped', PI_3.tStopRefresh)
# check responses
if MoveOn3.keys in ['', [], None]:  # No response was made
    MoveOn3.keys = None
thisExp.addData('MoveOn3.keys',MoveOn3.keys)
if MoveOn3.keys != None:  # we had a response
    thisExp.addData('MoveOn3.rt', MoveOn3.rt)
thisExp.addData('MoveOn3.started', MoveOn3.tStartRefresh)
thisExp.addData('MoveOn3.stopped', MoveOn3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Participant_Ins_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TrialTypes_All.xlsx'),
    seed=None, name='Practice')
thisExp.addLoop(Practice)  # add the loop to the experiment
thisPractice = Practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in Practice:
    currentLoop = Practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Prac"-------
    continueRoutine = True
    routineTimer.add(1.750000)
    # update component parameters for each repeat
    ColorWordP.setColor(letterColor, colorSpace='rgb')
    ColorWordP.setText(colorword)
    WhiteWordP.setText(blackword)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    PracComponents = [ColorWordP, WhiteWordP, key_resp]
    for thisComponent in PracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ColorWordP* updates
        if ColorWordP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ColorWordP.frameNStart = frameN  # exact frame index
            ColorWordP.tStart = t  # local t and not account for scr refresh
            ColorWordP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ColorWordP, 'tStartRefresh')  # time at next scr refresh
            ColorWordP.setAutoDraw(True)
        if ColorWordP.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ColorWordP.tStartRefresh + 1.75-frameTolerance:
                # keep track of stop time/frame for later
                ColorWordP.tStop = t  # not accounting for scr refresh
                ColorWordP.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ColorWordP, 'tStopRefresh')  # time at next scr refresh
                ColorWordP.setAutoDraw(False)
        
        # *WhiteWordP* updates
        if WhiteWordP.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            WhiteWordP.frameNStart = frameN  # exact frame index
            WhiteWordP.tStart = t  # local t and not account for scr refresh
            WhiteWordP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(WhiteWordP, 'tStartRefresh')  # time at next scr refresh
            WhiteWordP.setAutoDraw(True)
        if WhiteWordP.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > WhiteWordP.tStartRefresh + 1.75-frameTolerance:
                # keep track of stop time/frame for later
                WhiteWordP.tStop = t  # not accounting for scr refresh
                WhiteWordP.frameNStop = frameN  # exact frame index
                win.timeOnFlip(WhiteWordP, 'tStopRefresh')  # time at next scr refresh
                WhiteWordP.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 1.75-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['q', 'p'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac"-------
    for thisComponent in PracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice.addData('ColorWordP.started', ColorWordP.tStartRefresh)
    Practice.addData('ColorWordP.stopped', ColorWordP.tStopRefresh)
    Practice.addData('WhiteWordP.started', WhiteWordP.tStartRefresh)
    Practice.addData('WhiteWordP.stopped', WhiteWordP.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    Practice.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        Practice.addData('key_resp.rt', key_resp.rt)
    Practice.addData('key_resp.started', key_resp.tStartRefresh)
    Practice.addData('key_resp.stopped', key_resp.tStopRefresh)
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_5.setText(corrAns
)
    text_6.setText('Correct answer')
    text_7.setText(key_resp.keys
)
    # keep track of which components have finished
    feedbackComponents = [text_5, text_6, text_7, text_8]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice.addData('text_5.started', text_5.tStartRefresh)
    Practice.addData('text_5.stopped', text_5.tStopRefresh)
    Practice.addData('text_6.started', text_6.tStartRefresh)
    Practice.addData('text_6.stopped', text_6.tStopRefresh)
    Practice.addData('text_7.started', text_7.tStartRefresh)
    Practice.addData('text_7.stopped', text_7.tStopRefresh)
    Practice.addData('text_8.started', text_8.tStartRefresh)
    Practice.addData('text_8.stopped', text_8.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Practice'

# get names of stimulus parameters
if Practice.trialList in ([], [None], None):
    params = []
else:
    params = Practice.trialList[0].keys()
# save data for this loop
Practice.saveAsExcel(filename + '.xlsx', sheetName='Practice',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "BeginTrials"-------
continueRoutine = True
# update component parameters for each repeat
Moveon4.keys = []
Moveon4.rt = []
_Moveon4_allKeys = []
# keep track of which components have finished
BeginTrialsComponents = [text_9, Moveon4]
for thisComponent in BeginTrialsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BeginTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BeginTrials"-------
while continueRoutine:
    # get current time
    t = BeginTrialsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BeginTrialsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *Moveon4* updates
    waitOnFlip = False
    if Moveon4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Moveon4.frameNStart = frameN  # exact frame index
        Moveon4.tStart = t  # local t and not account for scr refresh
        Moveon4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Moveon4, 'tStartRefresh')  # time at next scr refresh
        Moveon4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Moveon4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Moveon4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Moveon4.status == STARTED and not waitOnFlip:
        theseKeys = Moveon4.getKeys(keyList=['space'], waitRelease=False)
        _Moveon4_allKeys.extend(theseKeys)
        if len(_Moveon4_allKeys):
            Moveon4.keys = _Moveon4_allKeys[-1].name  # just the last key pressed
            Moveon4.rt = _Moveon4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BeginTrialsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BeginTrials"-------
for thisComponent in BeginTrialsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
# check responses
if Moveon4.keys in ['', [], None]:  # No response was made
    Moveon4.keys = None
thisExp.addData('Moveon4.keys',Moveon4.keys)
if Moveon4.keys != None:  # we had a response
    thisExp.addData('Moveon4.rt', Moveon4.rt)
thisExp.addData('Moveon4.started', Moveon4.tStartRefresh)
thisExp.addData('Moveon4.stopped', Moveon4.tStopRefresh)
thisExp.nextEntry()
# the Routine "BeginTrials" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ConditionFile.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Trigger"-------
    continueRoutine = True
    # update component parameters for each repeat
    outlet.push_sample(x=[congruent])
    # keep track of which components have finished
    TriggerComponents = []
    for thisComponent in TriggerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TriggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trigger"-------
    while continueRoutine:
        # get current time
        t = TriggerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TriggerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TriggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trigger"-------
    for thisComponent in TriggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Trigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_Loop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(Condition_File),
        seed=None, name='trials_Loop')
    thisExp.addLoop(trials_Loop)  # add the loop to the experiment
    thisTrials_Loop = trials_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Loop.rgb)
    if thisTrials_Loop != None:
        for paramName in thisTrials_Loop:
            exec('{} = thisTrials_Loop[paramName]'.format(paramName))
    
    for thisTrials_Loop in trials_Loop:
        currentLoop = trials_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_Loop.rgb)
        if thisTrials_Loop != None:
            for paramName in thisTrials_Loop:
                exec('{} = thisTrials_Loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(1.750000)
        # update component parameters for each repeat
        Colorword.setColor(letterColor, colorSpace='rgb')
        Colorword.setText(colorword)
        Whiteword.setText(blackword)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [Colorword, Whiteword, resp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Colorword* updates
            if Colorword.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Colorword.frameNStart = frameN  # exact frame index
                Colorword.tStart = t  # local t and not account for scr refresh
                Colorword.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Colorword, 'tStartRefresh')  # time at next scr refresh
                Colorword.setAutoDraw(True)
            if Colorword.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Colorword.tStartRefresh + 1.75-frameTolerance:
                    # keep track of stop time/frame for later
                    Colorword.tStop = t  # not accounting for scr refresh
                    Colorword.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Colorword, 'tStopRefresh')  # time at next scr refresh
                    Colorword.setAutoDraw(False)
            
            # *Whiteword* updates
            if Whiteword.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Whiteword.frameNStart = frameN  # exact frame index
                Whiteword.tStart = t  # local t and not account for scr refresh
                Whiteword.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Whiteword, 'tStartRefresh')  # time at next scr refresh
                Whiteword.setAutoDraw(True)
            if Whiteword.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Whiteword.tStartRefresh + 1.75-frameTolerance:
                    # keep track of stop time/frame for later
                    Whiteword.tStop = t  # not accounting for scr refresh
                    Whiteword.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Whiteword, 'tStopRefresh')  # time at next scr refresh
                    Whiteword.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 1.75-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['q', 'p'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # was this correct?
                    if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                        resp.corr = 1
                    else:
                        resp.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_Loop.addData('Colorword.started', Colorword.tStartRefresh)
        trials_Loop.addData('Colorword.stopped', Colorword.tStopRefresh)
        trials_Loop.addData('Whiteword.started', Whiteword.tStartRefresh)
        trials_Loop.addData('Whiteword.stopped', Whiteword.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_Loop (TrialHandler)
        trials_Loop.addData('resp.keys',resp.keys)
        trials_Loop.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            trials_Loop.addData('resp.rt', resp.rt)
        trials_Loop.addData('resp.started', resp.tStartRefresh)
        trials_Loop.addData('resp.stopped', resp.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_Loop'
    
    # get names of stimulus parameters
    if trials_Loop.trialList in ([], [None], None):
        params = []
    else:
        params = trials_Loop.trialList[0].keys()
    # save data for this loop
    trials_Loop.saveAsExcel(filename + '.xlsx', sheetName='trials_Loop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "Rest_2"-------
    continueRoutine = True
    routineTimer.add(15.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Rest_2Components = [Rest_]
    for thisComponent in Rest_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Rest_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Rest_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Rest_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Rest_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Rest_* updates
        if Rest_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Rest_.frameNStart = frameN  # exact frame index
            Rest_.tStart = t  # local t and not account for scr refresh
            Rest_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Rest_, 'tStartRefresh')  # time at next scr refresh
            Rest_.setAutoDraw(True)
        if Rest_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Rest_.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                Rest_.tStop = t  # not accounting for scr refresh
                Rest_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Rest_, 'tStopRefresh')  # time at next scr refresh
                Rest_.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Rest_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Rest_2"-------
    for thisComponent in Rest_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Rest_.started', Rest_.tStartRefresh)
    trials.addData('Rest_.stopped', Rest_.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if thanksText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.tStart = t  # local t and not account for scr refresh
        thanksText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanksText, 'tStartRefresh')  # time at next scr refresh
        thanksText.setAutoDraw(True)
    if thanksText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanksText.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            thanksText.tStop = t  # not accounting for scr refresh
            thanksText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanksText, 'tStopRefresh')  # time at next scr refresh
            thanksText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanksText.started', thanksText.tStartRefresh)
thisExp.addData('thanksText.stopped', thanksText.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
