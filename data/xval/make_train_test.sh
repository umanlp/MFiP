#! /bin/bash

sed -n '1, 1505 p' MFiP_all_frames_with_negative_samples.tsv >fold1.tsv
sed -n '1506, 3031 p' MFiP_all_frames_with_negative_samples.tsv >fold2.tsv
sed -n '3032, 4554 p' MFiP_all_frames_with_negative_samples.tsv >fold3.tsv
sed -n '4555, 6057 p' MFiP_all_frames_with_negative_samples.tsv >fold4.tsv
sed -n '6058, $ p' MFiP_all_frames_with_negative_samples.tsv >fold5.tsv



for i in $(seq 1 5)
do
	for opt in train.tsv test.tsv
	do
	echo "docid	words	frametype	frame	mf	tags" >fold$i/$opt
	done
done

cat fold1.tsv >>fold1/test.tsv
cat fold2.tsv >>fold2/test.tsv
cat fold3.tsv >>fold3/test.tsv
cat fold4.tsv >>fold4/test.tsv
cat fold5.tsv >>fold5/test.tsv

cat fold2.tsv fold3.tsv fold4.tsv fold5.tsv >>fold1/train.tsv
cat fold3.tsv fold4.tsv fold5.tsv fold1.tsv >>fold2/train.tsv
cat fold4.tsv fold5.tsv fold1.tsv fold2.tsv >>fold3/train.tsv
cat fold5.tsv fold1.tsv fold2.tsv fold3.tsv >>fold4/train.tsv
cat fold1.tsv fold2.tsv fold3.tsv fold4.tsv >>fold5/train.tsv

