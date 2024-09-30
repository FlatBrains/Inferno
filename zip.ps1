cd $PSScriptRoot

rm pack.zip
#Compress-Archive assets, pack.mcmeta, pack.png pack.zip -CompressionLevel Fastest

7z a pack.zip assets pack.png pack.mcmeta

git add .
git status -s
$message = Read-Host "Enter Git Commit Title"
git commit -m $message
git push -u origin main 

$hash = (Get-FileHash -a SHA1 pack.zip).Hash.ToLower()

echo ""
echo "pack.zip's sha1 hash:"
echo $hash
$hash | clip
