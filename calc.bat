@echo off
title OpenSystem v 0.5
echo witaj w systemie

:start
title OpenSystem
echo.
echo menu start
echo 1) +
echo 2) -
echo 3) *
echo 4) :
 
set/p start="wybierz z opcji nr 1-4: "
if %start% == 1 goto 1
if %start% == 2 goto 2
if %start% == 3 goto 3
if %start% == 4 goto 4
 
echo error #1- menu główne %date%  >>%homedrive%\system\priv\bledy.txt && goto error
