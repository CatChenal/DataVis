#!/bin/bash

## all files:
# ls  img/| egrep '\.png|\.svg'
#6_Sigma_Normal_distribution.svg.png
#Climate Data - New York region.png
#Four distributions.svg
#My 6_sigma Normal Dist Fig.svg
#My 6_sigma Normal Dist Fig_200.png

#

list=(img/Four distributions.svg  img/My 6_sigma Normal Dist Fig.svg)
str=''
for f in $(echo list) do
    str=str + '<img src=" ' + f +  ' ", align="left"/>\n'
done

echo str > img_links.html