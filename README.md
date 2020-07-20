# CyclePet
Take care of a pet using coins earned by exercising, a work in progress 
<p align="center">
  <img src="images/Capture.PNG" width="450" title="early screenshot">
</p>

# Libraries used

- [pygame](https://www.pygame.org/) Game rendering and event tracking
- [pygame_gui](https://pygame-gui.readthedocs.io/en/latest/quick_start.html) Buttons and UI styling
- [requests](https://requests.readthedocs.io/en/master/) HTTP requests for strava API use

### Included with most python distributions
- [Pickle](https://docs.python.org/3/library/pickle.html) Save states
- [Webbrowser](https://docs.python.org/3/library/webbrowser.html) Link opening for API authorization 
- [Time](https://docs.python.org/3/library/time.html) Measure passing of time


# How to Run

Requires knowledge of your platforms command line 

1. Download github as .zip

2. Extract files into a new folder, navigate to directory using 

``` 
cd \path
```
3. Use pip to install packages

```
pip install -r requirements.txt

or 

pip3 install -r requirements.txt
```
4. Run program
```
python gui.py

or

python3 gui.py
```

# Releases
<b> Current Version : 0.1 </b>
  
 
### 0.1

  - Pet animations
  - Background upgrades
  - Play with your pet to increase happiness
  
  
### 0.0
  - API integration
  - Basic pet health mechanics
  - Save/Load current pet
  - Placeholder art
  
  
  
  
  
 # Todo
 - [ ]  Sound / music
 - [ ]  Food animations
 - [ ]  Settings screen
 - [ ]  Catch Connection problems
 - [ ]  Cast age into days or years
 - [ ]  Shop UI
 - [ ]  Different pet art
 - [ ]  requirements.txt pip install
 - [ ]  Remove pygame_UI to allow for pyinstaller distribution
 - [ ]  Name of pet in UI
 - [ ]  Clean up imports

 
<p align="center">
  <img src="images/api_logo_pwrdBy_strava_horiz_gray.png" width="450" title="api credit">
</p>

