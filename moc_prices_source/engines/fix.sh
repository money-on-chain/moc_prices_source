#!/bin/bash
for FILE in $(ls ars_usd*); do
    NEW_FILE=$(echo $FILE | awk '{sub(/ars_usd/,"usd_ars"); print}')
    awk '{sub(/ARS_USD/,"USD_ARS"); print}' $FILE > $NEW_FILE
done
for FILE in $(ls mxn_usd*); do
    NEW_FILE=$(echo $FILE | awk '{sub(/mxn_usd/,"usd_mxn"); print}')
    awk '{sub(/MXN_USD/,"USD_MXN"); print}' $FILE > $NEW_FILE
done
rm ars_usd*
rm mxn_usd*
