import sys
import re

print('chr\tpos\tref\talt\ttype\tgene\ttranscript\tnc\taa\tcoverage\talt_rate')

with open(sys.argv[1]) as f:
	for line in f:
		if not line.startswith('#'):
			lst = line.strip().split('\t')
			DP4 = re.sub('.*DP4=', '', lst[7])
			DP4 = re.sub(';.*MQ=.*', '', DP4)
			ref_f, ref_r, alt_f, alt_r = [float(x) for x in DP4.split(',')]
			cov = alt_f + alt_r + ref_f + ref_r
			alt_rate = (alt_f + alt_r) / cov

			eff = re.sub('.*ANN=', 'ANN=', lst[7])
			if eff.startswith('ANN='):
				records = eff[4:].split(',')
				for record in records:
					if 'synonymous_variant' in record or 'missense_variant' in record or 'start_lost' in record or 'stop_gained' in record:
						tmp = record.split('|')
						#print(tmp)
						print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(lst[0],lst[1],lst[3],tmp[0],tmp[1],tmp[3],tmp[6],tmp[9],tmp[10],cov,round(alt_rate, 4)))

