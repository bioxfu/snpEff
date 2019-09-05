### annotate snpEff
wget http://sourceforge.net/projects/snpeff/files/snpEff_latest_core.zip
unzip snpEff_latest_core.zip

# add following two lines in snpEff.config file
# # Arabidopsis gene, TAIR10
# tair10.genome: Arabidopsis

# build database
mkdir -p snpEff/data/tair10
cd snpEff/data/tair10
ln -s /home/xfu/Gmatic7/gene/tair10/tair10.gtf genes.gtf
ln -s /home/xfu/Gmatic7/genome/tair10/tair10.fa sequences.fa
cd ../../
java -jar snpEff.jar build -gtf22 -v tair10 

## annotation
cd ..
java -jar snpEff/snpEff.jar -v tair10 test.vcf > test.vcf
python parse_snpEff_vcf.py test.vcf > test.tsv
