HEAD_FILL = "-" * 101 * 16

full = """
----------------------------------------11111111111111111111----------------------------------------
--------------------------------------11--------------------11--------------------------------------
-------------------------------------1-----1------------1-----1-------------------------------------
-------------------------------------1----1-1----------1-1----1-------------------------------------
-------------------------------------1----1-1----------1-1----1-------------------------------------
-------------------------------------1-----1---1----1---1-----1-------------------------------------
-------------------------------------1----------1111----------1-------------------------------------
--------------------------------------11--------------------11--------------------------------------
----------------------------------------11111111111111111111----------------------------------------
-------------------------------------------------11-------------------------------------------------
-----------------------------------------------111111-----------------------------------------------
----------------------------------------------1--11--1----------------------------------------------
---------------------------------------------1---11---1---------------------------------------------
--------------------------------------------1----11----1--------------------------------------------
-------------------------------------------1-----11-----1-------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
------------------------------------------------1--1------------------------------------------------
-----------------------------------------------1----1-----------------------------------------------
-----------------------------------------------1----1-----------------------------------------------
-----------------------------------------------1----1-----------------------------------------------"""

blink = """
----------------------------------------11111111111111111111----------------------------------------
--------------------------------------11--------------------11--------------------------------------
-------------------------------------1------------------------1-------------------------------------
-------------------------------------1----111----------111----1-------------------------------------
-------------------------------------1----111----------111----1-------------------------------------
-------------------------------------1---------1----1---------1-------------------------------------
-------------------------------------1----------1111----------1-------------------------------------
--------------------------------------11--------------------11--------------------------------------
----------------------------------------11111111111111111111----------------------------------------
-------------------------------------------------11-------------------------------------------------
-----------------------------------------------111111-----------------------------------------------
----------------------------------------------1--11--1----------------------------------------------
---------------------------------------------1---11---1---------------------------------------------
--------------------------------------------1----11----1--------------------------------------------
-------------------------------------------1-----11-----1-------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
------------------------------------------------1--1------------------------------------------------
-----------------------------------------------1----1-----------------------------------------------
-----------------------------------------------1----1-----------------------------------------------
-----------------------------------------------1----1-----------------------------------------------"""

dead = """
----------------------------------------11111111111111111111----------------------------------------
--------------------------------------11--------------------11--------------------------------------
-------------------------------------1---1---1--------1---1---1-------------------------------------
-------------------------------------1----111----------111----1-------------------------------------
-------------------------------------1---1---1--------1---1---1-------------------------------------
-------------------------------------1------------------------1-------------------------------------
-------------------------------------1----------1111----------1-------------------------------------
--------------------------------------11-------1----1-------11--------------------------------------
----------------------------------------11111111111111111111----------------------------------------
-------------------------------------------------11-------------------------------------------------
-----------------------------------------------111111-----------------------------------------------
----------------------------------------------1--11--1----------------------------------------------
---------------------------------------------1---11---1---------------------------------------------
--------------------------------------------1----11----1--------------------------------------------
-------------------------------------------1-----11-----1-------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
------------------------------------------------1--1------------------------------------------------
-----------------------------------------------1----1-----------------------------------------------
-----------------------------------------------1----1-----------------------------------------------
-----------------------------------------------1----1-----------------------------------------------"""

head = """
----------------------------------------11111111111111111111----------------------------------------
--------------------------------------11--------------------11--------------------------------------
-------------------------------------1------------------------1-------------------------------------
-------------------------------------1------------------------1-------------------------------------
-------------------------------------1------------------------1-------------------------------------
-------------------------------------1------------------------1-------------------------------------
-------------------------------------1------------------------1-------------------------------------
--------------------------------------11--------------------11--------------------------------------
----------------------------------------11111111111111111111----------------------------------------""" + HEAD_FILL

head_w_eyes = """
----------------------------------------11111111111111111111----------------------------------------
--------------------------------------11--------------------11--------------------------------------
-------------------------------------1-----1------------1-----1-------------------------------------
-------------------------------------1----1-1----------1-1----1-------------------------------------
-------------------------------------1----1-1----------1-1----1-------------------------------------
-------------------------------------1-----1------------1-----1-------------------------------------
-------------------------------------1------------------------1-------------------------------------
--------------------------------------11--------------------11--------------------------------------
----------------------------------------11111111111111111111----------------------------------------""" + HEAD_FILL

body = """
----------------------------------------11111111111111111111----------------------------------------
--------------------------------------11--------------------11--------------------------------------
-------------------------------------1-----1------------1-----1-------------------------------------
-------------------------------------1----1-1----------1-1----1-------------------------------------
-------------------------------------1----1-1----------1-1----1-------------------------------------
-------------------------------------1-----1---1----1---1-----1-------------------------------------
-------------------------------------1----------1111----------1-------------------------------------
--------------------------------------11--------------------11--------------------------------------
----------------------------------------11111111111111111111----------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------"""

one_arm = """
----------------------------------------11111111111111111111----------------------------------------
--------------------------------------11--------------------11--------------------------------------
-------------------------------------1-----1------------1-----1-------------------------------------
-------------------------------------1----1-1----------1-1----1-------------------------------------
-------------------------------------1----1-1----------1-1----1-------------------------------------
-------------------------------------1-----1---1----1---1-----1-------------------------------------
-------------------------------------1----------1111----------1-------------------------------------
--------------------------------------11--------------------11--------------------------------------
----------------------------------------11111111111111111111----------------------------------------
-------------------------------------------------11-------------------------------------------------
-----------------------------------------------1111-------------------------------------------------
----------------------------------------------1--11-------------------------------------------------
---------------------------------------------1---11-------------------------------------------------
--------------------------------------------1----11-------------------------------------------------
-------------------------------------------1-----11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------"""

arms = """
----------------------------------------11111111111111111111----------------------------------------
--------------------------------------11--------------------11--------------------------------------
-------------------------------------1-----1------------1-----1-------------------------------------
-------------------------------------1----1-1----------1-1----1-------------------------------------
-------------------------------------1----1-1----------1-1----1-------------------------------------
-------------------------------------1-----1---1----1---1-----1-------------------------------------
-------------------------------------1----------1111----------1-------------------------------------
--------------------------------------11--------------------11--------------------------------------
----------------------------------------11111111111111111111----------------------------------------
-------------------------------------------------11-------------------------------------------------
-----------------------------------------------111111-----------------------------------------------
----------------------------------------------1--11--1----------------------------------------------
---------------------------------------------1---11---1---------------------------------------------
--------------------------------------------1----11----1--------------------------------------------
-------------------------------------------1-----11-----1-------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------"""

one_leg = """
----------------------------------------11111111111111111111----------------------------------------
--------------------------------------11--------------------11--------------------------------------
-------------------------------------1-----1------------1-----1-------------------------------------
-------------------------------------1----1-1----------1-1----1-------------------------------------
-------------------------------------1----1-1----------1-1----1-------------------------------------
-------------------------------------1-----1---1----1---1-----1-------------------------------------
-------------------------------------1----------1111----------1-------------------------------------
--------------------------------------11--------------------11--------------------------------------
----------------------------------------11111111111111111111----------------------------------------
-------------------------------------------------11-------------------------------------------------
-----------------------------------------------111111-----------------------------------------------
----------------------------------------------1--11--1----------------------------------------------
---------------------------------------------1---11---1---------------------------------------------
--------------------------------------------1----11----1--------------------------------------------
-------------------------------------------1-----11-----1-------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
-------------------------------------------------11-------------------------------------------------
------------------------------------------------1---------------------------------------------------
-----------------------------------------------1----------------------------------------------------
-----------------------------------------------1----------------------------------------------------
-----------------------------------------------1----------------------------------------------------"""

win_frame = """
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------Y-O-U-------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
-----------------------------------------------------------W--i-----N!!-----------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------"""

wrong = """
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------W-R-O-N-G-!-!-!-!-!-!---------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------"""

lose = """
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------YOU LOSE!!!!!!!!!!!!!---------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------"""



flash = "1" * 101 * 25
clear = "-" * 101 * 25
head_full = full[:101 * 9 + 1] + HEAD_FILL