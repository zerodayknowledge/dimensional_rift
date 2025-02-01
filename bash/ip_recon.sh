#! /bin/zsh
rm myIpScriptOutput.txt -f
rm myIpOnlyOutput.txt -f
rm myUsableIp.txt -f
rm finalIp.txt -f
rm myAttackBox.txt -f
rm nmapData.txt -f
rm nmapData2.txt -f
rm nmapData3.txt -f
ip a >> myIpScriptOutput.txt
grep -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' myIpScriptOutput.txt >> myIpOnlyOutput.txt
grep -v -E '127\.0\.0\.1' myIpOnlyOutput.txt >> myUsableIp.txt
cat myUsableIp.txt | cut -c 10-18 >> myAttackBox.txt
cat myUsableIp.txt | cut -c 10-15 >> finalIp.txt
ip_data=$(cat finalIp.txt)
searchable_subnet="$ip_data.0/24"
echo "Nmap script starting"
sudo nmap -sS "$searchable_subnet" >> nmapData.txt
grep -v -E 'All 1000' nmapData.txt >> nmapData2.txt
echo "IP Addresses Found on Subnet"
grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' nmapData2.txt
echo "My Attack Box IP Address"
cat myAttackBox.txt
echo "Nmap script completed"
rm myIpScriptOutput.txt -f
rm myIpOnlyOutput.txt -f
rm myUsableIp.txt -f
rm finalIp.txt -f
rm myAttackBox.txt -f
rm nmapData.txt -f
rm nmapData2.txt -f
rm nmapData3.txt -f