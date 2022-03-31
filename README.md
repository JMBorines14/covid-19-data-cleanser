# Covid-19 Data Cleanser Script

This script was used to clean the DOH Covid-19 data drop CSV file, by applying the following changes:
<ol>
  <li> Creating a new column <i> Repatriate </i> if the Region of Residence of a Covid-19 patient is "ROF" </li>
  <li> Changing the format of the Age Group column (e.g. from '0 to 4' to '00 to 04') </li>
  <li> Changing the format of the Region of Residence column to a specified format (e.g. from 'Region I: Ilocos Region' to '01 - Region 1') </li>
  <li> Changing the format of date columns </li>
  <li> Replacing Ñ with N </li>
</ol>

# Input, Output
<ul>
  <li> This script takes in the case_information CSV file from the DOH Covid-19 Tracker (https://doh.gov.ph/covid19tracker), and will output a new CSV file containing the changes to the Data Drop. The resulting CSV file upon running this script was imported to Tableau to create Covid-19 visualizations across different regions in the Philippines. </li>
  <li> This script uses both numpy and pandas library </li>
</ul>
