
import os.path as path
import pubmed_parser as pp

root_path = '/Users/jim/Documents/repos/orgs/scholar_tools/pubmed_db_data'

file_path = path.join(root_path,'pubmed20n0001.xml.gz')
file_path = path.join(root_path,'pubmed20n1014.xml.gz')

dicts_out = pp.parse_medline_xml(file_path,
                                 reference_list=True) # return list of dictionary



#dicts_out = pp.parse_medline_xml('data/medline16n0902.xml.gz',
#                                 year_info_only=False,
#                                 nlm_category=False,
#                                 author_list=False,
#                                 reference_list=False) # return list of dictionary


