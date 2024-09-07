cd $PSScriptRoot

rm pack.zip
Compress-Archive assets, pack.mcmeta, pack.png pack.zip

git add .
git status -s
$message = Read-Host "Enter Git Commit Title: "
git commit -m $message
git push -u origin main

Get-FileHash -a SHA1 pack.zip