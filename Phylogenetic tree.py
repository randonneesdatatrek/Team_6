#!/usr/bin/env python
# coding: utf-8

# In[4]:


from Bio import Phylo
tree = Phylo.read("C:/Users/souissi/Desktop/coronavirus 2/unaligned.dnd", "newick")
Phylo.draw_ascii(tree)

