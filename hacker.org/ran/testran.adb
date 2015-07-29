with Ada.Text_IO, Random;
use Ada.Text_IO;

procedure TestRan is

   package My_Random is new Random(FLOAT);
   use My_Random;

   package Int_IO is new Ada.Text_IO.Integer_IO(INTEGER);
   use Int_IO;
   package Flt_IO is new Ada.Text_IO.Float_IO(FLOAT);
   use Flt_IO;

   SIZE : constant := 100;
   type MY_ARRAY is array(1..SIZE) of INTEGER;
   Events   : MY_ARRAY;
   Int_Rand : INTEGER;

begin
   Set_Seed;
   for Index in 1..2 loop
      Put(Random_Number, 2, 6, 0);
   end loop;

end TestRan;
