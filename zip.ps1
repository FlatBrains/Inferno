cd $PSScriptRoot

rm pack.zip
Compress-Archive assets, pack.mcmeta, pack.png pack.zip

git add .
git commit #exit by pressing esc and then :wq!
git push -u origin main

Get-FileHash -a SHA1 pack.zip