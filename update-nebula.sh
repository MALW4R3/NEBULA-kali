#!/bin/bash
cd
rm -rf NEBULA-kali
git clone https://github.com/MALW4R3/NEBULA-kali
cd ..
cd ..
cd bin
rm -rf nebula
cd
cd NEBULA-kali
sh setup.sh
cat update.txt | lolcat