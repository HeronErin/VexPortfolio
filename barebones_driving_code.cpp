/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Project:      Better moter controll                                     */
/*    Module:       main.cpp                                                  */
/*    Author:       Mitchell                                                  */
/*    Created:      Fri Jan 28 2022                                           */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// Copyright (C) 2023 HeronErin

// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License as
// published by the Free Software Foundation; either version 3 of the
// License, or (at your option) any later version.

// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.


// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Controller1          controller                    
// Motor1               motor         1               
// Motor2               motor         2               
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"
#include <stdlib.h>

using namespace vex;
const bool INVERT_MOTER_ONE = false;

const bool INVERT_MOTER_TWO  = false;

const bool INVERT_TURNING = false;

const bool USE_SAME_STICK_FOR_TURNING = true;




void movementCallback(){

    // Get joystick amounts and conver to float for calculations
   float speed = (float)Controller1.Axis3.position();
   float turn;
    if (USE_SAME_STICK_FOR_TURNING)
        turn =  (float)Controller1.Axis4.position();
    else
        turn =  (float)Controller1.Axis1.position();

    // variables for inverting
    int moterOneMult = 1; if (INVERT_MOTER_ONE) moterOneMult=-1;
    int moterTwoMult = 1; if (INVERT_MOTER_TWO) moterTwoMult=-1;

    if (INVERT_TURNING) turn*=-1;


    if (speed != 0){
        // Set one side to speed while setting other side to percentage of speed var based on turn direction
        int ispeed = (int) speed;
        if (turn > 0){
            Motor1.setVelocity(moterOneMult*ispeed                               , percent);
            Motor2.setVelocity(moterTwoMult*((int)(speed * (1- turn/100)))       , percent);
        }else{
            Motor1.setVelocity(moterOneMult*((int)(speed * (1- fabs(turn)/100))) , percent);
            Motor2.setVelocity(moterTwoMult*ispeed                               , percent);
          }
    }else{   
        // use opposing motors to turn without forward momentum
        Motor1.setVelocity(     moterOneMult*((int)turn), percent);
        Motor2.setVelocity(-1*  moterTwoMult*((int)turn), percent);
      }
}


int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();


  Controller1.Axis1.changed(movementCallback);
  Controller1.Axis3.changed(movementCallback);
  Controller1.Axis4.changed(movementCallback);
  
}
