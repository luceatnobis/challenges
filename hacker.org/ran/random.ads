generic
   type FLOAT_ITEM is digits <>;
package Random is

   procedure Set_Seed;

   procedure Force_Seed(Start_Seed : FLOAT_ITEM);

   function Get_Seed return FLOAT_ITEM;

   function Random_Number return FLOAT_ITEM;

end Random;
