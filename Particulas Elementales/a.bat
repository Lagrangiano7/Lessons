setlocal enabledelayedexpansion

echo Convirtiendo notebooks a PDF en paralelo...
echo.

for %%F in ("[1-9]*.ipynb") do (
    echo Lanzando conversion de: %%F
    start cmd /k py -m nbconvert --to pdf "%%F"
)

echo.
echo Todos los procesos han sido lanzados.
pause