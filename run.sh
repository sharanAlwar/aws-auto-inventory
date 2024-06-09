echo -e "\e[1;31m:!--Staring run.sh--!:\e[0m"
echo -e "\e[1;31m:!--Changing permissions of running-aws-auto.sh & running-collection2csv.sh--!:\e[0m"
chmod +x running-aws-auto.sh
chmod +x running-collection2csv.sh
echo -e "\e[1;31m:!--Running aws-auto.sh--!:\e[0m"
./running-aws-auto.sh
echo -e "\e[1;31m:!--Completed aws-auto.sh--!:\e[0m"
echo -e "\e[1;31m:!--Staring collection2csv.sh--!:\e[0m"
./running-collection2csv.sh
echo -e "\e[1;31m:!--Completed collection2csv.sh--!:\e[0m"