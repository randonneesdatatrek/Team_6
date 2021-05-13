#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Bio.Align.Applications import ClustalwCommandline
in_file = "C:/Users/souissi/Desktop/covid 19 teen/unaligned.fasta"
app_path = "C:/Program Files (x86)/ClustalW2"
app_executable = "clustalw2"
app_aligner = app_path +"/" + app_executable 
clustalw_cline = ClustalwCommandline(app_aligner, infile=in_file)
#print(clustalw_cline)
print(type(clustalw_cline))


# In[3]:


clustalw_cline()

