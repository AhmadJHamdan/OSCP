# this script is mainly to turn off the computer after making sure the downloaded file is completed so 
# I don't wait it till it is done and I can sleep restfully before the download is completed...

# main usage: ./checkdownloaded.sh downloaded_file_name destination_directory command_to_be_executed

while true
do 
if [[ $(ls $2) = $1 ]]
then
echo "[+] Download Completed..."
break
else
echo "[-] Download In Progress..."
sleep 300 # the script will wait 5 minuted 
fi
done
$3
