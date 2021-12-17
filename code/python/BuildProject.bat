set projectpath="C:\Users\nicka\OneDrive\Documents\School\Capstone\Program\UnityProject\Capstone"
set buildpath="C:\Users\nicka\OneDrive\Documents\School\Capstone\Program\build"
set logpath="C:\Users\nicka\OneDrive\Documents\School\Capstone\Program\log.txt"
"C:\Program Files\Unity\Hub\Editor\2019.4.33f1\Editor\Unity.exe" -quit -batchmode -projectpath %projectpath% -exectuteMethod Capstone.Build.BuildProject -outputPath %buildpath% -buildTarget Win64 -logFile %logpath%