rm pack.zip
Compress-Archive assets, pack.mcmeta, pack.png pack.zip
Get-FileHash -a SHA1 pack.zip