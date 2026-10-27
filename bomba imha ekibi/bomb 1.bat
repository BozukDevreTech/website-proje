@echo off
title Sifre Dogrulama
color a
set sifre=ABC123

REM set a=00
REM set b=05
REM goto basla

REM :basla
REM cls


REM if %b%==0 goto algoritma
REM ) else (
REM goto devam1
REM :devam1
REM echo.
REM echo.
REM set /a b-=1
REM ) else (
REM goto devam
REM :devam
REM echo ^	^ ---------
REM echo ^	^ } %a%:%b% {
REM echo ^	^ ---------

REM timeout /t 1 >nul
REM goto basla
REM :algoritma

REM echo.
REM echo.
REM echo ^	^ ---------
REM echo ^	^ } 00:00 {
REM echo ^	^ ---------

REM pause  >nul

:gir
cls
echo ^	Lutfen sifreyi girin
timeout /t 2 >nul
start yardimci.vbs
timeout /t 12 >nul
start sifre123.vbs

set /p girilensifre=


rem Şifreyi doğrula
if %girilensifre% == %sifre% (
echo.
echo.
echo.
echo.
  echo ^	^	Sifre dogru!
  timeout /t 2 >nul
  echo.
  echo ^	^	TEBRIKLER
  timeout /t 1 >nul
  echo.
  echo ^	Bomba basariyla imha edildi.
  timeout /t 2 >nul
  echo.
  echo.
  pause
  exit
) else (
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
color c
  echo ^	Bomba patladi
  timeout /t 2 >nul
  echo ^	Oyunu Kaybettiniz
echo.
  rem timeout /t komutu "1" zaman birimi olarak bekler. Bu işaret '>' , ekran çıktısını bir dosyaya yönlendirir ve bu sayede "pause ve timeout" gibi komutların ekranda gösterdiği yazıyı görüntülenmez.
  timeout /t 2 >nul
  color 7
  pause
  goto gir
)
