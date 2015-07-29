
with Ada.Text_IO, Calendar;
use Ada.Text_IO, Calendar;

package body Random is

X_initial : FLOAT_ITEM := 0.0;
M         : FLOAT_ITEM := 1.0;
A         : FLOAT_ITEM := 7.0;
C         : FLOAT_ITEM := 13.0 / 31.0;


procedure Set_Seed is
   Time_And_Date    : TIME;
   All_Day          : DAY_DURATION;
   Minutes          : FLOAT_ITEM;
   Int_Minutes      : INTEGER;
   Part_Of_A_Minute : FLOAT_ITEM;
begin
   Time_And_Date := Clock;                -- Get the time and date
   All_Day := Seconds(Time_And_Date);     -- Seconds since midnight
   Minutes := FLOAT_ITEM(All_Day) / 60.0;   -- Floating type Minutes
   Int_Minutes := INTEGER(Minutes - 0.5); -- Integer type minutes
   Part_Of_A_Minute := FLOAT_ITEM(All_Day)
                               - 60.0 * FLOAT_ITEM(Int_Minutes);
   X_Initial := 0.1;
end Set_Seed;


procedure Force_Seed(Start_Seed : FLOAT_ITEM) is
Temp : FLOAT_ITEM;
Natural_Temp : NATURAL;
begin
   Natural_Temp := NATURAL(Start_Seed - 0.5);
   Temp := Start_Seed - FLOAT_ITEM(Natural_Temp);
   X_Initial := Start_Seed;
exception
   when Constraint_Error =>
      Put_Line("Seed out of range, ignored");
end Force_Seed;


function Get_Seed return FLOAT_ITEM is
begin
   return X_Initial;
end Get_Seed;


function Random_Number return FLOAT_ITEM is
   Temp         : FLOAT_ITEM;
   Natural_Temp : NATURAL;
begin
   Temp := A * X_Initial + C;
   Natural_Temp := NATURAL(Temp - 0.5);
   Temp := Temp - FLOAT_ITEM(Natural_Temp);
   X_Initial := Temp;
   return Temp;
end Random_Number;

end Random;
