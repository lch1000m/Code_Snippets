
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf


yf.pdr_override()
mcd = pdr.get_data_yahoo("009150.KS", start="2016-01-01", end="2018-10-24")

mcd.to_csv(r'C:\Codes\Snippets\stock trading\sample.txt', index=True, sep='\t')
