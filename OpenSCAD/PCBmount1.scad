Width=98;
HoleDistance=84;
Height=15;
Thickness=2.5;
HoleDiameter=3.5;

HolePosY=Height/2;
HolePosX1=(Width-HoleDistance)/2;
HolePosX2=Width/2;
HolePosX3=Width-((Width-HoleDistance)/2);


module braket(){
    difference(){
        union(){
            cube([Width,Height,Thickness]);
            cube([Width,Thickness,2*Thickness]);
        }
        holes();
        translate([0,-1,0]){
            rotate([0,-45,0]){
               cube(Height+2);
            } 
        }
        translate([Width,-1,0]){
            rotate([0,-45,0]){
               cube(Height+2);
            } 
        }
    }
}

module holes(){
    hexHole(HolePosX1,HolePosY,HoleDiameter);
    sunkenHole(HolePosX2,HolePosY+1,HoleDiameter);
    hexHole(HolePosX3,HolePosY,HoleDiameter);
}

module simpleHole(x,y,dia){
    translate([x,y,0]){
        cylinder(3*Thickness,d=d,center=true,$fn=180);
    }
}

module sunkenHole(x,y,dia){
    union(){
       simpleHole(x,y,dia);
       translate([x,y,0]){
            cylinder(Thickness,d=2*dia,center=true,$fn=180);
        }
    }
}

module hexHole(x,y,dia){
    union(){
       simpleHole(x,y,dia);
       translate([x,y,(6*Thickness/5)]){
            cylinder(Thickness,d=5.5,center=true,$fn=6);
        }
    }
}

braket();