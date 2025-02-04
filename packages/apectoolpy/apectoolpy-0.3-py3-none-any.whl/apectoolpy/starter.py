def generate():
    return '''
*NAMEDPLANE    
   ELEV: Y1   , 3, 0.001, 0
   ELEV: Y2   , 3, 0.001, 1
   ELEV: Y3   , 3, 0.001, 2
   ELEV: Y4   , 3, 0.001, 3
   ELEV: X1   , 4, 0.001, 0
   ELEV: X2   , 4, 0.001, 1
   ELEV: X3   , 4, 0.001, 2
   ELEV: X4   , 4, 0.001, 3
   PLAN: BASE, 2, 0.0009144, 0
   PLAN: 2F  , 2, 0.0009144, 3
   PLAN: 3F  , 2, 0.0009144, 6
   PLAN: 4F  , 2, 0.0009144, 9
   PLAN: 5F  , 2, 0.0009144, 12

*MATERIAL    
    1, CONC , Grade C4000       , 0, 0, , F, NO, 0.05, 1, ASTM19(RC) ,            , Grade C4000   , NO, 2.51255e+07
    2, STEEL, A36               , 0, 0, , F, NO, 0.02, 1, ASTM09(S)  ,            , A36           , NO, 1.99948e+08


*STLDCASE    ; Static Load Cases
; LCNAME, LCTYPE, DESC
DL   , D , Selfweight
SDL  , D , Super-imposed Dead load
H  , EP , Lateral Earth Pressure
LL   , L , Live Load
LLm  , L , Live Load (MEP)
LLs  , L , Live Storage
LR   , LR, Roof live load
Ex   , E , Earthquake load at x
Ex + , E , Earthquake load at x (+ ecc)
Ex - , E , Earthquake load at x (- ecc)
Ey   , E , Earthquake load at y
Ey + , E , Earthquake load at y (+ ecc)
Ey - , E , Earthquake load at y (- ecc)
Wxmax  , W , Considers max wind load pressure
Wxmin  , W , Considers min wind load pressure
Wymax   , W , Considers max wind load pressure
Wymin + , W , Considers min wind load pressure

*USE-STLD, DL

*SELFWEIGHT    ; Self Weight
; X, Y, Z, GROUP
0, 0, -1,

; End of data for load case [DL] -------------------------

*LOADTOMASS   
   XY, YES, YES, YES, YES, 9.806
   DL, 1, SDL, 1, LLm, 1.0, LLs, 0.25
   '''